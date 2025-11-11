# Repository API Documentation

_Generated on 2025-11-11 21:48:34 ._

This reference captures all public functions, classes, and methods discovered in the repository's Python source files. Use the file import paths when integrating these utilities into your own scripts.

---

## Module `Advanced/FastAPI/main.py`

- **Import Path**: `Advanced.FastAPI.main`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

#### `async get_items(cuisine: AvailableCuisines)`

_No docstring provided._

**Usage Example:**
```python
from Advanced.FastAPI.main import get_items

await get_items(cuisine=AvailableCuisines(...))  # inside an async context
```

#### `async get_items(code: int)`

_No docstring provided._

**Usage Example:**
```python
from Advanced.FastAPI.main import get_items

await get_items(code=1)  # inside an async context
```

#### `async hello()`

_No docstring provided._

**Usage Example:**
```python
from Advanced.FastAPI.main import hello

await hello()  # inside an async context
```

#### `async hello(name)`

_No docstring provided._

**Usage Example:**
```python
from Advanced.FastAPI.main import hello

await hello(name=1)  # inside an async context
```

### Classes

#### `class AvailableCuisines(str, Enum)`

_No docstring provided._

**Instantiation Example:**
```python
from Advanced.FastAPI.main import AvailableCuisines

instance = AvailableCuisines()
```

_No public methods documented._

## Module `Advanced/decorators.py`

- **Import Path**: `Advanced.decorators`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

#### `calc_cube(numbers)`

_No docstring provided._

**Usage Example:**
```python
from Advanced.decorators import calc_cube

calc_cube(numbers=1)
```

#### `calc_square(numbers)`

_No docstring provided._

**Usage Example:**
```python
from Advanced.decorators import calc_square

calc_square(numbers=1)
```

#### `time_it(func)`

_No docstring provided._

**Usage Example:**
```python
from Advanced.decorators import time_it

time_it(func=1)
```

### Classes

_No public classes defined._

## Module `Basics/13_read_write_file.py`

- **Import Path**: `Basics.13_read_write_file`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `count_num_in_file(file_path, num)`

_No docstring provided._

**Usage Example:**
```python
from Basics.13_read_write_file import count_num_in_file

count_num_in_file(file_path="/path/to/resource", num=1)
```

#### `count_num_in_tokens(tokens, num)`

_No docstring provided._

**Usage Example:**
```python
from Basics.13_read_write_file import count_num_in_tokens

count_num_in_tokens(tokens=1, num=1)
```

#### `sum_numbers(file_path)`

_No docstring provided._

**Usage Example:**
```python
from Basics.13_read_write_file import sum_numbers

sum_numbers(file_path="/path/to/resource")
```

#### `sum_tokens(tokens)`

_No docstring provided._

**Usage Example:**
```python
from Basics.13_read_write_file import sum_tokens

sum_tokens(tokens=1)
```

### Classes

_No public classes defined._

## Module `Basics/14_json_addressbook.py`

- **Import Path**: `Basics.14_json_addressbook`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/16_exception.py`

- **Import Path**: `Basics.16_exception`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/17_class.py`

- **Import Path**: `Basics.17_class`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

#### `class Human`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.17_class import Human

instance = Human(n=1, o="o")
```

_Methods:_

- `__init__(self, n, o)`
  - _No docstring provided._
  - Example call: `Human(n=1, o="o")`
- `do_work(self)`
  - _No docstring provided._
  - Example call: `instance.do_work()`
- `speaks(self)`
  - _No docstring provided._
  - Example call: `instance.speaks()`

## Module `Basics/18_inheritance.py`

- **Import Path**: `Basics.18_inheritance`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

#### `class Car(Vehicle)`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.18_inheritance import Car

instance = Car()
```

_Methods:_

- `__init__(self)`
  - _No docstring provided._
  - Example call: `Car()`
- `specific_usage(self)`
  - _No docstring provided._
  - Example call: `instance.specific_usage()`

#### `class MotorCycle(Vehicle)`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.18_inheritance import MotorCycle

instance = MotorCycle()
```

_Methods:_

- `__init__(self)`
  - _No docstring provided._
  - Example call: `MotorCycle()`
- `specific_usage(self)`
  - _No docstring provided._
  - Example call: `instance.specific_usage()`

#### `class Vehicle`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.18_inheritance import Vehicle

instance = Vehicle()
```

_Methods:_

- `general_usage(self)`
  - _No docstring provided._
  - Example call: `instance.general_usage()`

## Module `Basics/19_multiple_inheritance.py`

- **Import Path**: `Basics.19_multiple_inheritance`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

#### `class Child(Father, Mother)`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.19_multiple_inheritance import Child

instance = Child()
```

_Methods:_

- `skills(self)`
  - _No docstring provided._
  - Example call: `instance.skills()`

#### `class Father`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.19_multiple_inheritance import Father

instance = Father()
```

_Methods:_

- `skills(self)`
  - _No docstring provided._
  - Example call: `instance.skills()`

#### `class Mother`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.19_multiple_inheritance import Mother

instance = Mother()
```

_Methods:_

- `skills(self)`
  - _No docstring provided._
  - Example call: `instance.skills()`

## Module `Basics/20_raise_exception.py`

- **Import Path**: `Basics.20_raise_exception`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `process_file()`

_No docstring provided._

**Usage Example:**
```python
from Basics.20_raise_exception import process_file

