Python 
--

### Arguments

  - *argv
    - The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.

  - **kwargs
    - The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.

### Decorator

  - Python decorator is a function that helps to add some additional functionalities to an already defined function.
  - The main purpose of any decorator is to change your class methods or attributes in such a way so that the user of your class no need to make any change in their code.

  - #### @property
    - @property decorator for a class method make the method behaving like an attribute
    - property setter can be used to set the value of this 'attribute'

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'

    @gotmarks.setter
    def gotmarks(self, sentence):
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks
```

### Underscore variable

  - The underscore prefix is meant as a hint to another programmer that a variable or method starting with a single underscore is intended for internal use.
  - Single trailing underscore
    - In summary, a single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python keywords.
  - Leading double underscores
    - Triggers name mangling when used in a class context. Enforced by the Python interpreter.
  - Leading and trailing double underscores
    - Names that have both leading and trailing double underscores are reserved for special use in the language.
  - Single underscore as a variable
    - Per convention, a single standalone underscore is sometimes used as a name to indicate that a variable is temporary or insignificant.

### Python Code For 2 And 3

#### Print

```python
from __future__ import print_function

print('Hello', file=sys.stderr)
```

#### Division

```python
from __future__ import division
```
