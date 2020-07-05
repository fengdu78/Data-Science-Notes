# Question 60

### **Question**

> **_Write a program to compute:_**

```
f(n)=f(n-1)+100 when n>0
and f(0)=0
```

> **_with a given n input by console (n>0)._**

> **_Example:
> If the following n is given as input to the program:_**

```
5
```

> **_Then, the output of the program should be:_**

```
500
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

### Hints

> **_We can define recursive function in Python._**

---

**Main author's Solution: Python 2**

```python
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(raw_input())
print f(n)
```

---

**My Solution: Python 3**

```python
def f(n):
    if n == 0:
        return 0
    return f(n-1) + 100

n = int(input())
print(f(n))
```

---

# Question 61

### **Question**

> **_The Fibonacci Sequence is computed based on the following formula:_**

```
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
```

> **_Please write a program to compute the value of f(n) with a given n input by console._**

> **_Example:
> If the following n is given as input to the program:_**

```
7
```

> **_Then, the output of the program should be:_**

```
13
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

### Hints

> **_We can define recursive function in Python._**

---

**Main author's Solution: Python 2**

```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(raw_input())
print f(n)
```

---

**My Solution: Python 3**

```python
def f(n):
    if n < 2:
        return n
    return f(n-1) + f(n-2)

n = int(input())
print(f(n))
```

---

# Question 62

### **Question**

> **_The Fibonacci Sequence is computed based on the following formula:_**

```
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
```

> **_Please write a program to compute the value of f(n) with a given n input by console._**

> **_Example:
> If the following n is given as input to the program:_**

```
7
```

> **_Then, the output of the program should be:_**

```
0,1,1,2,3,5,8,13
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

### Hints

> **_We can define recursive function in Python.
> Use list comprehension to generate a list from an existing list.
> Use string.join() to join a list of strings._**

---

**Main author's Solution: Python 2**

```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(raw_input())
values = [str(f(x)) for x in range(0, n+1)]
print ",".join(values)

```

---

**My Solution: Python 3**

```python
def f(n):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]

n = int(input())
fibo = [0]*(n+1)  # initialize a list of size (n+1)
f(n)              # call once and it will set value to fibo[0-n]
fibo = [str(i) for i in fibo]   # converting integer data to string type
ans = ",".join(fibo)    # joining all string element of fibo with ',' character
print(ans)

```
---
```python

'''Solution by: popomaticbubble
'''
def fibo(n):
    if n < 2: return n
	return fibo(n-1)+fibo(n-2)

def print_fiblist(n):
    fib_list = [(str(fibo(i))) for i in range(0, n+1)]
    return print(",".join(fib_list))
n = int(input())
print_fiblist(n)

```

---

# Question 63

### **Question**

> **_Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console._**

> **_Example:
> If the following n is given as input to the program:_**

```
10
```

> **_Then, the output of the program should be:_**

```
0,2,4,6,8,10
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

### Hints

> **_Use yield to produce the next value in generator._**

---

**Solution:**

```python
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(raw_input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print ",".join(values)

```

**OR**

```python
# Solution by: StartZer0
n = int(input())

for i in range(0, n+1, 2):
  if i < n - 1:
    print(i, end = ',' )
  else:
    print(i)
```

---

# Question 64

### **Question**

> **_Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console._**

> **_Example:
> If the following n is given as input to the program:_**

```
100
```

> **_Then, the output of the program should be:_**

```
0,35,70
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

### Hints

> **_Use yield to produce the next value in generator._**

---

**Main author's Solution: Python 2**

```python
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(raw_input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print ",".join(values)
```

---

**My Solution: Python 3**

```python
def generate(n):
    for i in range(n+1):
        if i % 35 == 0:    # 5*7 = 35, if a number is divisible by a & b then it is also divisible by a*b
            yield i

n = int(input())
resp = [str(i) for i in generate(n)]
print(",".join(resp))

```

---

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_15.md "Day 15")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_17.md "Day 17")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
