def calculator():
    while True:
        operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
        if operation == "q":
            print("Exiting the calculator.")
            break
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operation!"

        print("Result:", result)

calculator()
