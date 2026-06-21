---

### Section overview

- Series and DataFrames

- Conditional filtering and useful methods

- Missing data

- Group by operations

- Combining DataFrames

- Text methods and time methods

- Inputs and outputs

---


## Series - part 01

A series is a data structure in Pandas that holds an array of information along with a named index.

Clear explanation:

A NumPy array has numerical index.

![image](https://raw.githubusercontent.com/PVSSP656/Data-Analysis-Journey/main/Notes/Assets/image.png)

But, instead of remembering the positions of elements in an array, Pandas allows us to give “string” as index for data in an array.

Pandas series adds on a labelled index

![image 1](https://raw.githubusercontent.com/PVSSP656/Data-Analysis-Journey/main/Notes/Assets/image%201.png)

But data is still numerically organized:

![image 2](https://raw.githubusercontent.com/PVSSP656/Data-Analysis-Journey/main/Notes/Assets/image%202.png)

---

[Series Part 01](https://github.com/PVSSP656/Data-Analysis-Journey/blob/main/Notes/Assets/Series_part_01.pdf)


---

---

---

## Series - part 02

![[Series_02.pdf]]

---

---

---

# DataFrames - Part One - creating a DataFrame

A group of Pandas series that share the same index is called as a DataFrame

  

![image 3](https://raw.githubusercontent.com/PVSSP656/Data-Analysis-Journey/main/Notes/Assets/image%203.png)

  

So now, a dataframe is:

  
![Image 4](https://github.com/PVSSP656/Data-Analysis-Journey/raw/main/Notes/Assets/Image%204.png)


---

![[DataFrames_-_Part_One_-_Creating_a_DataFrame.pdf]]

---

---

---

## DataFrames - Part Two - Basic Properties

![[DataFrames_-_Part_02_-_Basic_Properties.pdf]]

---

---

---

## DataFrames - Part Three - Working with Columns

![[DataFrames_-_Part_Three_-_Working_with_Columns.pdf]]


----------------------

---

---

## DataFrames - Part Four - Working with Rows

![[DataFrames - Part Four - Working with Rows.pdf]]


---

---

---

# Conditional Filtering

![[Conditional Filtering.pdf]]

---
---
---

# Useful Methods - Apply on Single Column

![[Useful Methods - Apply on a Single Column.pdf]]

---

---

---

# Useful Methods - Apply on Multiple Columns

## np.vectorize()

### Purpose
Applies a Python function element-wise to every element of a NumPy array.

### Syntax

```python
np.vectorize(function)
```

### Example

```python
def square(x):
    return x**2

v_square = np.vectorize(square)

v_square(np.array([1, 2, 3]))
```

Output:

```python
array([1, 4, 9])
```

### Notes
- Makes custom functions work on NumPy arrays.
- Improves readability.
- Does **not** improve performance.
- Internally behaves similarly to looping over elements.

### Important

`np.vectorize()` is a convenience function, not true NumPy vectorization.

```python
arr**2
```

is generally faster than

```python
np.vectorize(square)(arr)
```

![[Useful Methods - Apply on Multiple Columns.pdf]]

---

---

---

# Useful Methods - Statistical Information and Sorting

![[Useful Methods - Statistical Information and Sorting.pdf]]

---

---

---

# Missing Data - Overview

Options for dealing with missing data:
- Keep it
- Remove it
- Replace it

![Image 5](https://github.com/PVSSP656/Data-Analysis-Journey/raw/main/Notes/Assets/Image%205.png)

![Image 6](https://github.com/PVSSP656/Data-Analysis-Journey/raw/main/Notes/Assets/Image%206.png)

![Image 7](https://github.com/PVSSP656/Data-Analysis-Journey/raw/main/Notes/Assets/Image%207.png)

![Image 8](https://github.com/PVSSP656/Data-Analysis-Journey/raw/main/Notes/Assets/Image%208.png)

![[Missing Data - Pandas Operations.pdf]]

---

---

---

# GroupBy Operations - Part One

A groupby() operation in Pandas allows us to examine data on per category basis.
We need to choose a categorical column to call with groupby().
Categorical columns are not continuous. 

![Screenshot](https://raw.githubusercontent.com/PVSSP656/Data-Analysis-Journey/main/Notes/Assets/Screenshot_20260622-002106_Udemy.png)

![[GroupBy Operations - Part One.pdf]]
