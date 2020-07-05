# Question 44

### **Question:**

> **_Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included)._**

---

### Hints:

> **_Use map() to generate a list. Use lambda to define anonymous functions._**

---

**Main Author's Solution: Python 2**

```python
squaredNumbers = map(lambda x: x**2, range(1,21))
print squaredNumbers
```

---

**My Solution: Python 3**

```python
def sqr(x):
    return x*x

squaredNumbers = list(map(sqr, range(1,21)))
print (squaredNumbers)
```

---

# Question 45

### **Question:**

> **_Define a class named American which has a static method called printNationality._**

---

### Hints:

> **_Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this [link](https://realpython.com/blog/python/instance-class-and-static-methods-demystified/)._**

---

**Main Author's Solution: Python 2**

```python
class American(object):
    @staticmethod
    def printNationality():
        print "America"

anAmerican = American()
anAmerican.printNationality()
American.printNationality()
```

---

**My Solution: Python 3**

```python
class American():
    @staticmethod
    def printNationality():
        print("I am American")

american = American()
american.printNationality()   # this will not run if @staticmethod does not decorates the function.
                              # Because the class has no instance.

American.printNationality()   # this will run even though the @staticmethod
                              # does not decorate printNationality()
```

---

# Question 46

### **Question:**

> **_Define a class named American and its subclass NewYorker._**

---

### Hints:

> **Use class Subclass(ParentClass) to define a subclass.\***

---

**Main Author's Solution: Python 2**

```python
class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print anAmerican
print aNewYorker
```

---

**My Solution: Python 3**

```python
class American():
    pass

class NewYorker(American):
    pass

american = American()
newyorker = NewYorker()

print(american)
print(newyorker)
```

---

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_11.md "Day 11")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_13.md "Day 13")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
