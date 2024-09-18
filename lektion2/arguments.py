# 1. Positional Arguments
def greet(name, message):
    print(f"{message}, {name}!")


greet("Alice", "Hello")  # Positional arguments


# 2. Default arguments
def greet_with_default(name, message="Hi"):
    print(f"{message}, {name}!")


greet_with_default("Bob")  # Uses default message
greet_with_default("Charlie", "Hello")  # Overrides default message


# 3. Keyword arguments
def greet_keyword(name, message):
    print(f"{message}, {name}!")


greet_keyword(name="Dave", message="Hey")  # Keyword arguments
greet_keyword(message="Greetings", name="Eve")  # Order doesn't matter


# 4. How many arguments does print take? (*args), args is an arbitrary name
def my_print(*args):
    print("Printing arguments:")
    for arg in args:
        print(arg)


my_print("This", "is", "a", "test")

# The built-in print function can take arbitrary number of positional arguments
print("Hello", "World", 123, True)


# 5. **kwargs
def introduce(**kwargs):
    print("Introducing:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


introduce(name="Frank", age=30, city="New York")


# 6. * and ** operator
def add(a, b, c):
    return a + b + c


numbers = [1, 2, 3]
result = add(*numbers)  # Unpacking list into positional arguments
print("Sum:", result)


def person_info(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")


info = {"name": "Grace", "age": 28, "city": "London"}
person_info(**info)  # Unpacking dict into keyword arguments


"""
1. Positional Arguments
2. Default arguments
3. Keyword arguments
4. How many arguments does print take? (*args), args is an arbitrary name
5. **kwargs
6. * and ** operator
"""
