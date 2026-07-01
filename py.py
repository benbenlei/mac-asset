def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Unsupported operator: {operator}")


if __name__ == "__main__":
    x = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    y = float(input("Enter second number: "))
    print(f"Result: {calculate(x, y, op)}")
