# 1. Loop through lists
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(f"Item in list: {item}")

# 2. In range
for i in range(5):
    print(f"In range loop: {i}")

# 3. While loop (Ctrl + C for infinite loop)
counter = 0
while counter < 3:  # To prevent an infinite loop here
    print(f"While loop count: {counter}")
    counter += 1

# Infinite loop example (commented out for safety):
# while True:
#     print("Infinite loop! Press Ctrl + C to stop.")

# 4. break, continue
for number in range(1, 6):
    if number == 3:
        continue  # Skips number 3
    if number == 5:
        break  # Exits the loop when reaching 5
    print(f"Loop with continue and break: {number}")

# 5. List comprehension
squares = [x**2 for x in range(6)]  # Creates a list of squares from 0 to 5
print(f"List comprehension (squares): {squares}")

"""
1. Loop through lists
2. In range
3. While loop (infinite loops, Ctrl + C)
4. break, continue
5. List comprehension
"""
