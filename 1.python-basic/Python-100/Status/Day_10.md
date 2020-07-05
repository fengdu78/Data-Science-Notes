# Question 31

### **Question:**

> **_Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys._**

---

### Hints:

```
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.
```

---

**Main Author's Solution: Python 2**

```python
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print d

printDict()
```

---

**My Solution: Python 3**

```python
def printDict():
    dict={i:i**2 for i in range(1,21)}   # Using comprehension method and
    print(dict)

printDict()
```

---

# Question 32

### **Question:**

> **_Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only._**

---

### Hints:

```
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
```

---

**Main Author's Solution: Python 2**

```python
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k in d.keys():
		print k
printDict()
```

---

**My Solution: Python 3**

```python
def printDict():
    dict = {i: i**2 for i in range(1, 21)}
    print(dict.keys())      # print keys of a dictionary

printDict()
```

---

# Question 33

### **Question:**

> **_Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included)._**

---

### Hints:

```
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.
```

---

**Main Author's Solution: Python 2**

```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li

printList()
```

---

**My Solution: Python 3**

```python
def printList():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)

printList()
```

---

# Question 34

### **Question:**

> **_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list._**

---

### Hints:

```
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list
```

---

**Main Author's Solution: Python 2**

```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[:5]

printList()
```

---

**My Solution: Python 3**

```python
def printList():
    lst = [i ** 2 for i in range(1, 21)]

    for i in range(5):
        print(lst[i])

printList()
```
---
```python
'''Solution by: popomaticbubble
'''
def squares(n):
    squares_list = [i**2 for i in range(1,n+1)]
    print(squares_list[0:5])
squares(20)
```
---

```python
'''Solution by: yuan1z'''
func = lambda :print([i**2 for i in range(1,21)][:5])
```

---

# Question 35

### **Question:**

> **_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list._**

---

### Hints:

```
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list
```

---

**Main Author's Solution: Python 2**

```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[-5:]

printList()
```

---

**My Solution: Python 3**

```python
def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(19,14,-1):
        print(lst[i])

printList()
```
---
```python
'''Solution by: popomaticbubble
'''
def squares(n):
    squares_list = [i**2 for i in range(1,n+1)]
    print(squares_list[-5:])
squares(20)
```

---

# Question 36

### **Question:**

> **_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list._**

---

```
Hints: Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list
```

---

**Main Author's Solution: Python 2**

```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[5:]

printList()
```

---

**My Solution: Python 3**

```python
def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(5,20):
        print(lst[i])

printList()
```

---

# Question 37

### **Question:**

> **_Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included)._**

---

### Hints:

```
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use tuple() to get a tuple from a list.
```

---

**Main Author's Solution: Python 2**

```python
def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print tuple(li)

printTuple()
```

---

**My Solution: Python 3**

```python
def printTupple():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))

printTupple()
```

---

```python
'''
Solution by: Seawolf159
'''
def square_of_numbers():
    return tuple(i ** 2 for i in range(1, 21))

print(square_of_numbers())
```

---

### Comment

**_Problems of this section is very much easy and all of those are of a modification of same type problem which mainly focused on using some commonly used function works with list,dictionary, tupple.In my entire solutions, I havn't tried to solve problems in efficient way.Rather I tried to solve in a different way that I can.This will help a beginner to know how simplest problems can be solved in different ways._**

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%209.md "Day 9")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_11.md "Day 11")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