process_file()
```

### Classes

_No public classes defined._

## Module `Basics/21_iterators.py`

- **Import Path**: `Basics.21_iterators`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

#### `class RemoteControl`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.21_iterators import RemoteControl

instance = RemoteControl()
```

_Methods:_

- `__init__(self)`
  - _No docstring provided._
  - Example call: `RemoteControl()`

## Module `Basics/22_Generators.py`

- **Import Path**: `Basics.22_Generators`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `fib()`

_No docstring provided._

**Usage Example:**
```python
from Basics.22_Generators import fib

fib()
```

### Classes

_No public classes defined._

## Module `Basics/Exercise/10_functions/10_functions_exercise.py`

- **Import Path**: `Basics.Exercise.10_functions.10_functions_exercise`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `calculate_area(dimension1, dimension2, shape='triangle')`

:param dimension1: In case of triangle it is "base". For rectangle it is "length".
:param dimension2: In case of triangle it is "height". For rectangle it is "width".
:param shape: Either "triangle" or "rectangle"
:return: Area of a shape

**Usage Example:**
```python
from Basics.Exercise.10_functions.10_functions_exercise import calculate_area

calculate_area(dimension1=1, dimension2=1, shape='triangle')
```

#### `print_pattern(n=5)`

:param n: Integer number representing number of lines
to be printed in a pattern. If n=3 it will print,
  *
  **
  ***
If n=4, it will print,
  *
  **
  ***
  ****
Default value for n is 5. So if function caller doesn't
supply the input number then it will assume it to be 5
:return: None

**Usage Example:**
```python
from Basics.Exercise.10_functions.10_functions_exercise import print_pattern

print_pattern(n=5)
```

### Classes

_No public classes defined._

## Module `Basics/Exercise/11_dict_tuples/11_dict_exercise_1_country_population.py`

- **Import Path**: `Basics.Exercise.11_dict_tuples.11_dict_exercise_1_country_population`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `add()`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.11_dict_tuples.11_dict_exercise_1_country_population import add

add()
```

#### `main()`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.11_dict_tuples.11_dict_exercise_1_country_population import main

main()
```

#### `print_all()`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.11_dict_tuples.11_dict_exercise_1_country_population import print_all

print_all()
```

#### `query()`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.11_dict_tuples.11_dict_exercise_1_country_population import query

query()
```

#### `remove()`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.11_dict_tuples.11_dict_exercise_1_country_population import remove

remove()
```

### Classes

_No public classes defined._

## Module `Basics/Exercise/11_dict_tuples/11_dict_exercise_2_stocks.py`

- **Import Path**: `Basics.Exercise.11_dict_tuples.11_dict_exercise_2_stocks`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `add()`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.11_dict_tuples.11_dict_exercise_2_stocks import add

add()
```

#### `main()`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.11_dict_tuples.11_dict_exercise_2_stocks import main

main()
```

#### `print_all()`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.11_dict_tuples.11_dict_exercise_2_stocks import print_all

print_all()
```

### Classes

_No public classes defined._

## Module `Basics/Exercise/11_dict_tuples/11_dict_exercise_3_circle.py`

- **Import Path**: `Basics.Exercise.11_dict_tuples.11_dict_exercise_3_circle`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `circle_calc(radius)`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.11_dict_tuples.11_dict_exercise_3_circle import circle_calc

circle_calc(radius=1)
```

### Classes

_No public classes defined._

## Module `Basics/Exercise/13_read_write_files/exercise_1_poem.py`

- **Import Path**: `Basics.Exercise.13_read_write_files.exercise_1_poem`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/13_read_write_files/exercise_2_stocks.py`

- **Import Path**: `Basics.Exercise.13_read_write_files.exercise_2_stocks`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/15_exception_handling/exception_handling_solution.py`

- **Import Path**: `Basics.Exercise.15_exception_handling.exception_handling_solution`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/16_class_and_objects/16_class_and_objects.py`

- **Import Path**: `Basics.Exercise.16_class_and_objects.16_class_and_objects`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

#### `class Employee`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.Exercise.16_class_and_objects.16_class_and_objects import Employee

instance = Employee(id=1, name=1)
```

_Methods:_

- `__init__(self, id, name)`
  - _No docstring provided._
  - Example call: `Employee(id=1, name=1)`
- `display(self)`
  - _No docstring provided._
  - Example call: `instance.display()`

## Module `Basics/Exercise/17_inheritance/17_inheritance.py`

- **Import Path**: `Basics.Exercise.17_inheritance.17_inheritance`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

#### `class Animal`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.Exercise.17_inheritance.17_inheritance import Animal

instance = Animal(habitat="habitat")
```

_Methods:_

- `__init__(self, habitat)`
  - _No docstring provided._
  - Example call: `Animal(habitat="habitat")`
- `print_habitat(self)`
  - _No docstring provided._
  - Example call: `instance.print_habitat()`
- `sound(self)`
  - _No docstring provided._
  - Example call: `instance.sound()`

#### `class Dog(Animal)`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.Exercise.17_inheritance.17_inheritance import Dog

