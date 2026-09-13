def add(i, n):
    return i + n

def subract(i, n):
    return i - n

def multiply(i, n):
    return i * n

def divide(i, n):
    return i / n

print("\nWelcome to your Four Functional Calculator!\n")
print("1. ADD\n2. SUBRACT\n3. MULTIPLY\n4. DIVIDE\n")

choice = input("Enter which operation you want to use:").strip().upper()

try:
    num1 = float(input("Enter your first number:"))
except ValueError:
    print("Kindly enter a valid number for calculation.")

try:
    num2 = float(input("Enter your second number:"))
except ValueError:
    print("Kindly enter a valid number for calculation.")

if choice == "ADD":
    print(f"\nThe answer to {num1} + {num2} is: {add(num1, num2)}")

elif choice == "SUBTRACT":
    print(f"\nThe answer to {num1} - {num2} is: {subract(num1, num2)}")

elif choice == "MULTIPLY":
    print(f"\nThe answer to {num1} × {num2} is: {multiply(num1, num2)}")

elif choice == "DIVIDE":
    try:
        print(f"\nThe answer to {num1} ÷ {num2} is: {divide(num1, num2)}")
    except ZeroDivisionError:
        print("Please enter a non - zero number for division.")

else:
    print("Please choose a valid operation for calculation.")