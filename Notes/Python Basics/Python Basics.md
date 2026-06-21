March 31, 2026

# Variables and Types

## What is ‘ isinstance() ‘ ?

‘ isinstance() ‘ checks the type of a variable.

Syntax:

```python
isinstance(variable,type)
```

It returns:

- True — if variable is that type

- False — otherwise

## What is % ?

It is a string formatting operator (old style).

Example:

```python
print("String: %s" %mystring
```

(we saw in java)

Code:

```python
mystring = "burger"
myfloat = 5.0
myint = 6
if mystring == "hello" :
    print("String: %s" %mystring)
else:
    print(mystring.capitalize(), "is not hello")
if isinstance(myfloat,float) and myfloat == 7.0:
    print("Float number: %.2f" %myfloat)
else:
    print(myfloat, " is not equal to 7.0" )
if isinstance(myint, int) and myint == 6:
    print("True")
```

> Output:

```bash
Burger is not hello
5.0  is not equal to 7.0
True

Process finished with exit code 0
```

## How do you set a variable to equal to nothing?

```python
x = None
print(x)
```

> Output

```bash
None
```

## What is representation?

‘ repr() ‘ gives the official/internal representation of a variable

Example:

```python
x = print("Hello")
print(repr(x))
```

> Output:

```bash
Hello
'Hello'
```

### Why to use repr() ?

1. Debugging

1. See exact values

1. Show quotes/special characters

---

April 1, 2026

# Lists

Lists are very similar to arrays.

They can **contain any type of variable,** and they can contain as many variables as you wish.

### What does append() do in Python?

append() adds an element to the end of a list. Adds only one element

Example:

```python
items = ['burger','pizza']
print(items)
items.append('hello')
print(items)
```

> Output:

```bash
['burger', 'pizza']
['burger', 'pizza', 'hello']
```

⚠️ Important difference:

```python
items = ['burger','pizza']
print(items)
items.append('hello')
print(items)
items.append(['coke'])
print(items)
```

> Output:

```bash
['burger', 'pizza']
['burger', 'pizza', 'hello']
['burger', 'pizza', 'hello', ['coke']]
```

To add multiple elements at last:

Use:

```python
extend()
```

But the new elements should be in ‘ [ ] ‘.

Example:

```python
my_list = [1,2,3]
print(my_list)
my_list.append(10)
print(my_list)
my_list.extend([11,12,13,15])
print(my_list)
```

> Output:

```bash
[1, 2, 3]
[1, 2, 3, 10]
[1, 2, 3, 10, 11, 12, 13, 15]
```

Iteration can be done like this:

Example:

```python
my_list = [1,2,3]
print(my_list)
my_list.append(10)
print(my_list)
my_list.extend([11,12,13,15])
print(my_list)

# iteration
for x in my_list:
	print(x)
```

> Output:

```bash
[1, 2, 3]
[1, 2, 3, 10]
[1, 2, 3, 10, 11, 12, 13, 15]
1
2
3
10
11
12
13
15
```

But if we need to print in straight line, then:

```python
my_list = [1,2,3]
print(my_list)
my_list.append(10)
print(my_list)
my_list.extend([11,12,13,15])
print(my_list)
for x in my_list:
    print(x,end=" ")
```

> Output:

```bash
[1, 2, 3]
[1, 2, 3, 10]
[1, 2, 3, 10, 11, 12, 13, 15]
1 2 3 10 11 12 13 15 
```

🔥 Cleanest way:

```bash
print(*my_list)
```

Example:

```python
my_list = [1,2,3]
print(my_list)
my_list.append(10)
print(my_list)
my_list.extend([11,12,13,15])
print(my_list)
for x in my_list:
    print(x,end=" ")
print("")
print(*my_list)
```

> Output:

```bash
[1, 2, 3]
[1, 2, 3, 10]
[1, 2, 3, 10, 11, 12, 13, 15]
1 2 3 10 11 12 13 15 
1 2 3 10 11 12 13 15
```

## Exercise

In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator `[]`. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

```python
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
for x in range(4):
    numbers.append(x)
strings.append("hello")
strings.append("world")


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
```

> Output:

```bash
[1, 2, 3]
['hello', 'world']
The second name on the names list is Eric
```

---

April 1, 2026

# Loops

There are two types of loops:

1. ‘for’ loop

1. ‘while’ loop

## The ‘for’ loop:

```python
primes = [2,3,5,7]
for primes in primes:
	print(primes)
```

> Output:

```python
2
3
5
7
```

For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.

### 🧠 `range()` vs `xrange()`

