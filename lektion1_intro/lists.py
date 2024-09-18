# 1. Create a list
my_list = [1, 2, 3, 4, 5]
print(f"List created: {my_list}")

# 2. What can be in a list? - A list can contain different data types
mixed_list = [1, "two", 3.0, True]
print(f"Mixed list: {mixed_list}")

# 3. Empty lists
empty_list = []
print(f"Empty list: {empty_list}")

# 4. .append() - Adding an element to the list
my_list.append(6)
print(f"List after append: {my_list}")

# 5. Access elements with l[0]
first_element = my_list[0]
print(f"First element in the list: {first_element}")

# 6. Modify a list
my_list[1] = 10
print(f"List after modification: {my_list}")

# 7. Remove elements with .remove()
my_list.remove(10)
print(f"List after removing 10: {my_list}")

# 8. .insert() - Insert an element at a specific position
my_list.insert(1, 20)
print(f"List after insert: {my_list}")

# 9. .pop() - Removes the last element and returns it
last_element = my_list.pop()
print(f"List after pop: {my_list}, Popped element: {last_element}")

# 10. len() - Get the length of the list
list_length = len(my_list)
print(f"Length of the list: {list_length}")

# 11. .sort() - Sort the list in ascending order
my_list.sort()
print(f"List after sort: {my_list}")

# 12. Slicing [1:3] - Get a sublist from index 1 to 2 (excluding index 3), the third argument is the step length [start:end:step_length]
sublist = my_list[1:3]
print(f"Sliced list (1:3): {sublist}")


"""
1. Create a list
2. What can be in a list?
3. Empty lists
4. .append()
5. Access elements with l[0]
6. Modify a list
7. Remove elements with .remove()
8. .insert()
9. .pop()
10. .len()
11. .sort()
12. Slicing [1:3]
"""
