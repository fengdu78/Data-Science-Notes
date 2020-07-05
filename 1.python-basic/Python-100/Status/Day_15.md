# Question 54

### **Question**

> **_Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only._**

> **_Example:
> If the following email address is given as input to the program:_**

```
john@google.com
```

> **_Then, the output of the program should be:_**

```
google
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

### Hints

> **_Use \w to match letters._**

---

**Main author's Solution: Python 2**

```python
import re
emailAddress = raw_input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print r2.group(2)
```

---

**My Solution: Python 3**

```python
import re

email = "john@google.com elise@python.com"
pattern = "\w+@(\w+).com"
ans = re.findall(pattern,email)
print(ans)
```

---

# Question 55

### **Question**

> **_Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only._**

> **_Example:
> If the following words is given as input to the program:_**

```
2 cats and 3 dogs.
```

> **_Then, the output of the program should be:_**

```
['2', '3']
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

### Hints

> **_Use re.findall() to find all substring using regex._**

---

**Main author's Solution: Python 2**

```python
import re
s = raw_input()
print re.findall("\d+",s)
```

---

**My Solution: Python 3**

```python
import re

email = input()
pattern = "\d+"
ans = re.findall(pattern,email)
print(ans)
```

**OR**

```python
email = input().split()
ans = []
for word in email:
    if word.isdigit():     # can also use isnumeric() / isdecimal() function instead
       ans.append(word)
print(ans)
```

**OR**

```python
email = input().split()
ans = [word for word in email if word.isdigit()]  # using list comprehension method
print(ans)
```

---

# Question 56

### **Question**

> **_Print a unicode string "hello world"._**

---

### Hints

> **_Use u'strings' format to define unicode string._**

---

**Main author's Solution: Python 2**

```python
unicodeString = u"hello world!"
print unicodeString
```

---

# Question 57

### **Question**

> **_Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8._**

---

### Hints

> **_Use unicode()/encode() function to convert._**

---

**Main author's Solution: Python 2**

```python
s = raw_input()
u = unicode( s ,"utf-8")
print u
```

---

**My Solution: Python 3**

```python
s = input()
u = s.encode('utf-8')
print(u)
```

---

# Question 58

### **Question**

> **_Write a special comment to indicate a Python source code file is in unicode._**

---

### Hints

> **_Use unicode() function to convert._**

---

**Solution:**

```python
# -*- coding: utf-8 -*-
```

---

# Question 59

### **Question**

> **_Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)._**

> **_Example:
> If the following n is given as input to the program:_**

```
5
```

> **_Then, the output of the program should be:_**

```
3.55
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

### Hints

> **_Use float() to convert an integer to a float.Even if not converted it wont cause a problem because python by default understands the data type of a value_**

---

**Main author's Solution: Python 2**

```python
n=int(raw_input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print sum
```

---

**My Solution: Python 3**

```python
n = int(input())
sum = 0
for i in range(1, n+1):
    sum+= i/(i+1)
print(round(sum, 2))  # rounded to 2 decimal point
```

---

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_14.md "Day 14")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_16.md "Day 16")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