instance = Dog()
```

_Methods:_

- `__init__(self)`
  - _No docstring provided._
  - Example call: `Dog()`
- `sound(self)`
  - _No docstring provided._
  - Example call: `instance.sound()`

## Module `Basics/Exercise/18_multiple_inheritance/18_multiple_inheritance.py`

- **Import Path**: `Basics.Exercise.18_multiple_inheritance.18_multiple_inheritance`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

#### `class Engineer`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.Exercise.18_multiple_inheritance.18_multiple_inheritance import Engineer

instance = Engineer()
```

_Methods:_

- `Engineers_action(self)`
  - _No docstring provided._
  - Example call: `instance.Engineers_action()`

#### `class Person(Teacher, Engineer, Youtuber)`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.Exercise.18_multiple_inheritance.18_multiple_inheritance import Person

instance = Person()
```

_No public methods documented._

#### `class Teacher`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.Exercise.18_multiple_inheritance.18_multiple_inheritance import Teacher

instance = Teacher()
```

_Methods:_

- `teachers_action(self)`
  - _No docstring provided._
  - Example call: `instance.teachers_action()`

#### `class Youtuber`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.Exercise.18_multiple_inheritance.18_multiple_inheritance import Youtuber

instance = Youtuber()
```

_Methods:_

- `youtubers_action(self)`
  - _No docstring provided._
  - Example call: `instance.youtubers_action()`

## Module `Basics/Exercise/19_raise_exception_finally/19_raise_exception_finally.py`

- **Import Path**: `Basics.Exercise.19_raise_exception_finally.19_raise_exception_finally`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

#### `class AdultException(Exception)`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.Exercise.19_raise_exception_finally.19_raise_exception_finally import AdultException

instance = AdultException()
```

_No public methods documented._

#### `class Person`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.Exercise.19_raise_exception_finally.19_raise_exception_finally import Person

instance = Person(name=1, age=1)
```

_Methods:_

- `__init__(self, name, age)`
  - _No docstring provided._
  - Example call: `Person(name=1, age=1)`
- `display(self)`
  - _No docstring provided._
  - Example call: `instance.display()`
- `get_minor_age(self)`
  - _No docstring provided._
  - Example call: `instance.get_minor_age()`

## Module `Basics/Exercise/20_Iterators/20_Iterators.py`

- **Import Path**: `Basics.Exercise.20_Iterators.20_Iterators`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

#### `class Fibonacci`

_No docstring provided._

**Instantiation Example:**
```python
from Basics.Exercise.20_Iterators.20_Iterators import Fibonacci

instance = Fibonacci(limit=1)
```

_Methods:_

- `__init__(self, limit)`
  - _No docstring provided._
  - Example call: `Fibonacci(limit=1)`

## Module `Basics/Exercise/21_generators/21_generators.py`

- **Import Path**: `Basics.Exercise.21_generators.21_generators`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `next_square()`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.21_generators.21_generators import next_square

next_square()
```

### Classes

_No public classes defined._

## Module `Basics/Exercise/22_list_set_dict_comprehension/22_list_set_dict_comprehension.py`

- **Import Path**: `Basics.Exercise.22_list_set_dict_comprehension.22_list_set_dict_comprehension`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/23_sets_frozensets/23_sets_frozensets.py`

- **Import Path**: `Basics.Exercise.23_sets_frozensets.23_sets_frozensets`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/24_argparse/24_argparse.py`

- **Import Path**: `Basics.Exercise.24_argparse.24_argparse`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/25_decorators/25_decorators.py`

- **Import Path**: `Basics.Exercise.25_decorators.25_decorators`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `check(f)`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.25_decorators.25_decorators import check

check(f="f")
```

#### `factorial(n)`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.25_decorators.25_decorators import factorial

factorial(n=1)
```

### Classes

_No public classes defined._

## Module `Basics/Exercise/26_multithreading/26_multithreading.py`

- **Import Path**: `Basics.Exercise.26_multithreading.26_multithreading`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `sleepMe(i)`

_No docstring provided._

**Usage Example:**
```python
from Basics.Exercise.26_multithreading.26_multithreading import sleepMe

sleepMe(i="i")
```

### Classes

_No public classes defined._

## Module `Basics/Exercise/3_numbers/3_numbers_exercise.py`

- **Import Path**: `Basics.Exercise.3_numbers.3_numbers_exercise`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/4_strings/4_string_exercise_answer.py`

- **Import Path**: `Basics.Exercise.4_strings.4_string_exercise_answer`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/5_lists/5_lists_exercise.py`

- **Import Path**: `Basics.Exercise.5_lists.5_lists_exercise`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/8_if/8_exercise1_1.py`

- **Import Path**: `Basics.Exercise.8_if.8_exercise1_1`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/8_if/8_exercise1_2.py`

- **Import Path**: `Basics.Exercise.8_if.8_exercise1_2`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/8_if/8_exercise2.py`

- **Import Path**: `Basics.Exercise.8_if.8_exercise2`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Exercise/9_for/9_for_exercise.py`

- **Import Path**: `Basics.Exercise.9_for.9_for_exercise`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/10_name_/caller.py`

