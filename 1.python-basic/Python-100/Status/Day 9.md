# Question 26

### **Question:**

> **_Define a function which can compute the sum of two numbers._**

---

### Hints:

> **_Define a function with two numbers as arguments. You can compute the sum in the function and return the value._**

---

**Main author's Solution: Python 2**

```python
def SumFunction(number1, number2):
	return number1 + number2

print SumFunction(1,2)
```

---

**My Solution: Python 3**

```python
sum = lambda n1,n2 : n1 + n2      # here lambda is use to define little function as sum
print(sum(1,2))
```

---

# Question 27

### **Question:**

> **_Define a function that can convert a integer into a string and print it in console._**

---

### Hints:

> **_Use str() to convert a number to string._**

---

**Main author's Solution: Python 2**

```python
def printValue(n):
	print str(n)

printValue(3)
```

---

**My Solution: Python 3**

```python
conv = lambda x : str(x)
n = conv(10)
print(n)
print(type(n))            # checks the type of the variable
```

---

# Question 28

### **Question:**

> **_Define a function that can receive two integer numbers in string form and compute their sum and then print it in console._**

---

### Hints:

> **_Use int() to convert a string to integer._**

---

**Main author's Solution: Python 2**

```python
def printValue(s1,s2):
	print int(s1) + int(s2)
printValue("3","4") #7
```

---

**My Solution: Python 3**

```python
sum = lambda s1,s2 : int(s1) + int(s2)
print(sum("10","45"))      # 55
```

---

# Question 29

### **Question:**

> **_Define a function that can accept two strings as input and concatenate them and then print it in console._**

---

### Hints:

> **_Use + sign to concatenate the strings._**

---

**Main author's Solution: Python 2**

```python
def printValue(s1,s2):
	print s1 + s2

printValue("3","4") #34
```

---

**My Solution: Python 3**

```python
sum = lambda s1,s2 : s1 + s2
print(sum("10","45"))        # 1045
```

---

# Question 30

### **Question:**

> **_Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line._**

---

### Hints:

> **_Use len() function to get the length of a string._**

---

**Main author's Solution: Python 2**

```python
def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1 > len2:
		print s1
	elif len2 > len1:
		print s2
	else:
		print s1
		print s2

printValue("one","three")

```

---

**My Solution: Python 3**

```python
def printVal(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
        print(s1)
        print(s2)

s1,s2=input().split()
printVal(s1,s2)
```

---

```python
'''Solution by: yuan1z'''
func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)
```

---

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%208.md "Day 9")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_10.md "Day 10")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
