# NumPy
                                    # │
                                    # ├── Array
                                    # │   ├── 1D
                                    # │   └── 2D / Matrix
                                    # │
                                    # ├── Attributes
                                    # │   ├── shape
                                    # │   ├── ndim
                                    # │   ├── size
                                    # │   └── dtype
                                    # │
                                    # ├── Access
                                    # │   ├── Indexing
                                    # │   └── Slicing
                                    # │
                                    # ├── Creation
                                    # │   ├── zeros()
                                    # │   ├── ones()
                                    # │   ├── full()
                                    # │   ├── eye()
                                    # │   ├── arange()
                                    # │   └── linspace()
                                    # │
                                    # ├── Manipulation
                                    # │   ├── reshape()
                                    # │   ├── concatenate()
                                    # │   ├── vstack()
                                    # │   ├── hstack()
                                    # │   ├── transpose
                                    # │   └── flatten()
                                    # │
                                    # ├── Calculations
                                    # │   ├── + - * /
                                    # │   ├── sum()
                                    # │   ├── mean()
                                    # │   ├── median()
                                    # │   ├── min()
                                    # │   ├── max()
                                    # │   └── std()
                                    # │
                                    # ├── Filtering
                                    # │   ├── Boolean filtering
                                    # │   └── where()
                                    # │
                                    # ├── Other Important
                                    # │   ├── sort()
                                    # │   ├── random
                                    # │   ├── unique()
                                    # │   ├── NaN
                                    # │   └── copy()
                                    # │
                                    # └── Linear Algebra
                                    #     ├── Matrix multiplication
                                    #     └── Transpose


import numpy as np


# ============================================================
# 1. NUMPY ARRAY
# ============================================================
# NumPy array numerical data store karne ke liye hoti hai.

arr = np.array([10, 20, 30, 40, 50])

print("\n--- 1. NumPy Array ---")
print(arr)

# OUTPUT:
# [10 20 30 40 50]


# ============================================================
# 2. 2D ARRAY / MATRIX
# ============================================================
# 2D array = rows aur columns

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n--- 2. 2D Array ---")
print(matrix)

# OUTPUT:
# [[1 2 3]
#  [4 5 6]]


# ============================================================
# 3. ARRAY ATTRIBUTES
# ============================================================
# shape = rows, columns
# ndim  = dimensions
# size  = total elements
# dtype = data type

print("\n--- 3. Attributes ---")
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data Type:", matrix.dtype)

# OUTPUT:
# Shape: (2, 3)
# Dimensions: 2
# Size: 6
# Data Type: int64


# ============================================================
# 4. INDEXING
# ============================================================
# Specific element access karna

print("\n--- 4. Indexing ---")
print("First:", arr[0])
print("Third:", arr[2])
print("Last:", arr[-1])

# OUTPUT:
# First: 10
# Third: 30
# Last: 50


# ============================================================
# 5. SLICING
# ============================================================
# Array ka portion nikalna

print("\n--- 5. Slicing ---")
print(arr[1:4])
print(matrix[0, 1:3])

# OUTPUT:
# [20 30 40]
# [2 3]


# ============================================================
# 6. ZEROS
# ============================================================
# zeros() 0 se filled array banata hai

print("\n--- 6. np.zeros() ---")
print(np.zeros(4))

# OUTPUT:
# [0. 0. 0. 0.]


# ============================================================
# 7. ONES
# ============================================================
# ones() 1 se filled array banata hai

print("\n--- 7. np.ones() ---")
print(np.ones(4))

# OUTPUT:
# [1. 1. 1. 1.]


# ============================================================
# 8. FULL
# ============================================================
# full() given value se array fill karta hai

print("\n--- 8. np.full() ---")
print(np.full(4, 7))

# OUTPUT:
# [7 7 7 7]


# ============================================================
# 9. EYE
# ============================================================
# eye() identity matrix banata hai

print("\n--- 9. np.eye() ---")
print(np.eye(3))