- **Import Path**: `Basics.Hindi.10_name_.caller`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/10_name_/utility.py`

- **Import Path**: `Basics.Hindi.10_name_.utility`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `foo()`

_No docstring provided._

**Usage Example:**
```python
from Basics.Hindi.10_name_.utility import foo

foo()
```

### Classes

_No public classes defined._

## Module `Basics/Hindi/12_read_write_file/12_read_write_file.py`

- **Import Path**: `Basics.Hindi.12_read_write_file.12_read_write_file`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/1_Variables/1_variables.py`

- **Import Path**: `Basics.Hindi.1_Variables.1_variables`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/2_numbers/2_numbers.py`

- **Import Path**: `Basics.Hindi.2_numbers.2_numbers`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/4_user_input/4_user_input.py`

- **Import Path**: `Basics.Hindi.4_user_input.4_user_input`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/4_user_input/Exercise/4_user_input_exercise.py`

- **Import Path**: `Basics.Hindi.4_user_input.Exercise.4_user_input_exercise`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/6_if/6_if.py`

- **Import Path**: `Basics.Hindi.6_if.6_if`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/7_for/7_for.py`

- **Import Path**: `Basics.Hindi.7_for.7_for`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/7_for/for_loop.py`

- **Import Path**: `Basics.Hindi.7_for.for_loop`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/8_functions/8_functions.py`

- **Import Path**: `Basics.Hindi.8_functions.8_functions`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `cylinder_volume(radius, height=1)`

_No docstring provided._

**Usage Example:**
```python
from Basics.Hindi.8_functions.8_functions import cylinder_volume

cylinder_volume(radius=1, height=1)
```

#### `find_total(exp)`

This function takes list of numbers as input and returns sum of that list
:param exp: input list
:return: total sum

**Usage Example:**
```python
from Basics.Hindi.8_functions.8_functions import find_total

find_total(exp=1)
```

### Classes

_No public classes defined._

## Module `Basics/Hindi/9_modules/main.py`

- **Import Path**: `Basics.Hindi.9_modules.main`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/Hindi/9_modules/utility/area.py`

- **Import Path**: `Basics.Hindi.9_modules.utility.area`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

#### `area_circle(radius)`

_No docstring provided._

**Usage Example:**
```python
from Basics.Hindi.9_modules.utility.area import area_circle

area_circle(radius=1)
```

#### `area_square(length)`

_No docstring provided._

**Usage Example:**
```python
from Basics.Hindi.9_modules.utility.area import area_square

area_square(length=1)
```

### Classes

_No public classes defined._

## Module `Basics/address.py`

- **Import Path**: `Basics.address`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/area.py`

- **Import Path**: `Basics.area`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `calculate_area(base, height)`

_No docstring provided._

**Usage Example:**
```python
from Basics.area import calculate_area

calculate_area(base="base", height=1)
```

### Classes

_No public classes defined._

## Module `Basics/caller.py`

- **Import Path**: `Basics.caller`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/dict_tuple.py`

- **Import Path**: `Basics.dict_tuple`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `add_and_multiple(n1, n2)`

Exercise 2
:param n1: Number 1
:param n2: Number 2
:return: a tuple containing sum and multiplication of two input numbers

**Usage Example:**
```python
from Basics.dict_tuple import add_and_multiple

add_and_multiple(n1=1, n2=1)
```

#### `age_dictionary()`

Exercise 1
This program asks for person name and age and builds a dictionary using that
Later on you can input person name and it will tell you the age of that person
:return:

**Usage Example:**
```python
from Basics.dict_tuple import age_dictionary

age_dictionary()
```

### Classes

_No public classes defined._

## Module `Basics/for.py`

- **Import Path**: `Basics.for`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

#### `demo_break_marathon()`

break demo using running race

**Usage Example:**
```python
from Basics.for import demo_break_marathon

demo_break_marathon()
```

#### `demo_continue()`

Print square of all numbers between 1 to 10 except even numbers

**Usage Example:**
```python
from Basics.for import demo_continue

demo_continue()
```

#### `ex_expense_break()`

Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program
should tell you in which month that expense occurred.

**Usage Example:**
```python
from Basics.for import ex_expense_break

ex_expense_break()
```

#### `ex_heads_tails()`

After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out “heads” count.

**Usage Example:**
```python
from Basics.for import ex_heads_tails

ex_heads_tails()
```

#### `ex_print_shape()`

Write a program that prints following shape
*
**
***
****
*****

**Usage Example:**
```python
from Basics.for import ex_print_shape

ex_print_shape()
```

### Classes

_No public classes defined._

## Module `Basics/functions.py`

- **Import Path**: `Basics.functions`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `calculate_area(dimension1, dimension2, shape='triangle')`

:param dimension1: In case of triangle it is "base". For rectangle it is "length".
:param dimension2: In case of triangle it is "height". For rectangle it is "width".
:param shape: Either "triangle" or "rectangle"
:return: Area of a shape

**Usage Example:**
```python
from Basics.functions import calculate_area

calculate_area(dimension1=1, dimension2=1, shape='triangle')
```

#### `print_pattern(n=5)`

:param n: Integer number representing number of lines
to be printed in a pattern. If n=3 it will print,
  *
  **
  ***
If n=4, it will print,
  *
  **
  ***
  ****
