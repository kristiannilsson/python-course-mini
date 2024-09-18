# 2. Loop Through Numbers: Write a program that uses a loop to print numbers from 1 to 20. Include both a for loop and a while loop version.

""" for i in range(1, 21):
    print(i) """

""" i = 1
while i <= 20:
    print(i)
    i += 1
 """
# 3. List and Loops: Create a program that filters out and prints only even numbers from a given list of numbers. Starter Code:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

""" for number in numbers:
    if number % 2 == 0:
        print(number) """

# 7. Selection and String Manipulation: Write a program that takes a string input from the user and prints "This is a palindrome" if the string is a palindrome (reads the same backward as forward) and "This is not a palindrome" otherwise. Starter Code:

# user_input = input("Enter a string: ")
# [start:end:step]
""" if user_input == user_input[::-1]:
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")
 """

my_string = "qwerty"

for character in my_string[::-1]:
    print(character)
