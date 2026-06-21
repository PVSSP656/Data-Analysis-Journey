## NumPy arrays

### 1. Import NumPy

```python
import numpy as np
```

---

### 2. Create a Python List

```python
mylist = [1,2,3]
```

> Output:
> 
> ```python
> [1, 2, 3]
> ```

---

### 3. Check Type of List

```python
type(mylist)
```

> Output:
> 
> ```python
> <class 'list'>
> ```

---

### 4. Convert List to NumPy Array

```python
np.array(mylist)
```

> Output:
> 
> ```python
> array([1, 2, 3])
> ```

---

### 5. Check Type Again

```python
type(mylist)
```

> Output:
> 
> ```python
> <class 'list'>
> ```

---

### 6. Store Array in Variable

```python
myarray = np.array(mylist)
```

---

### 7. Check Type of NumPy Array

```python
type(myarray)
```

> Output:
> 
> ```python
> <class 'numpy.ndarray'>
> ```

---

---

## 2D Arrays

### 8. Create a Matrix

```python
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix
```

> Output:
> 
> ```python
> [[1, 2, 3],
>  [4, 5, 6],
>  [7, 8, 9]]
> ```

---

### 9. Convert Matrix to NumPy Array

```python
np.array(my_matrix)
```

> Output:
> 
> ```python
> array([[1, 2, 3],
>        [4, 5, 6],
>        [7, 8, 9]])
> ```

---

## Arrays of Zeros

### 10. Create 1D Array of Zeros

```python
np.zeros(5)
```

> Output:
> 
> ```python
> array([0., 0., 0., 0., 0.])
> ```

---

### 11. Create 5×5 Matrix of Zeros

```python
np.zeros((5,5))
```

> Output:
> 
> ```python
> array([[0., 0., 0., 0., 0.],
>        [0., 0., 0., 0., 0.],
>        [0., 0., 0., 0., 0.],
>        [0., 0., 0., 0., 0.],
>        [0., 0., 0., 0., 0.]])
> ```

---

## Linspace

### 12. Length of Linspace

```python
len(np.linspace(0,10,3))
```

> Output:
> 
> ```python
> 3
> ```

Generated values:

```python
array([ 0., 5., 10.])
```

---

## Random Numbers

### 13. Random Numbers Between 0 and 1

```python
np.random.rand(10)
```

> Output:
> 
> ```python
> array([...10 random values...])
> ```

---

### 14. Generate 2 Random Numbers

```python
np.random.rand(2)
```

> Output:
> 
> ```python
> array([...2 random values...])
> ```

---

### 15. Random Numbers from Standard Normal Distribution

```python
np.random.randn(4)
```

> Output:
> 
> ```python
> array([...4 random values...])
> ```

---

### 16. Random Integers

```python
np.random.randint(0,10,5)
```

> Output:
> 
> ```python
> array([...5 random integers...])
> ```

---

### 17. Random Integer Matrix

```python
np.random.randint(0,10,(2,2))
```

> Output:
> 
> ```python
> array([[..., ...],
>        [..., ...]])
> ```

---

## Random Seed

### 18. Fix Randomness

```python
np.random.seed(42)

print(np.random.rand(),
      np.random.rand(),
      np.random.rand(),
      np.random.rand())
```

> Output:
> 
> ```python
> 0.3745401188473625
> 0.9507143064099162
> 0.7319939418114051
> 0.5986584841970366
> ```

---

## Array Operations

### 19. Create Random Array

```python
arr = np.random.randint(0,10,15)
arr
```

> Output:
> 
> ```python
> array([1, 4, 0, 9, 5, 8, 0, 9, 2, 6, 3, 8, 2, 4, 2])
> ```

---

### 20. Maximum Value

```python
arr.max()
```

> Output:
> 
> ```python
> 9
> ```

---

### 21. Minimum Value

```python
arr.min()
```

> Output:
> 
> ```python
> 0
> ```

---

### 22. Index of Maximum Value

```python
arr.argmax()
```

> Output:
> 
> ```python
> 3
> ```

---

### 23. Index of Minimum Value

```python
arr.argmin()
```

> Output:
> 
> ```python
> 2
> ```

---

### 24. Data Type of Array

```python
arr.dtype
```

> Output:
> 
> ```python
> dtype('int64')
> ```

---

## String Arrays

### 25. Create List with String

```python
arr = ['burger']
```

> Output:
> 
> ```python
> ['burger']
> ```

---

### 26. Convert to NumPy Array

```python
arr = np.array(arr)
```

> Output:
> 
> ```python
> array(['burger'], dtype='<U6')
> ```

---

### 27. Check Data Type

```python
arr.dtype
```

> Output:
> 
> ```python
> dtype('<U6')
> ```

---

## Summary

|Function|Purpose|
|---|---|
|`np.array()`|Create NumPy array|
|`np.zeros()`|Array of zeros|
|`np.linspace()`|Equally spaced values|
|`np.random.rand()`|Random values between 0 and 1|
|`np.random.randn()`|Random values from normal distribution|
|`np.random.randint()`|Random integers|
|`np.random.seed()`|Fix random output|
|`arr.max()`|Maximum value|
|`arr.min()`|Minimum value|
|`arr.argmax()`|Index of maximum value|
|`arr.argmin()`|Index of minimum value|
|`arr.dtype`|Data type of array|

---

---

---

## Array indexing and selecting

```python
import numpy as np
arr = np.arange(0,5)
print(arr[3])
print(arr[1,4])
```

> Output:
> 
> ```python
> 3
> [1,2,3]
> ```

```python
print(arr[0 , 5])
print(arr[ : 5})
```

> Output:
> 
> ```python
> [0,1,2,3,4]
> [0,1,2,3,4]
> ```

### Copying of an array]

```python
arr_copy = arr.copy(arr)
print(arr_copy)

arr_copy[ : ] = 100
print(arr_copy)
```

> Output:

```python
[0,1,2,3,4]
[100,100,100,100,100]
```

### Checking greatness

```python
arr = np.arange(1,5)
print(arr)
print(arr>2)

bool_arr = arr > 2
print(bool_arr)
print(arr[bool_arr])
```

> Output:
> 
> ```python
> [1 2 3 4]
> [False False  True  True]
> [False False  True  True]
> [3 4]
> ```

---

---

---

## NumPy operations

![[NumPy_Operations.pdf]]

---

---

---

## NumPy Exercises

![[NumPy_Exercises.pdf]]