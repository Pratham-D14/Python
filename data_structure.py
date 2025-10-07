# Array and it's method in python
arr = [1, 2, 3]

# Adding and Removing Element from Array
# Append methods add element at last of the existing array
arr.append(5)
print(arr)

# Pop methods remove the last value from the existing array
arr.pop()
print(arr)

# Inserting value at a particular index
arr.insert(1, 6)  # args -> (index, value)
print(arr)

# Modifying elements using index
arr[0] = 0
print(arr)


# initialize array of size n with default value of 1
n = 5
arr = [1] * n

# Sublist  (slicing an array)
arr = [1, 2, 3, 4]
print(arr[1:3])  # -> From index 1-2 as 3 is excluded
print(arr[0:4])
print(arr[0:])
print(arr[:4])


# Unpacking
a, b, c = [1, 2, 4]  # the no.of variables on LHS should be equal to RHS


# Looping through Arrays
nums = [1, 2, 3]

# using for-loop/index
for i in range(len(nums)):
    print(nums[i])

# Without index
for n in nums:
    print(n)


# with index and value using enumerate function
for i, n in enumerate(nums):
    print(i, n)


# Loop through multiple arrays simultaneously
# with unpacking
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)


# Reversing an Array
nums1.reverse()
print(nums1)


# Sorting of array
# Ascending order
nums1.sort()
print(nums1)

# Descending order
nums1.sort(reverse=True)
print(nums1)

# Sorting a string
arr = ['bob', 'alice', 'jane', 'doe']
# Sorting alphabetically
arr.sort()
print(arr)

# Custom Sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)


# List comprehension
arr = [i+i for i in range(5)]
print(arr)


# 2D List
arr = [[0] * 4 for i in range(4)]
print(arr)


# Dist Comprehension
my_dict = {i: 2*i for i in range(4)}
print(my_dict)

# Looping through DICTIONARY
print('----- Key: Values -----')
for key in my_dict:
    print(key, my_dict[key])

#
print('----- Values -----')
for val in my_dict.values():
    print(val)

#
print('----- key/value -----')
for key, val in my_dict.items():
    print(key, val)
