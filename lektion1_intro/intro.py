# 1. Print
print("Hello, World!")

# 2. Variables
x = 5
y = 10

# 3. Strings (f-strings, concatenation)
name = "Alice"
greeting_f_string = f"Hello, {name}!"  # f-string
greeting_concatenation = "Hello, " + name + "!"  # string concatenation

# 4. Arithmetic
sum_xy = x + y
difference_xy = x - y
product_xy = x * y
quotient_xy = y / x

# 5. Exponents
exponent_xy = x**2  # x to the power of 2

# 6. Modulo
modulo_xy = y % x  # remainder when y is divided by x

# 7. Plus-equals
x += 3  # x = x + 3

# 8. Comments
# This is a single-line comment
"""String
are
multiline
comments"""


# 9. Functions
def greet(person_name):
    return f"Hello, {person_name}!"


# Displaying results
print(greeting_f_string)
print(greeting_concatenation)
print(
    f"Sum: {sum_xy}, Difference: {difference_xy}, Product: {product_xy}, Quotient: {quotient_xy}"
)
print(f"Exponent: {exponent_xy}")
print(f"Modulo: {modulo_xy}")
print(f"Updated x after plus-equals: {x}")
print(greet("Bob"))


"""
1. Print
2. Variables
3. Stings (f-strings, +)
4. Arithmetic
5. Exponents
6. Modulo
7. Plus-equals
8. Comments
9. Functions
"""
