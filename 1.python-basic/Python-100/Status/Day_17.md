# Question 65

### **Question**

> **_Please write assert statements to verify that every number in the list [2,4,6,8] is even._**

---

### Hints

> **_Use "assert expression" to make assertion._**

---

**Main author's Solution: Python 2**

```python
li = [2,4,6,8]
for i in li:
    assert i%2==0
```

---

**My Solution: Python 3**

```python
data = [2,4,5,6]
for i in data:
    assert i%2 == 0, "{} is not an even number".format(i)
```

---

# Question 66

### **Question**

> **_Please write a program which accepts basic mathematic expression from console and print the evaluation result._**

> **_Example:
> If the following n is given as input to the program:_**

```
35 + 3
```

> **_Then, the output of the program should be:_**

```
38
```

---

### Hints

> **_Use eval() to evaluate an expression._**

---

**Main author's Solution: Python 2**

```python
expression = raw_input()
print eval(expression)
```

---

**My Solution: Python 3**

```python
expression = input()
ans = eval(expression)
print(ans)
```

---

# Question 67

### **Question**

> **_Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list._**

---

### Hints

> **_Use if/elif to deal with conditions._**

---

**Main author's Solution: Python 2**

```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print bin_search(li,11)
print bin_search(li,12)

```

---

**My Solution: Python 3**

```python
#to be written

```
**Solution by ulmasovjafarbek: Python 3**
```python
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = round((low + high) / 2)
        
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
lst = [1,3,5,7,]
print(binary_search(lst, 9))   
```
---

**Solution by AasaiAlangaram: Python 3**

```python
def binary_search_Ascending(array, target):
    lower = 0
    upper = len(array)
    print('Array Length:',upper)
    while lower < upper:
        x = (lower + upper) // 2
        print('Middle Value:',x)
        value = array[x]
        if target == value:
            return x
        elif target > value:
            lower = x
        elif target < value:
            upper = x

Array = [1,5,8,10,12,13,55,66,73,78,82,85,88,99]
print('The Value Found at Index:',binary_search_Ascending(Array, 82))

```

---

**Solution by yuan1z: Python 3**

```python
idx = 0
def bs(num,num_list):
    global idx
    if (len(num_list) == 1):
        if num_list[0] == num:
            return idx
        else:
            return "No exit in the list"
    elif num in num_list[:len(num_list)//2]:
        return bs(num,num_list[:len(num_list)//2])
    else:
        idx += len(num_list)//2
    return bs(num,num_list[len(num_list)//2:])

print(bs(66,[1,5,8,10,12,13,55,66,73,78,82,85,88,99,100]))

```

---

# Question 68

### **Question**

> **_Please generate a random float where the value is between 10 and 100 using Python module._**

---

### Hints

> **_Use random.random() to generate a random float in [0,1]._**

---

**Main author's Solution: Python 2**

```python
import random
print random.random()*100
```

---

**My Solution: Python 3**

```python
import random
rand_num = random.uniform(10,100)
print(rand_num)
```

---

# Question 69

### **Question**

> **_Please generate a random float where the value is between 5 and 95 using Python module._**

---

### Hints

> **_Use random.random() to generate a random float in [0,1]._**

---

**Main author's Solution: Python 2**

```python
import random
print random.random()*100-5
```

---

**My Solution: Python 3**

```python
import random
rand_num = random.uniform(5,95)
print(rand_num)
```

---

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_16.md "Day 16")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_18.md "Day 18")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
