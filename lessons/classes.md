## Class Syntax
```python
class ClassName:
    <statement-1>



    <statement-N>
```
## Example One: Car Class
```python
class Car:
    def __init__(self):
        self.ignition = False
        self.color = 'red'
        
    def turn_keys(self, ignition=False):
        self.ignition = ignition
```
### Car Class Breakdown
Here we defined our `Car` class. Any object we create will inherit the definitions within this class.
```python
class Car:
```

The `__init__` method serves as the *constructor* for our class, allowing us to define *attributes* and the initial *state* of each car that gets made.
```python
def __init__(self):
    self.ignition = False
    self.color = 'red'
```

Passing `self` to our method tells any car created from this class that the attributes defined are exclusive to that car.
```python
def __init__(self):
```

Each car will be turned off and have the color red upon **instantiation** (object creation), serving as the cars initial *state*.

`self.ignition` and `self.color` are the attributes each car will have.
```python
self.ignition = False
self.color = 'red'
```

Here, we have a method that changes the state of the cars ignition.
```python
def turn_keys(self, ignition=False):
    self.ignition = ignition
```

### Car Usage

Instantiate a new object from the Car class
```python
honda = Car()
```

Check out the `honda` attributes
```python
honda.__dict__
```
or
```python
honda.ignition # False
honda.color # red
```

Now turn the keys and change the car's ignition state
```python
honda.turn_keys(True)
```

Check the new ignition state
```python
honda.ignition # True
```