# OUTPUT:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


# ============================================================
# 10. ARANGE
# ============================================================
# range ki tarah numbers generate karta hai

print("\n--- 10. np.arange() ---")
print(np.arange(1, 6))

# OUTPUT:
# [1 2 3 4 5]


# ============================================================
# 11. LINSPACE
# ============================================================
# Range mein equally spaced numbers deta hai

print("\n--- 11. np.linspace() ---")
print(np.linspace(0, 10, 5))

# OUTPUT:
# [ 0.   2.5  5.   7.5 10. ]


# ============================================================
# 12. RESHAPE
# ============================================================
# Array ka shape change karta hai

numbers = np.arange(1, 7)

print("\n--- 12. Reshape ---")
print(numbers)
print(numbers.reshape(2, 3))

# OUTPUT:
# [1 2 3 4 5 6]
# [[1 2 3]
#  [4 5 6]]


# ============================================================
# 13. CONCATENATE
# ============================================================
# Arrays ko combine karta hai

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\n--- 13. Concatenate ---")
print(np.concatenate((a, b)))

# OUTPUT:
# [1 2 3 4 5 6]


# ============================================================
# 14. VSTACK
# ============================================================
# Arrays ko vertically combine karta hai

x = np.array([[1, 2],
              [3, 4]])

y = np.array([[5, 6],
              [7, 8]])

print("\n--- 14. Vertical Stack ---")
print(np.vstack((x, y)))

# OUTPUT:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]


# ============================================================
# 15. HSTACK
# ============================================================
# Arrays ko horizontally combine karta hai

print("\n--- 15. Horizontal Stack ---")
print(np.hstack((x, y)))

# OUTPUT:
# [[1 2 5 6]
#  [3 4 7 8]]


# ============================================================
# 16. ARRAY MATHEMATICAL OPERATIONS
# ============================================================
# Arrays par direct calculations

p = np.array([10, 20, 30])
q = np.array([1, 2, 3])

print("\n--- 16. Mathematical Operations ---")
print("Addition:", p + q)
print("Subtraction:", p - q)
print("Multiplication:", p * q)
print("Division:", p / q)
print("Power:", p ** 2)

# OUTPUT:
# Addition: [11 22 33]
# Subtraction: [ 9 18 27]
# Multiplication: [10 40 90]
# Division: [10. 10. 10.]
# Power: [100 400 900]


# ============================================================
# 17. NUMPY MATHEMATICAL FUNCTIONS
# ============================================================
# sqrt, square, abs etc.

print("\n--- 17. Mathematical Functions ---")

print("Square Root:", np.sqrt([4, 9, 16]))
print("Square:", np.square([2, 3, 4]))
print("Absolute:", np.abs([-10, 20, -30]))

# OUTPUT:
# Square Root: [2. 3. 4.]
# Square: [ 4  9 16]
# Absolute: [10 20 30]


# ============================================================
# 18. SUM
# ============================================================
# Total calculate karta hai

data = np.array([10, 20, 30, 40, 50])

print("\n--- 18. Sum ---")
print(np.sum(data))

# OUTPUT:
# 150


# ============================================================
# 19. MEAN
# ============================================================
# Average calculate karta hai

print("\n--- 19. Mean ---")
print(np.mean(data))

# OUTPUT:
# 30.0


# ============================================================
# 20. MEDIAN
# ============================================================
# Middle value

print("\n--- 20. Median ---")
print(np.median(data))

# OUTPUT:
# 30.0


# ============================================================
# 21. MINIMUM / MAXIMUM
# ============================================================

print("\n--- 21. Min / Max ---")
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))

# OUTPUT:
# Minimum: 10
# Maximum: 50


# ============================================================
# 22. STANDARD DEVIATION
# ============================================================
# Data kitna spread hai

print("\n--- 22. Standard Deviation ---")
print(np.std(data))

# OUTPUT:
# 14.142135623730951


