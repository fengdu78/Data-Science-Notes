# The extended part of the repository starts from this page. Previous 94 problems were collected from the repository mentioned in intro. The following problems are collected from Hackerrank and other resources from internet.All the given solutions are in python 3.

# Question 95

### **Question**

> **_Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up._**

> **_If the following string is given as input to the program:_**
>
> ```
> 5
> 2 3 6 6 5
> ```
>
> **_Then, the output of the program should be:_**
>
> ```
> 5
> ```

### Hints

> **_Make the scores unique and then find 2nd best number_**

---

**My Solution: Python 3**

```python
n = int(input())
arr = map(int, input().split())
arr = list(set(arr))
arr.sort()
print(arr[-2])
```

---

```python
'''
Solution by: mishrasunny-coder
'''
num = int(input("Enter num: "))
L = []

while True:
    L.append(num)
    num = int(input("Enter another: "))
    if num == 0:
        break

L1 = list(set(L[:]))
L2 = sorted(L1)
print(L2)

print(f'The runner up is {L2[-2]}')
```

---
```python
'''Solution by: KailashS3 
'''
num = int(input())
scores = list(map(int, input().split(' ')))
winner = max(scores)
lst = []

if len(scores) != num:
    print('length of score is greater than input given')
else:
    for score in scores:
	if winner > score:
	    lst.append(score)

runnerup = max(lst)
print(runnerup)
```
---

# Question 96

### **Question**

> **_You are given a string S and width W.
> Your task is to wrap the string into a paragraph of width._**

> **_If the following string is given as input to the program:_**
>
> ```
> ABCDEFGHIJKLIMNOQRSTUVWXYZ
> 4
> ```
>
> **_Then, the output of the program should be:_**
>
> ```
> ABCD
> EFGH
> IJKL
> IMNO
> QRST
> UVWX
> YZ
> ```

### Hints

> **_Use wrap function of textwrap module_**

---

**My Solution: Python 3**

```python
import textwrap

def wrap(string, max_width):
    string = textwrap.wrap(string,max_width)
    string = "\n".join(string)
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
```

---
```python
'''Solution by: mishrasunny-coder
'''
import textwrap

string = input()
width = int(input())

print(textwrap.fill(string,width))
```
---
```python
'''solution by  : Prashanth
'''
from textwrap import wrap
x = str(input(': '))
w = int(input())
z = list(wrap(x, w))
for i in z:
    print(i)
```

---
# Question 97

### **Question**

> **_You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)_**

> **_Different sizes of alphabet rangoli are shown below:_**
>
> ```
> #size 3
>
> ----c----
> --c-b-c--
> c-b-a-b-c
> --c-b-c--
> ----c----
>
> #size 5
>
> --------e--------
> ------e-d-e------
> ----e-d-c-d-e----
> --e-d-c-b-c-d-e--
> e-d-c-b-a-b-c-d-e
> --e-d-c-b-c-d-e--
> ----e-d-c-d-e----
> ------e-d-e------
> --------e--------
> ```

### Hints

> **_First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest._**

---

**My Solution: Python 3**

```python

import string
def print_rangoli(size):
    n = size
    alph = string.ascii_lowercase
    width = 4 * n - 3

    ans = []
    for i in range(n):
        left = '-'.join(alph[n - i - 1:n])
        mid = left[-1:0:-1] + left
        final = mid.center(width, '-')
        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2::-1]:
            ans.append(i)
    ans = '\n'.join(ans)
    print(ans)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
```

---

# Question 98

### **Question**

> **_You are given a date. Your task is to find what the day is on that date._**

**Input**

> **_A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format._**
>
> ```
> 08 05 2015
> ```

**Output**

> **_Output the correct day in capital letters._**
>
> ```
> WEDNESDAY
> ```

---

### Hints

> **_Use weekday function of calender module_**

---

**Solution:**

```python
import calendar

month, day, year = map(int, input().split())

dayId = calendar.weekday(year, month, day)
print(calendar.day_name[dayId].upper())
```

---

# Question 99

### **Question**

> **_Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both._**

**Input**

> **_The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers._**
>
> ```
> 4
> 2 4 5 9
> 4
> 2 4 11 12
> ```

**Output**

> **_Output the symmetric difference integers in ascending order, one per line._**
>
> ```
> 5
> 9
> 11
> 12
> ```

---

### Hints

> **_Use \'^\' to make symmetric difference operation._**

---

**Solution:**

```python
if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int,input().split()))

    m = int(input())
    set2 = set(map(int, input().split()))

    ans = list(set1 ^ set2)
    ans.sort()
    for i in ans:
        print(i)
```

---

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_22.md "Day 22")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_24.md "Day 24")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
