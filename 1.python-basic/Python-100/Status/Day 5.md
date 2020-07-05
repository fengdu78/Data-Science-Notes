# Question 16

### **Question:**

> **_Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers._** >**_Suppose the following input is supplied to the program:_**

```
1,2,3,4,5,6,7,8,9
```

> **_Then, the output should be:_**

```
1,9,25,49,81
```

---

### Hints:

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

**Main author's Solution: Python 2**

```python
## The solution by the author is incorrect.Thus it's not included here.
```

---

**My Solution: Python 3**

```python
lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(lst))
```

---

```python
'''Solution by: shagun'''
square odd no

lst = input().split(',')     # splits in comma position and set up in list

seq = []
lst = [int(i) for i in lst]  # converts string to integer
for i in lst:
        if i%2 != 0:
                i = i*i
                seq.append(i)


seq = [str(i) for i in seq]   # All the integers are converted to string to be able to apply join operation
print(",".join(seq))
```

---

**_There were a mistake in the the test case and the solution's whice were notified and fixed with the help of @dwedigital. My warm thanks to him._**

# Question 17

### **Question:**

> **_Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:_**

```
D 100
W 200
```

- D means deposit while W means withdrawal.

> **_Suppose the following input is supplied to the program:_**

```
D 300
D 300
W 200
D 100
```

> **_Then, the output should be:_**

```
500
```

---

### Hints:

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

**Main author's Solution: Python 2**

```python
import sys
netAmount = 0
while True:
    s = raw_input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print netAmount
```

---

**My Solution: Python 3**

```python
total = 0
while True:
    s = input().split()
    if not s:            # break if the string is empty
        break
    cm,num = map(str,s)    # two inputs are distributed in cm and num in string data type

    if cm=='D':
        total+=int(num)
    if cm=='W':
        total-=int(num)

print(total)
```

---

```python
'''Solution by: leonedott'''

lst = []
while True:
  x = input()
  if len(x)==0:
    break
  lst.append(x)

balance = 0
for item in lst:
  if 'D' in item:
    balance += int(item.strip('D '))
  if 'W' in item:
    balance -= int(item.strip('W '))
print(balance)
```

---

```python
'''Solution by: AlexanderSro'''

account = 0
while True:
    action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
    if action == "d":
        deposit = input("How much would you like to deposit? ")
        account = account + int(deposit)
    elif action == "w":
        withdrow = input("How much would you like to withdrow? ")
        account = account - int(withdrow)
    elif action == "b":
        print(account)
    else:
        quit()
```

---

```python
'''Solution by: ShalomPrinz
'''
lines = []
while True:
	loopInput = input()
	if loopInput == "done":
		break
	else:
		lines.append(loopInput)

lst = list(int(i[2:]) if i[0] == 'D' else -int(i[2:]) for i in lines)
print(sum(lst))
```
---
```python
'''Solution by: popomaticbubble 
'''
transactions = []

while True:
    text = input("> ")
    if text:
    	text = text.strip('D ')
    	text = text.replace('W ', '-')
    	transactions.append(text)
    else: 
		break	
		
transactions = (int(i) for i in transactions)
balance = sum(transactions)
print(f"Balance is {balance}")
```
---
```python
'''Solution by: ChichiLovesDonkeys
'''

money = 0
while 1:
    trans = input().split(' ')
    if trans[0] == 'D':
        money = money + int(trans[1])
    elif trans[0] == 'W':
        money = money - int(trans[1])
    elif input() == '':
        break
    print(f'Your current balance is: {money}')
```
---

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%204.md "Day 4")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%206.md "Day 6")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