Default value for n is 5. So if function caller doesn't
supply the input number then it will assume it to be 5
:return: None

**Usage Example:**
```python
from Basics.functions import print_pattern

print_pattern(n=5)
```

### Classes

_No public classes defined._

## Module `Basics/if.py`

- **Import Path**: `Basics.if`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `city_checker()`

if chapter exercise (a)

**Usage Example:**
```python
from Basics.if import city_checker

city_checker()
```

#### `city_country_checker()`

if chapter exercise (b)

**Usage Example:**
```python
from Basics.if import city_country_checker

city_country_checker()
```

#### `cuisine_checker()`

If tutorial

**Usage Example:**
```python
from Basics.if import cuisine_checker

cuisine_checker()
```

### Classes

_No public classes defined._

## Module `Basics/myprogram.py`

- **Import Path**: `Basics.myprogram`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Basics/test.py`

- **Import Path**: `Basics.test`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `sum(a, b)`

_No docstring provided._

**Usage Example:**
```python
from Basics.test import sum

sum(a="a", b="b")
```

### Classes

_No public classes defined._

## Module `Basics/variable_numbers_strings.py`

- **Import Path**: `Basics.variable_numbers_strings`
- **Status**: ⚠️ Could not parse module (`invalid character '½' (U+00BD) (variable_numbers_strings.py, line 11)`)

## Module `Basics/word_occurences.py`

- **Import Path**: `Basics.word_occurences`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `DataScience/BangloreHomePrices/server/server.py`

- **Import Path**: `DataScience.BangloreHomePrices.server.server`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `get_location_names()`

_No docstring provided._

**Usage Example:**
```python
from DataScience.BangloreHomePrices.server.server import get_location_names

get_location_names()
```

#### `predict_home_price()`

_No docstring provided._

**Usage Example:**
```python
from DataScience.BangloreHomePrices.server.server import predict_home_price

predict_home_price()
```

### Classes

_No public classes defined._

## Module `DataScience/BangloreHomePrices/server/util.py`

- **Import Path**: `DataScience.BangloreHomePrices.server.util`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `get_data_columns()`

_No docstring provided._

**Usage Example:**
```python
from DataScience.BangloreHomePrices.server.util import get_data_columns

get_data_columns()
```

#### `get_estimated_price(location, sqft, bhk, bath)`

_No docstring provided._

**Usage Example:**
```python
from DataScience.BangloreHomePrices.server.util import get_estimated_price

get_estimated_price(location=1, sqft="sqft", bhk="bhk", bath="bath")
```

#### `get_location_names()`

_No docstring provided._

**Usage Example:**
```python
from DataScience.BangloreHomePrices.server.util import get_location_names

get_location_names()
```

#### `load_saved_artifacts()`

_No docstring provided._

**Usage Example:**
```python
from DataScience.BangloreHomePrices.server.util import load_saved_artifacts

load_saved_artifacts()
```

### Classes

_No public classes defined._

## Module `DataScience/CelebrityFaceRecognition/google_image_scrapping/image_download.py`

- **Import Path**: `DataScience.CelebrityFaceRecognition.google_image_scrapping.image_download`
- **Summary**:
  Code credit:
https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d
Also thanks for Debjyoti Paul (my friend and data scientist at Amazon) for help with this

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `fetch_image_urls(query: str, max_links_to_fetch: int, wd, sleep_between_interactions: int=1, driver_path=None, target_path=None, search_term=None)`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.google_image_scrapping.image_download import fetch_image_urls

fetch_image_urls(query="query", max_links_to_fetch=1, wd="wd", sleep_between_interactions=1, driver_path=None, target_path=None, search_term=None)
```

#### `fetch_image_urls_util(url, driver_path)`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.google_image_scrapping.image_download import fetch_image_urls_util

fetch_image_urls_util(url="url", driver_path="/path/to/resource")
```

#### `persist_image(folder_path: str, url: str)`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.google_image_scrapping.image_download import persist_image

persist_image(folder_path="folder_path", url="url")
```

#### `search_and_download(search_term: str, driver_path: str, target_path='./datasets', number_images=50)`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.google_image_scrapping.image_download import search_and_download

search_and_download(search_term="search_term", driver_path="driver_path", target_path='./datasets', number_images=50)
```

### Classes

_No public classes defined._

## Module `DataScience/CelebrityFaceRecognition/server/server.py`

- **Import Path**: `DataScience.CelebrityFaceRecognition.server.server`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `classify_image()`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.server.server import classify_image

classify_image()
```

### Classes

_No public classes defined._

## Module `DataScience/CelebrityFaceRecognition/server/util.py`

- **Import Path**: `DataScience.CelebrityFaceRecognition.server.util`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `class_number_to_name(class_num)`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.server.util import class_number_to_name

class_number_to_name(class_num=1)
```

#### `classify_image(image_base64_data, file_path=None)`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.server.util import classify_image

classify_image(image_base64_data=1, file_path=None)
```

#### `get_b64_test_image_for_virat()`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.server.util import get_b64_test_image_for_virat

get_b64_test_image_for_virat()
```

#### `get_cropped_image_if_2_eyes(image_path, image_base64_data)`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.server.util import get_cropped_image_if_2_eyes

get_cropped_image_if_2_eyes(image_path=1, image_base64_data=1)
```

