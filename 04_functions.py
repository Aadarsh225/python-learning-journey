def greet(name):
    print(f"Hello, {name}!")

greet("Aadarsh")

def add(a,b):
    return a + b
result = add(5,10)
print(result)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(4))
print(is_even(7))

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_fib)
        return fib_sequence

print(fibonacci(10))

def is_palindrome(str):
    return str == str[::-1]

print(is_palindrome("madam"))


    
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Aadarsh")

def calc(a,b):
    return a + b, a - b, a * b, a / b
add, sub, mul, div = calc(10,5)
print(f"Addition: {add}, Subtraction: {sub}, Multiplication: {mul}, Division: {div}")

lst = [1,2,3,4,5]
def modify_list(lst):
    lst.append(6)
    print("Inside function:", lst)

modify_list(lst)
print("Outside function:", lst)

def square(lst):
    return [x**2 for x in lst]

squared_lst = square(lst)
print("Squared List:", squared_lst)

dict = {"name":"Aadarsh", "age":20, "city":"Birgunj"}
def welcome_user(user):
    print(f"Welcome, {user['name']} from {user['city']}!")

welcome_user(dict)