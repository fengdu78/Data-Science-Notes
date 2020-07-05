# Question 100

### **Question**

> **_You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification._**

> **_If the following string is given as input to the program:_**
>
> ```
> 4
> bcdef
> abcdefg
> bcde
> bcdef
> ```
>
> **_Then, the output of the program should be:_**
>
> ```
> 3
> 2 1 1
> ```

### Hints

> **_Make a list to get the input order and a dictionary to count the word frequency_**

---

**My Solution: Python 3**

```python
n = int(input())

word_list = []
word_dict = {}

for i in range(n):
    word = input()
    if word not in word_dict:
        word_list.append(word)
    word_dict[word] = word_dict.get(word, 0) + 1

print(len(word_list))
for word in word_list:
    print(word_dict[word], end=' ')
```

---

# Question 101

### **Question**

> **_You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency._**

> **_If the following string is given as input to the program:_**
>
> ```
> aabbbccde
> ```
>
> **_Then, the output of the program should be:_**
>
> ```
> b 3
> a 2
> c 2
> d 1
> e 1
> ```

### Hints

> **_Count frequency with dictionary and sort by Value from dictionary Items_**

---

**My Solution: Python 3**

```python
word = input()
dct = {}
for i in word:
    dct[i] = dct.get(i,0) + 1

dct = sorted(dct.items(),key=lambda x: (-x[1],x[0]))
for i in dct:
    print(i[0],i[1])
```

---

```python
'''Solution by: yuan1z'''

X = input()
my_set = set(X)
arr = []
for item in my_set:
    arr.append([item,X.count(item)])
tmp = sorted(arr,key = lambda x: (-x[1],x[0]))

for i in tmp:
    print(i[0]+' '+str(i[1]))
```

---

```python
'''Solution by: StartZer0'''

s = list(input())

dict_count_ = {k:s.count(k) for k in s}
list_of_tuples = [(k,v) for k,v in dict_count_.items()]
list_of_tuples.sort(key = lambda x: x[1], reverse = True)

for item in list_of_tuples:
  print(item[0], item[1])
```

---

# Question 102

### **Question**

> **_Write a Python program that accepts a string and calculate the number of digits and letters._**

**Input**

> ```
> Hello321Bye360
> ```

**Output**

> ```
> Digit - 6
> Letter - 8
> ```

---

### Hints

> **_Use isdigit() and isalpha() function_**

---

**Solution:**

```python
word = input()
digit,letter = 0,0
for char in word:
    digit+=char.isdigit()
    letter+=char.isalpha()

print('Digit -',digit)
print('Letter -',letter)
```

---

# Question 103

### **Question**

> **_Given a number N.Find Sum of 1 to N Using Recursion_**

**Input**

> ```
> 5
> ```

**Output**

> ```
> 15
> ```

---

### Hints

> **_Make a recursive function to get the sum_**

---

**Solution:**

```python
def rec(n):
    if n == 0:
        return n
    return rec(n-1) + n


n = int(input())
sum = rec(n)
print(sum)
```

---

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_22.md "Day 23")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)

# To Be Continue...
