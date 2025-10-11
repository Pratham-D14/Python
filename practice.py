import ctypes

# Understanding how variable scope works in python
try:
    x = 10
except Exception as e:
    print(e)

print(x)  # here x is getting 10 because there are only 3 scopes in python
'''
1. Functions
2. Classes
3. Modules
'''
# and try, except, if, for, while blocks don't have their scope


# ---------------------------------------------------
# Understanding the concept of closures
def outer():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

click = outer()
'''here click variable is getting increment functions along
with the variable count as increment remembers that variable'''

print(click())  # 1
print(click())  # 2
print(click())  # 3


# ---------------------------------------------------------
# understanding how decorators works in python

def add_sprinkles(func):
    def wrapper():
        print('Added sprinkles')
        func()
    return wrapper

@add_sprinkles
def get_icecream():
    print("Here's your icecream")

get_icecream()

# ----------------------------------------------------------------
# How to give arguments to a base function

def add_sprinkles(func):
    def wrapper(*args, **kwargs):  # for sending arguments to base function
        print('Added sprinkles')
        func(*args, **kwargs) # for sending arguments to base function
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):  # for sending arguments to base function
        print('Added Fudge')
        func(*args, **kwargs) # for sending arguments to base function
    return wrapper


@add_sprinkles
@add_fudge
def get_icecream(flavor):
    print(f"Here's your {flavor} icecream")

get_icecream("Vanilla")


# ----------------------------------------------------------------
# How to give arguments to a decorator function

print("-------------------")
def add_sprinkles(func):
    def wrapper(*args, **kwargs):  # for sending arguments to base function
        print('Added sprinkles')
        func(*args, **kwargs) # for sending arguments to base function
    return wrapper

def add_fudge(fudge_flavor):
    def decorator(func):
        def wrapper(*args, **kwargs):  # for sending arguments to base function
            print(f'Added {fudge_flavor} Fudge')
            func(*args, **kwargs) # for sending arguments to base function
        return wrapper
    return decorator

@add_sprinkles
@add_fudge('chocolate')
def get_icecream(flavor):
    print(f"Here's your {flavor} icecream")

get_icecream("Vanilla")


# ------------------------------------------------------------------------
# Printing the ASCII value of a char
print(ord('a'))
print(ord('d'))


# -------------------------------------------------------------------------
# Joning the string using delimitor
strings = ['ab', 'cd', 'ed']
print(''.join(strings))


# -------------------------------------------------------------------------
# Mutability and Immutability in Python


fruits = []
print(f'Older list {fruits} and id: {id(fruits)}')

fruits.append('Apple')
fruits.append('Orange')
print(f'Older list {fruits} and id: {id(fruits)}')

# Getting the value using id (memory reference):
# retrieved_object = ctypes.cast(140714729806616, ctypes.py_object).value
# print('retrieved_object: ', retrieved_object)


# --------------------------------------------------------------------------
# zip()

names = ['person1', 'person2', 'person3', 'person4', 'person5']
bills = [50, 70, 100, 80, 110]

for name, amount in zip(names, bills):
    print(f'{name} paid {amount}')


# ---------------------------------------------------------------------------
# For Loop with else condition
staff = [('person1', 16), ('person2', 17), ('person3', 15)]

# the else condition only run's if the loop didn't break (fallback logic)
for name, age in staff:
    if age >= 18:
        print(f'{name} is eligible to manage the staff')
        break
else:
    print('No one is eligible for managing the staff')


# ----------------------------------------------------------------------------
# Walrus Operators (:=) in python

available_sizes = ['small', 'medium', 'large']

if(requested_size := input('Enter your chai cup size: ')) in available_sizes:
    print(f'Serving {requested_size} chai')
else:
    print('size not available')
