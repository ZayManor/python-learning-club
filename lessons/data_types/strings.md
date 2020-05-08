# Python Strings

## Syntax
**Single Quotes**
```python
'Hello, World!'
```

**Double Quotes**
```python
"Hello, World!"
```

## Accessing Elements of a String
Python strings are iterable objects. This means we can access the characters that make up the string.
```python
a = "apples"
a[0] # output: a
a[5] # output: s
```

## String Conversions
You can convert other data types to a string
```python
str(5) # output: "5"
str(5.0) # output: "5.0"
```

## String Class
Strings contain their own set of methods that enable you to alter the contents of that string.
```python
a = "apples"
a.upper()           # output: "APPLES"
a.replace('a', 'B') # output: "BPPLES"
a.split()           # output: ["apples"]
```

[Click To learn more about string class methods](https://www.w3schools.com/python/python_ref_string.asp)