#### `get_cv2_image_from_base64_string(b64str)`

credit: https://stackoverflow.com/questions/33754935/read-a-base-64-encoded-image-from-memory-using-opencv-python-library
:param uri:
:return:

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.server.util import get_cv2_image_from_base64_string

get_cv2_image_from_base64_string(b64str="b64str")
```

#### `load_saved_artifacts()`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.server.util import load_saved_artifacts

load_saved_artifacts()
```

### Classes

_No public classes defined._

## Module `DataScience/CelebrityFaceRecognition/server/wavelet.py`

- **Import Path**: `DataScience.CelebrityFaceRecognition.server.wavelet`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

#### `w2d(img, mode='haar', level=1)`

_No docstring provided._

**Usage Example:**
```python
from DataScience.CelebrityFaceRecognition.server.wavelet import w2d

w2d(img=1, mode='haar', level=1)
```

### Classes

_No public classes defined._

## Module `Debugging/conditional_breakpoint.py`

- **Import Path**: `Debugging.conditional_breakpoint`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Debugging/debugging.py`

- **Import Path**: `Debugging.debugging`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `add_num(a, b)`

Return sum of two numbers

**Usage Example:**
```python
from Debugging.debugging import add_num

add_num(a="a", b="b")
```

### Classes

_No public classes defined._

## Module `Debugging/watches_callstack.py`

- **Import Path**: `Debugging.watches_callstack`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `bar()`

_No docstring provided._

**Usage Example:**
```python
from Debugging.watches_callstack import bar

bar()
```

#### `foo()`

_No docstring provided._

**Usage Example:**
```python
from Debugging.watches_callstack import foo

foo()
```

### Classes

_No public classes defined._

## Module `DeepLearningML/8_sgd_vs_gd/gradient_descent.py`

- **Import Path**: `DeepLearningML.8_sgd_vs_gd.gradient_descent`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `gradient_descent(x, y, epochs)`

_No docstring provided._

**Usage Example:**
```python
from DeepLearningML.8_sgd_vs_gd.gradient_descent import gradient_descent

gradient_descent(x=1, y=1, epochs="epochs")
```

### Classes

_No public classes defined._

## Module `ML/1_linear_reg/linearReg.py`

- **Import Path**: `ML.1_linear_reg.linearReg`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `ML/3_gradient_descent/Exercise/ex_gradient_descent.py`

- **Import Path**: `ML.3_gradient_descent.Exercise.ex_gradient_descent`
- **Summary**:
  Good students always try to solve exercise on their own first and then look at the ready made solution
I know you are an awesome student !! :)
Hence you will look into this code only after you have done your due diligence.
If you are not an awesome student who is full of laziness then only you will come here
without writing single line of code on your own. In that case anyways you are going to
face my anger with fire and fury !!!

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `gradient_descent(x, y)`

_No docstring provided._

**Usage Example:**
```python
from ML.3_gradient_descent.Exercise.ex_gradient_descent import gradient_descent

gradient_descent(x=1, y=1)
```

#### `predict_using_sklean()`

_No docstring provided._

**Usage Example:**
```python
from ML.3_gradient_descent.Exercise.ex_gradient_descent import predict_using_sklean

predict_using_sklean()
```

### Classes

_No public classes defined._

## Module `ML/3_gradient_descent/gradient_descent.py`

- **Import Path**: `ML.3_gradient_descent.gradient_descent`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `gradient_descent(x, y)`

_No docstring provided._

**Usage Example:**
```python
from ML.3_gradient_descent.gradient_descent import gradient_descent

gradient_descent(x=1, y=1)
```

### Classes

_No public classes defined._

## Module `Modules/argparse_tutorial.py`

- **Import Path**: `Modules.argparse_tutorial`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Modules/pandas_tutorial.py`

- **Import Path**: `Modules.pandas_tutorial`
- **Summary**:
  Introducing pandas using namespace pd,
such that you can call pandas class using pd instead of pandas.

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Modules/urllib_demo.py`

- **Import Path**: `Modules.urllib_demo`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `Multiprocessing/multiprocessing_introduction.py`

- **Import Path**: `Multiprocessing.multiprocessing_introduction`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `calc_cube(numbers)`

_No docstring provided._

**Usage Example:**
```python
from Multiprocessing.multiprocessing_introduction import calc_cube

calc_cube(numbers=1)
```

#### `calc_square(numbers)`

_No docstring provided._

**Usage Example:**
```python
from Multiprocessing.multiprocessing_introduction import calc_square

calc_square(numbers=1)
```

### Classes

_No public classes defined._

## Module `Multiprocessing/multiprocessing_lock.py`

- **Import Path**: `Multiprocessing.multiprocessing_lock`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `deposit(balance, lock)`

_No docstring provided._

**Usage Example:**
```python
from Multiprocessing.multiprocessing_lock import deposit

deposit(balance=1, lock="lock")
```

#### `withdraw(balance, lock)`

_No docstring provided._

**Usage Example:**
```python
from Multiprocessing.multiprocessing_lock import withdraw

