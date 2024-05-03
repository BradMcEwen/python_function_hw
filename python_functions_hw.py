#====================== Question 1 ======================
import math
response = input("What would you like to do: add, subtract, multiple, or divide? ")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2 

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if response == "add":
    print(num1, "+", num2, "=", add(num1, num2))
elif response == "subtract":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif response == "multiply":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif response == "divide":
    if num2 == 0:
        print("you cant divide by 0")
    else:
        print(num1, "/", num2, "=", divide(num1, num2))


#======================== Question 2 ========================



cart = []

print("Lets go grocery shopping!")
while True:
    user_input = input("Would you like to add or remove from your cart or say 'done' to finish: ")
    if user_input == "done":
        print("Thanks for shopping here are your items: ")
        for item in cart:
            print(item)
        break
    elif user_input == "remove":
        removal = input("what item would you like to remove?")
        if removal in cart:
            cart.remove(removal)
            print(removal, " is removed from the shopping cart.")
    else:
        cart.append(user_input)
        print(f"Your cart so far {cart}")
        