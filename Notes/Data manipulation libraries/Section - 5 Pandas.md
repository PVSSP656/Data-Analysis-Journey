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

![[image.png]]

But, instead of remembering the positions of elements in an array, Pandas allows us to give “string” as index for data in an array.

Pandas series adds on a labelled index

![[image 1.png]]

But data is still numerically organized:

![[image 2.png]]

---

![[Series_part_01.pdf]]

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

  

![[image 3.png]]

  

So now, a dataframe is:

  
![[image 4.png]]


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

![[Image 5.png]]

![[Image 6.png]]

![[Image 7.png]]

![[Image 8.png]]

![[Missing Data - Pandas Operations.pdf]]

---

---

---

# GroupBy Operations - Part One

A groupby() operation in Pandas allows us to examine data on per category basis.
We need to choose a categorical column to call with groupby().
Categorical columns are not continuous. 

![[Screenshot_20260622-002106_Udemy.png]]

![[GroupBy Operations - Part One.pdf]]

---

---

---

# GroupBy Operations - Part Two - MultiIndex

![[GroupBy Operations - Part Two - MultiIndex.pdf]]

---

---

---

# Combining DataFrames - Concatenation

Often the data you need exists in two separate sources, fortunately, Pandas makes it easy to combine these together. 
The simplest combination is if both sources are already in the same format, then a concatenation through the pd.concat() call is all that is needed.

Concatenation is simply 'pasting' the two dataframes together, by columns:

DataFrame - 1:

|        | Year | Pop |
| ------ | ---- | --- |
| USA    | 1776 | 328 |
| CANADA | 1867 | 38  |
| MEXICO | 1821 | 126 |

DataFrame - 2:

|        | GDP  | Perct |
| ------ | ---- | ----- |
| USA    | 20.5 | 75%   |
| CANADA | 1.7  | NAN   |
| MEXICO | 1.22 | 25%   |

The resulting dataframe is:

|        | Year | Pop | GDP  | Perct |
| ------ | ---- | --- | ---- | ----- |
| USA    | 1776 | 328 | 20.5 | 75%   |
| CANADA | 1867 | 38  | 1.7  | NAN   |
| MEXICO | 1821 | 126 | 1.22 | 25%   |
Similarly, we can perform on rows. 

![[Combining DataFrames - Concatenation.pdf]]

---

---

---

# Combining DataFrames - Inner Merge

Often DataFrames are not in the exact sam eorder or format, meaning we cannot simply concatenate them together.
In this case, we need to merge the DataFrames.
The is analogous to a JOIN command in SQL.

The ' .merge() ' methods takes in a key argument labeled **how**.
There are 3 main ways of merging tables together using the **how** parameter:
- Inner
- Outer
- Left or Right

Let's imagine a simple example:
Our company is holding a conference for people in the movie rental industry.
We'll have people register online beforehand and the login the day of conference.

![[Image 9.jpg]]

(For the sake of simplicity, let's assume all the names are unique)

First we need to decide **on** what columns to merge together.
The **on** column should be a *primary* identifier, meaning unique per row.
The **on** column should also be present in both tables being merged.
Since we assume names are unique here, we will merge **on** = "name".

With ***how*** = ***"inner"***, the result will be the set of records that match in both boxes. 

![[Image 10.jpg]]

```python
pd.merge(registrations,logins,how='inner',on='name')
```

![[Combining DataFrames - Inner Merge.pdf]]

---

---

---

# Combining DataFrames - Left and Right Merge

### Note: Order of the tables passed in as arguments does matter here.

![[Image 9.jpg]]

### Note: Registrations is the left table, logins will be the right table.

![[Image 11.jpg]]

![[Combining DataFrames - Left and Right Merge.pdf]]

---

---

---

# Combining DataFrames - Outer Merge

Setting ***how*** = ***'outer'*** allows us to include everything present in both tables.
Or, in mathematical terms, we can say that 'outer' is 'union'.

![[Combining DataFrames - Outer Merge.pdf]]

---

---

---

# Text Methods for String Data

Often text data needs to be cleaned or manipulated for processing.
While we can always use a custom `apply()` function for these tasks, pandas comes with many built-in string method calls.

![[Text Methods for String Data.pdf]]
