import numpy as np

# learning how to create a simple array and perform operations
array = np.array([1, 2, 3, 4, 5])
array *= 2

# print(array)
# print(type(array))  # <class 'numpy.ndarray'> -> nd == n - dimensional

# --------------------------------
# Multidimensional Array

# array = np.array('A')  # 0 dimensional array
# array = np.array(['A', 'B', 'C'])  # 1 dimensional array

# 2 dimensional array / Matrix
# array = np.array([['A', 'B', 'C', 'D'],
#                   ['E', 'F', 'G', 'H'],
#                   ['I', 'J', 'K', 'L']])

# 3 dimensional array
array = np.array([[['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L']],
                 [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L']],
                 [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'T'], ['I', 'J', 'K', 'L']]])

print(array.ndim)  # ndim == number of dimensional
print(array.shape)  # to find out the shape of the array -> output: (row, column, depth)

# Chain Indexing
print(array[0][0][0])  # for the first element of 1st column and 1st row

# Multidimensional indexing -> Faster then chain indexing
print(array[0, 0, 1])

# multidimensional indexing concatenation
word = array[0, 1, 0] + array[0, 0, 0] + array[2, 1, 3]
print(word)


# ------------------------
# Slicing (row, column, steps)
# array[start:ending:step]
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

# row
print(array[0])
print(array[0:2])  # excluding the last index the result will be 0, 1

# column
print(array[:, 0]) # 1st column of each row
print(array[:, 0:3])  # from column 0 to 2 for each row
print(array[:, 0::2])  # adding step for columns


# --------------------------------------
# broadcasting the arrays
array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

# rule for broadcasting
# 1. The Dimension have the same size
# OR
# 2. One of the dimension has a size of 1

print(array1.shape)  # Checking the shape to check according to broadcasting rule
print(array2.shape)

print(array1 * array2)

# Printing Table using Broadcasting
array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)


# ---------------------------------------------
# Aggregate Functions -> summarize data and typically returns a single value

print(np.sum(array1))  # adding all the values of the array
print(np.mean(array1))  # average from the array
print(np.std(array1))  # standard deviation of array
print(np.var(array1))  # variance of the array
print(np.min(array1))  # minimum value from the array
print(np.max(array1))  # maximum value from the array
print(np.argmin(array1))  # finding the position of minimum value in the array
print(np.argmax(array1))  # finding the position of maximum value in the array


# Summing all the columns
array2 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

print(np.sum(array2, axis=0))  # axis=0 means all the column
print(np.sum(array2, axis=1))  # axis=1 means adding each row


# ----------------------------------------
# Filtering

age = np.array([[18, 17, 20, 25, 30, 60, 35, 15],
                [20, 63, 47, 72, 50, 48, 16, 32]])

teenager = age[age < 18]
adults = age[(age >= 18) & (age < 60)]
seniors = age[age >= 60]

# What if I want a filtered array in same format as the original
adults = np.where((age >= 18) & (age < 60), age, 0)  # args -> (condition, array, replace_value)
print(adults)


# ----------------------------------------
# random numbers
rng = np.random.default_rng()
# rng = np.random.default_rng(seed=1)  # (seed=1): for producing same response again

print(rng.integers(1, 10, size=3))  # second number is excluded: range = (1 - 9)
print(rng.integers(1, 50, size=(3, 4)))  # in 2d Array

# np.random.seed(seed=1)  # For remembering the value (producing same)

# Floating point number
print(np.random.uniform())  # args -> (low, high, size)

# Generating random values from array
fruits = np.array(['apple', 'orange', 'banana', 'coconut', 'pineapple'])
fruit = rng.choice(fruits)  # args -> (array, size)
print(fruit)
