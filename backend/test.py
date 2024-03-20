#LLAMA OUTPUT




# Define a function for each operation
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# Define the main function
def calculator():
    # Get the first operand from the user
    operand1 = float(input("Enter the first operand: "))

    # Get the second operand from the user
    operand2 = float(input("Enter the second operand: "))

    # Ask the user which operation to perform
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation
    result = None
    if operation == "+":
        result = add(operand1, operand2)
    elif operation == "-":
        result = sub(operand1, operand2)
    elif operation == "*":
        result = mul(operand1, operand2)
    elif operation == "/":
        result = div(operand1, operand2)
    else:
        print("Invalid operation. Please try again.")
        return

    # Print the result
    print(f"{operand1} {operation} {operand2} = {result}")

# Call the main function
calculator()