withdraw(balance=1, lock="lock")
```

### Classes

_No public classes defined._

## Module `Multiprocessing/multiprocessing_pool.py`

- **Import Path**: `Multiprocessing.multiprocessing_pool`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `f(n)`

_No docstring provided._

**Usage Example:**
```python
from Multiprocessing.multiprocessing_pool import f

f(n=1)
```

### Classes

_No public classes defined._

## Module `Multiprocessing/multiprocessing_queue_pipe.py`

- **Import Path**: `Multiprocessing.multiprocessing_queue_pipe`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `calc_square(numbers, q)`

_No docstring provided._

**Usage Example:**
```python
from Multiprocessing.multiprocessing_queue_pipe import calc_square

calc_square(numbers=1, q="q")
```

### Classes

_No public classes defined._

## Module `Multiprocessing/multiprocessing_value_array.py`

- **Import Path**: `Multiprocessing.multiprocessing_value_array`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `calc_square(numbers, result, v)`

_No docstring provided._

**Usage Example:**
```python
from Multiprocessing.multiprocessing_value_array import calc_square

calc_square(numbers=1, result="result", v="v")
```

### Classes

_No public classes defined._

## Module `Multiprocessing/multithreading_producer_consumer.py`

- **Import Path**: `Multiprocessing.multithreading_producer_consumer`
- **Status**: ⚠️ Could not parse module (`expected an indented block after 'if' statement on line 14 (multithreading_producer_consumer.py, line 17)`)

## Module `Multiprocessing/multthreading_introduction.py`

- **Import Path**: `Multiprocessing.multthreading_introduction`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `calc_cube(numbers)`

_No docstring provided._

**Usage Example:**
```python
from Multiprocessing.multthreading_introduction import calc_cube

calc_cube(numbers=1)
```

#### `calc_square(numbers)`

_No docstring provided._

**Usage Example:**
```python
from Multiprocessing.multthreading_introduction import calc_square

calc_square(numbers=1)
```

### Classes

_No public classes defined._

## Module `TechTopics/LogicBuilding/ds.py`

- **Import Path**: `TechTopics.LogicBuilding.ds`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `TechTopics/LogicBuilding/triange_area.py`

- **Import Path**: `TechTopics.LogicBuilding.triange_area`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `jupyter/pandas_tutorial_on_stock_price.py`

- **Import Path**: `jupyter.pandas_tutorial_on_stock_price`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `numpy/numpy_tutorail_2.py`

- **Import Path**: `numpy.numpy_tutorail_2`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `numpy/numpy_tutorial.py`

- **Import Path**: `numpy.numpy_tutorial`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `pandas/1_intro/pandas_intro.py`

- **Import Path**: `pandas.1_intro.pandas_intro`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `get_average_wind_speed()`

_No docstring provided._

**Usage Example:**
```python
from pandas.1_intro.pandas_intro import get_average_wind_speed

get_average_wind_speed()
```

#### `get_days_for_event(event_name)`

_No docstring provided._

**Usage Example:**
```python
from pandas.1_intro.pandas_intro import get_days_for_event

get_days_for_event(event_name=1)
```

#### `get_max_temperature()`

_No docstring provided._

**Usage Example:**
```python
from pandas.1_intro.pandas_intro import get_max_temperature

get_max_temperature()
```

#### `parse_csv()`

_No docstring provided._

**Usage Example:**
```python
from pandas.1_intro.pandas_intro import parse_csv

parse_csv()
```

### Classes

_No public classes defined._

## Module `pandas/4_read_write_to_excel/read_write_with_flask/flask_with_excel.py`

- **Import Path**: `pandas.4_read_write_to_excel.read_write_with_flask.flask_with_excel`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `insert()`

_No docstring provided._

**Usage Example:**
```python
from pandas.4_read_write_to_excel.read_write_with_flask.flask_with_excel import insert

insert()
```

#### `save()`

_No docstring provided._

**Usage Example:**
```python
from pandas.4_read_write_to_excel.read_write_with_flask.flask_with_excel import save

save()
```

#### `show_tables()`

_No docstring provided._

**Usage Example:**
```python
from pandas.4_read_write_to_excel.read_write_with_flask.flask_with_excel import show_tables

show_tables()
```

### Classes

_No public classes defined._

## Module `scripts/generate_api_docs.py`

- **Import Path**: `scripts.generate_api_docs`
- **Summary**:
  Generate markdown documentation for all public Python APIs in the repository.

This script walks every ``.py`` file underneath the repository root, extracts
module metadata, top-level functions, classes, and their public members, and
writes a comprehensive markdown reference to ``docs/API_REFERENCE.md``.

Usage
-----
Run the script from the repository root:

    python3 scripts/generate_api_docs.py

Dependencies: standard library only.

- **Runtime Behavior**: This module executes statements at import time (for example, example/demo code). Consider wrapping demo code in `if __name__ == "__main__":` to avoid side effects.

### Functions

#### `build_documentation()`

_No docstring provided._

**Usage Example:**
```python
from scripts.generate_api_docs import build_documentation

build_documentation()
```

#### `iter_python_files()`

_No docstring provided._

**Usage Example:**
```python
from scripts.generate_api_docs import iter_python_files

iter_python_files()
```

#### `main()`

_No docstring provided._

**Usage Example:**
```python
from scripts.generate_api_docs import main

