def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


def get_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Please type a number.")


def main():
    print("--- Calculator ---")
    while True:
        print("\nChoose: + - * /  (or q to quit)")
        op = input("Operation: ").strip()

        if op == "q":
            print("Bye!")
            break
        if op not in ("+", "-", "*", "/"):
            print("Wrong operation. Try again.")
            continue

        a = get_number("First number: ")
        b = get_number("Second number: ")

        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        else:
            result = divide(a, b)

        print("Result:", result)


if __name__ == "__main__":
    main()
