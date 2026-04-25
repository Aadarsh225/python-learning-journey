# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = num1 / num2
#     print(f"The result of {num1} divided by {num2} is: {result}")
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero!")

# try:
#     num1 = int(input("Enter the first number: "))
#     if num1 < 0:
#         print("Negative number")
# except ValueError:
#     print("Error: Please enter a valid integer!")

# try:
#     a = int(input("Enter number: "))
#     b = int(input("Enter number: "))
#     print(a / b)
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# try:
#     x = int(input("Enter number: "))
# except:
#     print("Error")
# finally:
#     print("Done")

try:
    x = int(input("Enter number: "))
except:
    print("Error")
else:
    print("Valid input:", x)