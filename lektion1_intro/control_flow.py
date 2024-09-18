# 1. Equals and not equals
a = 5
b = 10

equals = a == b  # False, because 5 is not equal to 10
not_equals = a != b  # True, because 5 is not equal to 10
print(f"Equals: {equals}, Not Equals: {not_equals}")

# 2. Booleans
is_true = True
is_false = False
print(f"Boolean values - True: {is_true}, False: {is_false}")

# 3. if statement
if a < b:
    print(f"{a} is less than {b}")

# 4. and operator
if a < b and b > 0:
    print(f"Both conditions are True: {a} is less than {b}, and {b} is positive")

# 5. or operator
if a < 0 or b > 0:
    print("One or both conditions are True")

# 6. not operator
if not is_false:
    print("The value of is_false is False, so not False is True")

# 7. else, elif
if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is less than {b}")

# Truthy and falsy https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/

"""
1. Equals and not equals
2. Booleans
3. if
4. and
5. or
6. not
7. else, elif
"""