|Feature|`range()`|`xrange()`|
|---|---|---|
|Python version|Python 3 ✅|Python 2 only ❌|
|Returns|range object (lazy)|generator-like|
|Memory|Efficient|Efficient|

General format for ‘range’:

```python
range(start, stop, step)
```

|Parameter|Meaning|
|---|---|
|start|where to begin|
|stop|where to end (NOT included ❗)|
|step|jump size|

Example:

```python
for x in range(5):
	print(x)
```

> Output:

```bash
0
1
2
3
4
```

It is same as:

```bash
range(0,5)
```

Example: range( start, stop)

```python
for x in range(3,6):
	print(x)
```

> Output:

```bash
3
4
5
```

Example: range( start, stop, step)

```python
for x in range(3,14,2):
	print(x)
```

> Output:

```bash
3
5
7
9
11
13
```

## The ‘while’ loop:

While loops repeat as long as a certain boolean condition is met.

Example:

```python
count = 0
while count < 10:
	print(count)
	count += 1
```

> Output:

```bash
0
1
2
3
4
5
6
7
8
9
```

## ‘break’ and ‘continue’ statements

‘break’ is used to exit a while loop.

‘continue’ is used to skip the current block, and return to the ‘for’ or ‘while’ statement.

Example: ‘break’

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

> Output:

```bash
0
1
2
```

When `i = 3` → loop stops immediately ❌

Example: ‘continue’

```python
for i in range(7):
    if i == 3:
        continue
    print(i)
```

> Output:

```bash
1
2
4
5
6
```

When `i = 3`:

- Skip it ❌

- Continue next iteration ✅

Example:

```python
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
```

> Output:

```python
0
1
2
3
4
1
3
5
7
9
```

### Can we use "else" clause for loops?

Unlike languages like C and C++, Python allows an **else** clause on loops. When a **for** or **while** loop finishes normally, the code in **else** runs. If the loop ends because of a **break**, the **else** block is skipped.  
Note that the **else** block still runs even if the loop uses **continue**.

Example:

```python
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
```

> Output:

```python
0
1
2
3
4
count value reached 5
1
2
3
4
```

## Exercise

Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.

```python
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break
    if number%2==0:
        print(numbers)
```

> Output:

```bash
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
[951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
```

---

# Functions

Used for dividing codes into blocks which can be called anytime.

Functions may receive arguments (variables passed from the caller to the function).

```python
def my_function_with_arguments(username,greetings):
		print("Hello %s, %s"%(username,repr(greetings)))
my_function_with_arguments('Burger','I hope you are fine')
```

> Output:

```bash
Hello Burger, I hope you are fine
```

Functions may return a value to the caller by a keyword - ‘return’.

Example:

```python
def sum(a,b):
	return a+b
print(sum(10,11))
```

> Output:

```bash
21
```

#### 🔥 `print` vs `return` in Python

✅ 1. `print()` → shows output on screen

→Used to display results

→Value is NOT stored

→ Only for seeing, no further use

✅ 2. `return` → gives value back

→ Used to send result out of function

→ Value can be stored and reused

→Very important in real programs

|Feature|`print()`|`return`|
|---|---|---|
|Purpose|Show output|Send value back|
|Reusable|❌ No|✅ Yes|
|Stores value|❌ No|✅ Yes|
|Ends function|❌ No|✅ Yes (important!)|

```bash
def test():
    print("Hello")
    return 5
    print("Bye")   # ❌ never runs
```

👉 After `return`, function **stops immediately**

## How do you call functions in Python?

Simply write the function’s name before (), placing any required arguments within the brackets.

## Exercise

In this exercise you'll use an existing function, and while adding your own to create a fully functional program.

1. Add a function named `list_benefits()` that returns the  
    following list of strings: "More organized code", "More readable code",  
    "Easier code reuse", "Allowing programmers to share and connect code  
    together"

1. Add a function named `build_sentence(info)` which receives a single argument containing a string and returns a sentence starting  
    with the given string and ending with the string " is a benefit of  
    functions!"

1. Run and see all the functions work together!

```bash
def list_benefits():
    return [
        "More organized code",
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together"
    ]
def build_sentence(info):
    return info + " is a benefit of functions!"
def name_of_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefits in list_of_benefits:
        print(build_sentence(benefits))
name_of_benefits_of_functions()
```

> Output:

```bash
More organized code is a benefit of functions!
More readable code is a benefit of functions!
Easier code reuse is a benefit of functions!
Allowing programmers to share and connect code together is a benefit of functions!
```

#### Explanation of the code:

🔹 1. Function: `list_benefits()`

