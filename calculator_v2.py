num1 = float(input("Emter first number: "))
op = input("Ebter operator: ")
num2 = float(input("Enter second number: "))

# -------------------------------------------

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