main()
```

#### `parse_module(path: Path)`

_No docstring provided._

**Usage Example:**
```python
from scripts.generate_api_docs import parse_module

parse_module(path="/path/to/resource")
```

#### `render_module_doc(module_doc: ModuleDoc)`

_No docstring provided._

**Usage Example:**
```python
from scripts.generate_api_docs import render_module_doc

render_module_doc(module_doc=ModuleDoc(...))
```

### Classes

#### `class ClassDoc`

_No docstring provided._

**Instantiation Example:**
```python
from scripts.generate_api_docs import ClassDoc

instance = ClassDoc()
```

_No public methods documented._

#### `class FunctionDoc`

_No docstring provided._

**Instantiation Example:**
```python
from scripts.generate_api_docs import FunctionDoc

instance = FunctionDoc()
```

_No public methods documented._

#### `class MethodDoc(FunctionDoc)`

_No docstring provided._

**Instantiation Example:**
```python
from scripts.generate_api_docs import MethodDoc

instance = MethodDoc()
```

_No public methods documented._

#### `class ModuleDoc`

_No docstring provided._

**Instantiation Example:**
```python
from scripts.generate_api_docs import ModuleDoc

instance = ModuleDoc()
```

_No public methods documented._

## Module `unittesting_pytest/custom_markers/mathlib.py`

- **Import Path**: `unittesting_pytest.custom_markers.mathlib`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

#### `calc_multiply(a, b)`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.custom_markers.mathlib import calc_multiply

calc_multiply(a="a", b="b")
```

#### `calc_total(a, b)`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.custom_markers.mathlib import calc_total

calc_total(a="a", b="b")
```

### Classes

_No public classes defined._

## Module `unittesting_pytest/custom_markers/test_mathlib.py`

- **Import Path**: `unittesting_pytest.custom_markers.test_mathlib`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

#### `test_mac_1()`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.custom_markers.test_mathlib import test_mac_1

test_mac_1()
```

#### `test_mac_2()`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.custom_markers.test_mathlib import test_mac_2

test_mac_2()
```

#### `test_windows_1()`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.custom_markers.test_mathlib import test_windows_1

test_windows_1()
```

#### `test_windows_2()`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.custom_markers.test_mathlib import test_windows_2

test_windows_2()
```

### Classes

_No public classes defined._

## Module `unittesting_pytest/fixtures/__init__.py`

- **Import Path**: `unittesting_pytest.fixtures`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `unittesting_pytest/fixtures/mydb.py`

- **Import Path**: `unittesting_pytest.fixtures.mydb`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

_No public functions defined._

### Classes

#### `class Connection`

_No docstring provided._

**Instantiation Example:**
```python
from unittesting_pytest.fixtures.mydb import Connection

instance = Connection()
```

_Methods:_

- `__init__(self)`
  - _No docstring provided._
  - Example call: `Connection()`
- `close(self)`
  - _No docstring provided._
  - Example call: `instance.close()`
- `cursor(self)`
  - _No docstring provided._
  - Example call: `instance.cursor()`

#### `class Cursor`

_No docstring provided._

**Instantiation Example:**
```python
from unittesting_pytest.fixtures.mydb import Cursor

instance = Cursor()
```

_Methods:_

- `close(self)`
  - _No docstring provided._
  - Example call: `instance.close()`
- `execute(self, query)`
  - _No docstring provided._
  - Example call: `instance.execute(query=1)`

#### `class MyDB`

_No docstring provided._

**Instantiation Example:**
```python
from unittesting_pytest.fixtures.mydb import MyDB

instance = MyDB()
```

_Methods:_

- `__init__(self)`
  - _No docstring provided._
  - Example call: `MyDB()`
- `connect(self, connection_string)`
  - _No docstring provided._
  - Example call: `instance.connect(connection_string=1)`

## Module `unittesting_pytest/fixtures/test_mydb.py`

- **Import Path**: `unittesting_pytest.fixtures.test_mydb`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

#### `cur()`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.fixtures.test_mydb import cur

cur()
```

#### `test_johns_id(cur)`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.fixtures.test_mydb import test_johns_id

test_johns_id(cur="cur")
```

#### `test_toms_id(cur)`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.fixtures.test_mydb import test_toms_id

test_toms_id(cur="cur")
```

### Classes

_No public classes defined._

## Module `unittesting_pytest/init.py`

- **Import Path**: `unittesting_pytest.init`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

_No public functions defined._

### Classes

_No public classes defined._

## Module `unittesting_pytest/parametrize/mathlib.py`

- **Import Path**: `unittesting_pytest.parametrize.mathlib`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

#### `calc_square(num)`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.parametrize.mathlib import calc_square

calc_square(num=1)
```

### Classes

_No public classes defined._

## Module `unittesting_pytest/parametrize/test_mathlib.py`

- **Import Path**: `unittesting_pytest.parametrize.test_mathlib`
- **Summary**: _No module docstring provided._

- **Runtime Behavior**: Safe to import (no side-effectful statements).

### Functions

#### `test_calc_square(test_input, expected_output)`

_No docstring provided._

**Usage Example:**
```python
from unittesting_pytest.parametrize.test_mathlib import test_calc_square

test_calc_square(test_input=1, expected_output=1)
```

### Classes

_No public classes defined._
