"""Mini Project 01: Calculator"""


def calculate(a, b, operator):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else None,
    }
    if operator not in operations:
        raise ValueError(f"Unsupported operator: {operator}")
    return operations[operator](a, b)


def main():
    print("=== Simple Calculator ===")
    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+ - * /): ").strip()
        b = float(input("Enter second number: "))
        result = calculate(a, b, operator)
        if result is None:
            print("Error: cannot divide by zero.")
        else:
            print(f"Result: {result}")
    except ValueError as exc:
        print(f"Invalid input: {exc}")


if __name__ == "__main__":
    main()
