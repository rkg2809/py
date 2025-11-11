"""Generate markdown documentation for all public Python APIs in the repository.

This script walks every ``.py`` file underneath the repository root, extracts
module metadata, top-level functions, classes, and their public members, and
writes a comprehensive markdown reference to ``docs/API_REFERENCE.md``.

Usage
-----
Run the script from the repository root:

    python3 scripts/generate_api_docs.py

Dependencies: standard library only.
"""

from __future__ import annotations

import ast
import datetime as _dt
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_PATH = REPO_ROOT / "docs" / "API_REFERENCE.md"


def _is_public(name: str) -> bool:
    return not name.startswith("_")


def _strip_docstring(docstring: Optional[str]) -> Optional[str]:
    if docstring is None:
        return None
    return textwrap.dedent(docstring).strip() or None


def _unparse(node: Optional[ast.AST]) -> Optional[str]:
    if node is None:
        return None
    try:
        return ast.unparse(node)
    except Exception:
        return None


def _format_default(node: Optional[ast.AST]) -> Optional[str]:
    default = _unparse(node)
    return default


def _guess_example_value(
    param_name: str, default_repr: Optional[str], annotation: Optional[str] = None
) -> str:
    if default_repr is not None:
        return default_repr

    annotation_lower = annotation.lower() if annotation else None
    if annotation_lower in {"int", "float", "complex", "decimal"}:
        return "1"
    if annotation_lower in {"str", "string"}:
        return f"\"{param_name}\""
    if annotation_lower in {"bool"}:
        return "True"
    if annotation_lower in {"list", "sequence", "tuple", "set"}:
        return "[]"
    if annotation_lower in {"dict", "mapping"}:
        return "{}"
    if annotation_lower and "path" in annotation_lower:
        return "\"/path/to/resource\""
    if annotation and annotation[0].isupper():
        if annotation_lower and "enum" in annotation_lower:
            return f"{annotation}.SAMPLE_VALUE"
        return f"{annotation}(...)"

    lowered = param_name.lower()
    numeric_markers = (
        "count",
        "num",
        "number",
        "size",
        "len",
        "length",
        "width",
        "height",
        "radius",
        "index",
        "idx",
        "id",
        "code",
        "age",
        "amount",
        "quantity",
        "level",
        "limit",
        "score",
        "value",
        "n",
        "m",
        "x",
        "y",
        "z",
    )
    path_markers = ("path", "file", "dir", "folder", "name")
    bool_markers = ("flag", "enable", "use_", "is_", "should", "allow", "has", "with_")

    if any(marker in lowered for marker in numeric_markers):
        return "1"
    if any(marker in lowered for marker in path_markers):
        return "\"/path/to/resource\""
    if any(marker in lowered for marker in bool_markers):
        return "True"
    return f"\"{param_name}\""


def _format_arguments(args: ast.arguments) -> str:
    def format_arg(arg: ast.arg, default: Optional[ast.AST]) -> str:
        annotation = _unparse(arg.annotation)
        ann = f": {annotation}" if annotation else ""
        default_repr = _format_default(default)
        if default_repr is not None:
            return f"{arg.arg}{ann}={default_repr}"
        return f"{arg.arg}{ann}"

    pieces: List[str] = []

    # To keep the logic tractable we handle positionals and their defaults together.
    total_pos_args = args.posonlyargs + args.args
    defaults = [None] * (len(total_pos_args) - len(args.defaults)) + list(args.defaults)
    for arg, default in zip(total_pos_args, defaults):
        pieces.append(format_arg(arg, default))

    if args.vararg is not None:
        var_annotation = _unparse(args.vararg.annotation)
        if var_annotation:
            pieces.append(f"*{args.vararg.arg}: {var_annotation}")
        else:
            pieces.append(f"*{args.vararg.arg}")

    if args.kwonlyargs:
        if args.vararg is None:
            pieces.append("*")
        for arg, default in zip(args.kwonlyargs, args.kw_defaults):
            pieces.append(format_arg(arg, default))

    if args.kwarg is not None:
        kw_annotation = _unparse(args.kwarg.annotation)
        if kw_annotation:
            pieces.append(f"**{args.kwarg.arg}: {kw_annotation}")
        else:
            pieces.append(f"**{args.kwarg.arg}")

    return ", ".join(pieces)


def _build_example_call(name: str, args: ast.arguments) -> str:
    arg_strings: List[str] = []
    defaults = [None] * (len(args.args) - len(args.defaults)) + list(args.defaults)

    for arg, default in zip(args.args, defaults):
        if arg.arg in {"self", "cls"}:
            continue
        default_repr = _format_default(default)
        annotation = _unparse(arg.annotation)
        example_value = _guess_example_value(arg.arg, default_repr, annotation)
        arg_strings.append(f"{arg.arg}={example_value}")

    if args.vararg and args.vararg.arg not in {"self", "cls"}:
        arg_strings.append(f"*{args.vararg.arg}")
    for arg, default in zip(args.kwonlyargs, args.kw_defaults):
        default_repr = _format_default(default)
        annotation = _unparse(arg.annotation)
        example_value = _guess_example_value(arg.arg, default_repr, annotation)
        arg_strings.append(f"{arg.arg}={example_value}")

    call_args = ", ".join(arg_strings)
    return f"{name}({call_args})" if call_args else f"{name}()"


