Python 
--

### Dictionary

#### Dictionary keys values ordering
  - If items(), keys(), values(), iteritems(), iterkeys(), and itervalues() are called with no intervening modifications to the dictionary, the lists will directly correspond.
  - "Dict keeps insertion order" in 3.7

### Pandas DataFrame

### Multiple columns to one json column

  - Create single json column of multiple columns values

```python
df['json_col'] = df[['A', 'B']].apply(lambda x: x.to_json(), axis=1)
```

### Expand diction columns
```python
result = pd.concat([capacity_in_ml, capacity_in_ml['data'].apply(pd.Series)], axis=1)
```

### Calculate capacity based on shifts

  - shifts
    - zone_id, warehouse_location_id, shopper_id, start_hour, end_hour
  - capacity
    - zone_id, warehouse_location_id, local_hour, capacity

```python
_df1 = self._pickup_options[['zone_id', 'warehouse_location_id', 'date', 'option_start_hour']]
_df2 = self._iss_shifts[['zone_id', 'warehouse_location_id', 'date', 'start_hour', 'end_hour']]
_df = _df1.merge(_df2, on=['zone_id', 'warehouse_location_id', 'date'])
_df['capacity'] = _df[['option_start_hour', 'start_hour', 'end_hour']].apply(
            lambda x: 1 if x[0] > x[1] and x[0] <= x[2] else 0, axis=1)
```

### dataframe loc
```python
# update a column with condition
data.loc[(data.age >= 12), ['section']] = 'M'

# update multiple columns with condition
data.loc[(data.age >= 20), ['section', 'city']] = ['S','Pune'] 
```


### Replace in String

```python
"https://logistics.instacart.com/batch_plan?zone_id={}".format(zone_id)
```

### Arguments

  - *argv
    - The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.

  - **kwargs
    - The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.

### Decorator

  - Python decorator is a function that helps to add some additional functionalities to an already defined function.
  - The main purpose of any decorator is to change your class methods or attributes in such a way so that the user of your class no need to make any change in their code.

  - #### @property
    - [This link](https://www.journaldev.com/14893/python-property-decorator) explained the @property well. 
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

st.name = "Anusha"
print(st.name)
print(st.gotmarks)
print("##################")
st.gotmarks = 'Golam obtained 36'
print(st.gotmarks)
print(st.name)
print(st.marks)
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

### Object Oriented Programming

  - #### Inheritance
    - Inheritance is a concept in object-oriented programming in which a class derives (or inherits) attributes and behaviors from another class without needing to implement them again.

  - ### pass
    - In Python we use the "pass" keyword (a statement) to indicate that nothing happens—the function, class or loop is empty.

  - ### super()
    - At a high level super() gives you access to methods in a superclass from the subclass that inherits from it.
    - [This link](https://realpython.com/python-super/) explains it well with examples. 

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
```

  - ### Composition vs Inheritance
    - [This link](https://realpython.com/inheritance-composition-python/) explain **Composition vs Inheritance** well.

  - ### Overriding
    - In Python method overriding occurs simply defining in the child class a method with the same name of a method in the parent class.
    - Always use super(cls, self) for Python 2.x or super() for Python 3.x to call the original implementation of a method. This respects the resolution order in case of multiple inheritance and, for Python 3.x, protects from changes in the class hierarchy.

### Datetime and Timestamp

#### Convert numpy.datetime64 to datetime.datetime
```python
In [220]: x
Out[220]: numpy.datetime64('2012-06-17T23:00:05.453000000-0700')

In [221]: datetime.datetime.utcfromtimestamp(x.tolist()/1e9)
Out[221]: datetime.datetime(2012, 6, 18, 6, 0, 5, 45299)
```

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