# ============================================================
# 23. AXIS
# ============================================================
# axis=0 → columns ke across
# axis=1 → rows ke across

data2 = np.array([
    [1, 2, 3],                    #    ROW* ->  1+2+3=6             COL* 1+4=5, 2+5=7, 3+6=9
    [4, 5, 6]                     #    R0W* ->  4+5+6=15   [6 15]          col -> [ 5 7 9]       
])

print("\n--- 23. Axis ---")
print("axis=0:", np.sum(data2, axis=0))
print("axis=1:", np.sum(data2, axis=1))

# OUTPUT:
# axis=0: [5 7 9]
# axis=1: [ 6 15]


# ============================================================
# 24. BOOLEAN FILTERING
# ============================================================
# Condition laga kar values filter karna

marks = np.array([45, 78, 90, 32, 65])

print("\n--- 24. Boolean Filtering ---")
print(marks > 50)
print(marks[marks > 50])

# OUTPUT:
# [False  True  True False  True]
# [78 90 65]


# ============================================================
# 25. WHERE
# ============================================================
# Condition ke according value choose karta hai

result = np.where(marks >= 50, "Pass", "Fail")

print("\n--- 25. np.where() ---")
print(result)

# OUTPUT:
# ['Fail' 'Pass' 'Pass' 'Fail' 'Pass']


# ============================================================
# 26. SORT
# ============================================================
# Values ko ascending order mein arrange karta hai

unsorted = np.array([50, 10, 40, 20, 30])

print("\n--- 26. Sorting ---")
print(np.sort(unsorted))

# OUTPUT:
# [10 20 30 40 50]


# ============================================================
# 27. RANDOM
# ============================================================
# Random numbers generate karta hai

np.random.seed(1)

print("\n--- 27. Random ---")
print(np.random.randint(1, 10, 5))

# OUTPUT:
# [6 9 6 1 1]


# ============================================================
# 28. TRANSPOSE
# ============================================================
# Rows ko columns aur columns ko rows banata hai

print("\n--- 28. Transpose ---")
print(matrix)
print(matrix.T)

# OUTPUT:
# [[1 2 3]
#  [4 5 6]]
#
# [[1 4]
#  [2 5]
#  [3 6]]


# ============================================================
# 29. MATRIX MULTIPLICATION
# ============================================================
# @ operator matrix multiplication ke liye

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("\n--- 29. Matrix Multiplication ---")
print(A @ B)

# OUTPUT:
# [[19 22]
#  [43 50]]


# ============================================================
# 30. NaN / MISSING VALUES
# ============================================================
# NaN = Not a Number
# Missing numerical data ko represent kar sakta hai

values = np.array([10, 20, np.nan, 40])

print("\n--- 30. NaN ---")
print("Array:", values)
print("Is NaN:", np.isnan(values))
print("Mean ignoring NaN:", np.nanmean(values))

# OUTPUT:
# Array: [10. 20. nan 40.]
# Is NaN: [False False  True False]
# Mean ignoring NaN: 23.333333333333332


# ============================================================
# 31. UNIQUE
# ============================================================
# Duplicate values remove karta hai

values2 = np.array([10, 20, 20, 30, 30, 30, 40])

print("\n--- 31. Unique ---")
print(np.unique(values2))

# OUTPUT:
# [10 20 30 40]


# ============================================================
# 32. FLATTEN
# ============================================================
# Multi-dimensional array ko 1D bana deta hai

print("\n--- 32. Flatten ---")
print(matrix.flatten())

# OUTPUT:
# [1 2 3 4 5 6]


# ============================================================
# 33. COPY
# ============================================================
# Independent copy banata hai

original = np.array([1, 2, 3])
copied = original.copy()

copied[0] = 100

print("\n--- 33. Copy ---")
print("Original:", original)
print("Copied:", copied)

# OUTPUT:
# Original: [1 2 3]
# Copied: [100   2   3]