def _module_has_runtime_code(module: ast.Module) -> bool:
    for node in module.body:
        # Skip module docstring expression
        if isinstance(node, ast.Expr) and isinstance(
            node.value, (ast.Str, ast.Constant)
        ):
            if (
                isinstance(node.value, ast.Str)
                or (
                    isinstance(node.value, ast.Constant)
                    and isinstance(node.value.value, str)
                )
            ):
                if node is module.body[0]:
                    continue

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
                ast.Import,
                ast.ImportFrom,
                ast.Assign,
                ast.AnnAssign,
                ast.AugAssign,
            ),
        ):
            continue
        return True
    return False


@dataclass
class FunctionDoc:
    name: str
    signature: str
    docstring: Optional[str]
    example_call: str
    is_async: bool = False


@dataclass
class MethodDoc(FunctionDoc):
    pass


def _extract_call_args(call_expression: str) -> str:
    if "(" in call_expression and call_expression.endswith(")"):
        return call_expression[call_expression.index("(") + 1 : -1]
    return ""


def _format_method_usage(cls_name: str, method: Optional[MethodDoc]) -> str:
    if method is None:
        return f"{cls_name}()"
    args_str = _extract_call_args(method.example_call)
    async_prefix = "await " if method.is_async else ""
    if method.name == "__init__":
        call = f"{cls_name}({args_str})" if args_str else f"{cls_name}()"
        return call
    if method.name == "__call__":
        call = f"{async_prefix}instance({args_str})" if args_str else f"{async_prefix}instance()"
        return call.strip()
    call_body = f"instance.{method.name}({args_str})" if args_str else f"instance.{method.name}()"
    return f"{async_prefix}{call_body}".strip()


@dataclass
class ClassDoc:
    name: str
    bases: List[str] = field(default_factory=list)
    docstring: Optional[str] = None
    methods: List[MethodDoc] = field(default_factory=list)


@dataclass
class ModuleDoc:
    path: Path
    module_name: str
    docstring: Optional[str]
    functions: List[FunctionDoc] = field(default_factory=list)
    classes: List[ClassDoc] = field(default_factory=list)
    has_runtime_code: bool = False
    parse_error: Optional[str] = None