```
deflist_benefits():
return [
"More organized code",
"More readable code",
"Easier code reuse",
"Allowing programmers to share and connect code together"
    ]
```

👉 What it does:

- Creates a **list of strings**

- Uses `return` → sends this list back

🧠 Output of this function:

```
[
"More organized code",
"More readable code",
"Easier code reuse",
"Allowing programmers to share and connect code together"
]
```

🔹 2. Function: `build_sentence(benefit)`

```
defbuild_sentence(benefit):
returnbenefit+" is a benefit of functions!"
```

👉 What it does:

- Takes **one string** as input (`benefit`)

- Adds extra text to it

- Returns a full sentence

🧠 Example:

```
build_sentence("More organized code")
```

👉 Output:

```
More organized code is a benefit of functions!
```

---

🔹 3. Function: `name_the_benefits_of_functions()`

```
defname_the_benefits_of_functions():
list_of_benefits=list_benefits()
```

👉 Step 1:

- Calls `list_benefits()`

- Stores result in `list_of_benefits`

```
forbenefitinlist_of_benefits:
```

👉 Step 2:

- Loop through each item in the list

- `benefit` becomes:
    
    - "More organized code"
    
    - "More readable code"
    
    - etc.
    

```
print(build_sentence(benefit))
```

👉 Step 3:

- Sends each benefit into `build_sentence()`

- Gets full sentence

- Prints it

🔹 4. Final Call

```
name_the_benefits_of_functions()
```

👉 This runs everything:

1. Gets list

1. Loops through it

1. Builds sentences

1. Prints output

---

# Questions

1. Given two numbers **a** and **b**. You need to perform basic mathematical operations on them. You will be provided an integer named as **operator.**

- If the operator equals to **1** add **a** and **b**, then print the result.

- If the operator equals to **2** subtract **b** from **a,** then print the result.

- If the operator equals to **3** multiply **a** and **b,** then print the result.

- If the operator equals to any other number**,** print "Invalid Input"(without quotes).

Note: Do not add a new line at the end.

```python
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def operations(a,b,operator):
    if operator == 1:
        print(add(a,b))
    elif operator == 2:
        print(subtract(a,b))
    elif operator == 3:
        print(multiply(a,b))
    else:
        print("Bro enter correctly!")
print("Enter 1 for addition, 2 for subtraction, and 3 for multiplication.")
operator = int(input("Enter operator:"))
a = int(input("Enter number1: "))
b = int(input("Enter number2: "))

operations(a,b,operator)
```

1. Given an integer **n**, write a program to return the factorial of **n**. The Factorial of a number is the product of all the numbers from 1 to **n**.

```python
import math
number = int(input("Enter a non-negative integer:"))
print(math.factorial(number))
```

---

# Classes & Objects

Example:

```python
class Person:
    name = "Burger"
    occupation = "Student"
    net_worth = 10
    def info(self):
        print("%s is a %s"%(self.name,self.occupation))
a = Person()
b = Person()
a.name = "Pizza"; a.occupation = "Lawyer"
b.name = "Harry"; b.occupation = "Teacher"
a.info()
b.info()

```

> Output:

```bash
Pizza is a Lawyer
Harry is a Teacher
```

## **init()**

The `__init__()` function, is a special function that is called when the class is being initiated.  
It's used for assigning values in a class.

```python
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) \#Prints '7'
```

> Output:

```bash
7
```

Explanation:

Constructor (`__init__`):

```python
def __init__(self, number):
    self.number = number
```

- `__init__` runs **automatically** when you create an object

- `self` means **this object**

- `number` is the value you pass

👉 So this line:

```python
self.number = number
```

means:

> “Store the given number inside the object”

Method:

```python
def returnNumber(self):
    return self.number
```

This function:

- takes the object (`self`)

- returns the stored number

👉 Basically:

> “Give me back the number inside the object”

Creating object

```python
var=NumberHolder(7)
```

- A new object is created

- `__init__` runs

- `self.number = 7`

👉 Now object `var` contains:

```python
number = 7
```

Calling method

```python
print(var.returnNumber())
```

- Calls the method

- Returns `7`

- Prints `7`

## Exercise

We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

```python
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()
car1.name = "Fer"; car1.kind = "convertible"; car1.color = "red"; car1.value = 60000.00
car2.name = "Jump"; car2.kind = "van"; car2.color = "blue"; car2.value = 10000.00
# test code
print(car1.description())
print(car2.description())
```

> Output:

```bash
Fer is a red convertible worth $60000.00.
Jump is a blue van worth $10000.00.
```