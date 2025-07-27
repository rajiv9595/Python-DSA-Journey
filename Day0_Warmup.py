# Day 0 - Python Warm-Up

# Q1: Take your name and print it 5 times using a loop
name = input("Enter your name: ")
for _ in range(5):
    print(name)

# Q2: Take 2 numbers and print their sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# Q3: Print the pattern:
# *
# **
# ***
# ****
for i in range(1, 5):
    print("*" * i)

# Q4: Write a function to return the square of a number
def square(n):
    return n ** 2

print("Square of 5 is:", square(5))

# Q5: Swap 2 numbers using a temporary variable
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("Before swap:", x, y)
temp = x
x = y
y = temp
print("After swap:", x, y)
