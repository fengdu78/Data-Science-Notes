# Question 90

### **Question**

> **_Please write a program which count and print the numbers of each character in a string input by console._**

> **_Example:
> If the following string is given as input to the program:_**

```
abcdefgabc
```

> **_Then, the output of the program should be:_**

```
a,2
c,2
b,2
e,1
d,1
g,1
f,1
```

### Hints

> **_Use dict to store key/value pairs.
> Use dict.get() method to lookup a key with default value._**

---

**Main author's Solution: Python 2**

```python
dic = {}
s=raw_input()
for s in s:
    dic[s] = dic.get(s,0)+1
print '\n'.join(['%s,%s' % (k, v) for k, v in dic.items()])
```

---

**My Solution: Python 3**

```python
import string

s = input()
for letter in string.ascii_lowercase:
    cnt = s.count(letter)
    if cnt > 0:
        print("{},{}".format(letter,cnt))
```

**OR**

```python
s = input()
for letter in range(ord('a'),ord('z')+1):    # ord() gets the ascii value of a char
    letter = chr(letter)                     # chr() gets the char of an ascii value
    cnt = s.count(letter)
    if cnt > 0:
        print("{},{}".format(letter,cnt))
```

---

# Question 91

### **Question**

> **_Please write a program which accepts a string from console and print it in reverse order._**

> **Example:
> If the following string is given as input to the program:\***

```
rise to vote sir
```

> **_Then, the output of the program should be:_**

```
ris etov ot esir
```

### Hints

> **_Use list[::-1] to iterate a list in a reverse order._**

---

**Main author's Solution: Python 2**

```python
s=raw_input()
s = s[::-1]
print s
```

---

**My Solution: Python 3**

```python
s = input()
s = ''.join(reversed(s))
print(s)
```

---

# Question 92

### **Question**

> **_Please write a program which accepts a string from console and print the characters that have even indexes._**

> **_Example:
> If the following string is given as input to the program:_**

```
H1e2l3l4o5w6o7r8l9d
```

> **_Then, the output of the program should be:_**

```
Helloworld
```

### Hints

> **_Use list[::2] to iterate a list by step 2._**

---

**Main author's Solution: Python 2**

```python
s=raw_input()
s = s[::2]
print s
```

---

**My Solution: Python 3**

```python
s = "H1e2l3l4o5w6o7r8l9d"
s = [ s[i] for i in range(len(s)) if i%2 ==0 ]
print(''.join(s))
```

**OR**

```python
s = "H1e2l3l4o5w6o7r8l9d"
ns =''
for i in range(len(s)):
    if i % 2 == 0:
        ns+=s[i]
print(ns)
```

---

# Question 93

### **Question**

> **_Please write a program which prints all permutations of [1,2,3]_**

---

### Hints

> **_Use itertools.permutations() to get permutations of list._**

---

**Solution:**

```python

import itertools
print list(itertools.permutations([1,2,3]))
```

---

# Question 94

### **Question**

> **_Write a program to solve a classic ancient Chinese puzzle:
> We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?_**

---

### Hints

> **_Use for loop to iterate all possible solutions._**

---

**Solution:**

```python
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print solutions
```

---

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_21.md "Day 21")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_23.md "Day 23")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
