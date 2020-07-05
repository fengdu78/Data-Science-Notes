# Question 10

### **Question**

> **_Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically._**

> **_Suppose the following input is supplied to the program:_**

```
hello world and practice makes perfect and hello world again
```

> **_Then, the output should be:_**

```
again and hello makes perfect practice world
```

---

### Hints:

> **_In case of input data being supplied to the question, it should be assumed to be a console input.We use set container to remove duplicated data automatically and then use sorted() to sort the data._**

---

**Main author's Solution: Python 2**

```python
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))
```

---

**My Solution: Python 3**

```python
word = input().split()

for i in word:
    if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))
```

**OR**

```python
word = input().split()
[word.remove(i) for i in word if word.count(i) > 1 ]   # removal operation with comprehension method
word.sort()
print(" ".join(word))
```

**OR**

```python
word = sorted(list(set(input().split())))              #  input string splits -> converting into set() to store unique
                                                       #  element -> converting into list to be able to apply sort
print(" ".join(word))
```

---
```python
'''Solution by: Sukanya-Mahapatra
'''
inp_string = input("Enter string: ").split()
out_string = []
for words in inp_string:
    if words not in out_string:
        out_string.append(words)
print(" ".join(sorted(out_string)))
```
---

# Question 11

### **Question**

> **_Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence._**

> **_Example:_**

```
0100,0011,1010,1001
```

> **_Then the output should be:_**

```
1010
```

> **_Notes: Assume the data is input by console._**

---

### Hints:

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

**Main author's Solution: Python 2**

```python
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p,2)
    if not intp % 5:
        value.append(p)

print ','.join(value)
```

---

**My Solution: Python 3**

```python
def check(x):                       # converts binary to integer & returns zero if divisible by 5
    total,pw = 0,1
    reversed(x)

    for i in x:
        total+=pw * (ord(i) - 48)   # ord() function returns ASCII value
        pw*=2
    return total % 5

data = input().split(",")           # inputs taken here and splited in ',' position
lst = []

for i in data:
    if check(i) == 0:               # if zero found it means divisible by zero and added to the list
        lst.append(i)

print(",".join(lst))
```

**OR**

```python
def check(x):                   # check function returns true if divisible by 5
    return int(x,2)%5 == 0      # int(x,b) takes x as string and b as base from which
                                # it will be converted to decimal
data = input().split(',')

data = list(filter(check,data)) # in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
print(",".join(data))
```

**OR**

```python
data = input().split(',')
data = list(filter(lambda i:int(i,2)%5==0,data))    # lambda is an operator that helps to write function of one line
print(",".join(data))
```

---

```python
'''Solution by: nikitaMogilev
'''
data = input().split(',')
data = [num for num in data if int(num, 2) % 5 == 0]
print(','.join(data))
```

---

# Question 12

### **Question:**

> **_Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line._**

---

### Hints:

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

**Main author's Solution: Python 2**

```python
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2 == 0) and (int(s[1])%2 == 0) and (int(s[2])%2 == 0) and (int(s[3])%2 == 0):
        values.append(s)
print ",".join(values)
```

---

**My Solution: Python 3**

```python
lst = []

for i in range(1000,3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))
```

**OR**

```python
def check(element):
    return all(ord(i)%2 == 0 for i in element)  # all returns True if all digits i is even in element

lst = [str(i) for i in range(1000,3001)]        # creates list of all given numbers with string data type
lst = list(filter(check,lst))                   # filter removes element from list if check condition fails
print(",".join(lst))
```

**OR**

```python
lst = [str(i) for i in range(1000,3001)]
lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))   # using lambda to define function inside filter function
print(",".join(lst))
```

---

```python
'''Solution by: nikitaMogilev
'''
# map() digits of each number with lambda function and check if all() of them even
# str(num) gives us opportunity to iterate through number by map() and join()
print(','.join([str(num) for num in range(1000, 3001) if all(map(lambda num: int(num) % 2 == 0, str(num)))]))
```

---

# Question 13

### **Question:**

> **_Write a program that accepts a sentence and calculate the number of letters and digits._**

> **_Suppose the following input is supplied to the program:_**

```
hello world! 123
```

> **_Then, the output should be:_**

```
LETTERS 10
DIGITS 3
```

---

### Hints:

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

**Main author's Solution: Python 2**

```python
s = raw_input()
d = {"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]
```

---

**My Solution: Python 3**

```python
word = input()
letter,digit = 0,0

for i in word:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letter+=1
    if '0'<=i and i<='9':
        digit+=1

print("LETTERS {0}\nDIGITS {1}".format(letter,digit))
```

**OR**

```python
word = input()
letter, digit = 0,0

for i in word:
    if i.isalpha(): # returns True if alphabet
        letter += 1
    elif i.isnumeric(): # returns True if numeric
        digit += 1
print(f"LETTERS {letter}\n{digits}") # two different types of formating method is shown in both solution
```
---
```python
''' Solution by: popomaticbubble
'''
import re

input_string = input('> ')
print()
counter = {"LETTERS":len(re.findall("[a-zA-Z]", input_string)), "NUMBERS":len(re.findall("[0-9]", input_string))}

print(counter)
```
---

## Conclusion

**_All the above problems are mostly string related problems. Major parts of the solution includes string releted functions and comprehension method to write down the code in more shorter form._**

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%202.md "Day 2")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%204.md "Day 4")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
