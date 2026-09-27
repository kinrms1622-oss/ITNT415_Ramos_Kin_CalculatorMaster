def display_menu():
    print("===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def add(a, b):
    return round(a + b, 2)

def subtract(a, b):
    return round(a - b, 2)

def multiply(a, b):
    return round(a * b, 2)

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return round(a / b, 2)
def get_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Exiting Calculator Master. Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Try again.")
            continue

        a, b = get_numbers()

        if choice == "1":
            print(f"Result: {add(a, b)}")
        elif choice == "2":
            print(f"Result: {subtract(a, b)}")
        elif choice == "3":
            print(f"Result: {multiply(a, b)}")
        elif choice == "4":
            print(f"Result: {divide(a, b)}")

if __name__ == "__main__":
    main()