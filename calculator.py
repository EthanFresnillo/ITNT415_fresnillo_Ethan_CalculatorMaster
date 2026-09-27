def main():
    while True:
        print("\n--- Calculator Master ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting calculator...")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input! Please select a valid option.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

if __name__ == "__main__":
    main()