def parse_module(path: Path) -> ModuleDoc:
    relative = path.relative_to(REPO_ROOT)
    module_parts = relative.with_suffix("").parts
    if module_parts[-1] == "__init__":
        module_name = ".".join(module_parts[:-1])
    else:
        module_name = ".".join(module_parts)

    module_doc = ModuleDoc(path=relative, module_name=module_name, docstring=None)

    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(relative))
    except Exception as exc:  # pragma: no cover - best effort logging
        module_doc.parse_error = str(exc)
        return module_doc

    module_doc.docstring = _strip_docstring(ast.get_docstring(tree))
    module_doc.has_runtime_code = _module_has_runtime_code(tree)

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not _is_public(node.name):
                continue
            signature = _format_arguments(node.args)
            example_call = _build_example_call(node.name, node.args)
            module_doc.functions.append(
                FunctionDoc(
                    name=node.name,
                    signature=signature,
                    docstring=_strip_docstring(ast.get_docstring(node)),
                    example_call=example_call,
                    is_async=isinstance(node, ast.AsyncFunctionDef),
                )
            )
        elif isinstance(node, ast.ClassDef) and _is_public(node.name):
            bases = [_unparse(base) or "" for base in node.bases]
            class_doc = ClassDoc(
                name=node.name,
                bases=[b for b in bases if b],
                docstring=_strip_docstring(ast.get_docstring(node)),
            )

            for class_node in node.body:
                if isinstance(class_node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if not _is_public(class_node.name) and class_node.name not in {
                        "__init__",
                        "__call__",
                        "__enter__",
                        "__exit__",
                    }:
                        continue
                    signature = _format_arguments(class_node.args)
                    example_call = _build_example_call(class_node.name, class_node.args)
                    class_doc.methods.append(
                        MethodDoc(
                            name=class_node.name,
                            signature=signature,
                            docstring=_strip_docstring(ast.get_docstring(class_node)),
                            example_call=example_call,
                            is_async=isinstance(class_node, ast.AsyncFunctionDef),
                        )
                    )
            module_doc.classes.append(class_doc)

    module_doc.functions.sort(key=lambda f: f.name)
    for class_doc in module_doc.classes:
        class_doc.methods.sort(key=lambda m: m.name)
    module_doc.classes.sort(key=lambda c: c.name)

    return module_doc


def iter_python_files() -> Iterable[Path]:
    ignored_dirs = {
        ".git",
        "__pycache__",
        ".mypy_cache",
        ".pytest_cache",
        ".venv",
        "env",
        "venv",
        "build",
        "dist",
        ".idea",
        ".vscode",
        ".cursor",
    }
    for path in REPO_ROOT.rglob("*.py"):
        if any(part in ignored_dirs for part in path.parts):
            continue
        if path.is_symlink():
            continue
        yield path


def render_module_doc(module_doc: ModuleDoc) -> str:
    lines: List[str] = []
    header_path = module_doc.path.as_posix()
    lines.append(f"## Module `{header_path}`\n")
    lines.append(f"- **Import Path**: `{module_doc.module_name or '<top-level>'}`")

    if module_doc.parse_error:
        lines.append(f"- **Status**: ⚠️ Could not parse module (`{module_doc.parse_error}`)\n")
        return "\n".join(lines)

    if module_doc.docstring:
        lines.append("- **Summary**:")
        lines.append(f"  {module_doc.docstring}\n")
    else:
        lines.append("- **Summary**: _No module docstring provided._\n")

    if module_doc.has_runtime_code:
        lines.append(
            "- **Runtime Behavior**: This module executes statements at import time "
            "(for example, example/demo code). Consider wrapping demo code in "
            "`if __name__ == \"__main__\":` to avoid side effects.\n"
        )
    else:
        lines.append("- **Runtime Behavior**: Safe to import (no side-effectful statements).\n")

    if module_doc.functions:
        lines.append("### Functions\n")
        for func in module_doc.functions:
            qualifier = "async " if func.is_async else ""
            lines.append(f"#### `{qualifier}{func.name}({func.signature})`\n")
            if func.docstring:
                lines.append(f"{func.docstring}\n")
            else:
                lines.append("_No docstring provided._\n")

            lines.append("**Usage Example:**")
            lines.append("```python")
            import_line = (
                f"from {module_doc.module_name} import {func.name}"
                if module_doc.module_name
                else f"import {module_doc.path.stem} as module"
            )
            lines.append(import_line)
            if module_doc.module_name:
                lines.append("")
                call_line = f"{func.example_call}"
                if func.is_async:
                    call_line = f"await {call_line}  # inside an async context"
                lines.append(call_line)
            else:
                lines.append("")
                call_line = f"module.{func.example_call}"
                if func.is_async:
                    call_line = f"await {call_line}  # inside an async context"
                lines.append(call_line)
            lines.append("```\n")
    else:
        lines.append("### Functions\n")
        lines.append("_No public functions defined._\n")

    if module_doc.classes:
        lines.append("### Classes\n")
        for cls in module_doc.classes:
            bases = f"({', '.join(cls.bases)})" if cls.bases else ""
            lines.append(f"#### `class {cls.name}{bases}`\n")
            if cls.docstring:
                lines.append(f"{cls.docstring}\n")
            else:
                lines.append("_No docstring provided._\n")

            lines.append("**Instantiation Example:**")
            lines.append("```python")
            if module_doc.module_name:
                lines.append(f"from {module_doc.module_name} import {cls.name}")
                lines.append("")
                init_method = next((m for m in cls.methods if m.name == '__init__'), None)
                init_call = _format_method_usage(cls.name, init_method) if init_method else f"{cls.name}()"
                lines.append(f"instance = {init_call}")
            else:
                lines.append(f"import {module_doc.path.stem} as module")
                lines.append("")
                init_method = next((m for m in cls.methods if m.name == '__init__'), None)
                init_call = _format_method_usage(cls.name, init_method) if init_method else f"{cls.name}()"
                lines.append(f"instance = module.{init_call}")
            lines.append("```\n")

            if cls.methods:
                lines.append("_Methods:_\n")
                for method in cls.methods:
                    qualifier = "async " if method.is_async else ""
                    lines.append(f"- `{qualifier}{method.name}({method.signature})`")
                    if method.docstring:
                        lines.append(f"  - {method.docstring}")
                    else:
                        lines.append("  - _No docstring provided._")
                    example_usage = _format_method_usage(cls.name, method)
                    lines.append(f"  - Example call: `{example_usage}`")
                lines.append("")
            else:
                lines.append("_No public methods documented._\n")
    else:
        lines.append("### Classes\n")
        lines.append("_No public classes defined._\n")

    return "\n".join(lines)


def build_documentation() -> str:
    header = [
        "# Repository API Documentation",
        "",
        f"_Generated on {_dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')}._",
        "",
        "This reference captures all public functions, classes, and methods discovered in "
        "the repository's Python source files. Use the file import paths when integrating "
        "these utilities into your own scripts.",
        "",
        "---",
        "",
    ]

    module_docs = [parse_module(path) for path in sorted(iter_python_files())]
    body_sections = [render_module_doc(module_doc) for module_doc in module_docs]
    return "\n".join(header + body_sections)


def main() -> None:
    DOCS_PATH.parent.mkdir(parents=True, exist_ok=True)
    documentation = build_documentation()
    DOCS_PATH.write_text(documentation, encoding="utf-8")
    print(f"Documentation written to {DOCS_PATH}")


if __name__ == "__main__":  # pragma: no cover
    main()
