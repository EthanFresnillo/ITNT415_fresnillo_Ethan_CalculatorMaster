# Developer: Ethan Emmanuel Fresnillo
# Course: ITNT415

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    while True:
        print("\n=== Calculator Master: Ethan's Gen Z Edition ===")
        print("1. Flex (Addition)")
        print("2. Ghost (Subtraction)")
        print("3. Stack the bag (Multiplication)")
        print("4. Split the bill (Division)")
        print("5. Bounce (Exit)")
        
        choice = input("What's the move? (1-5): ")

        if choice == '5':
            print("Aight, bet. Catch you later!")
            break
        
        if choice not in ('1', '2', '3', '4'):
            print("No cap, that's invalid. Pick 1-5.")
            continue

        try:
            num1 = float(input("Drop the first number: "))
            num2 = float(input("Drop the second number: "))
        except ValueError:
            print("Bruh, that's literally not a number. Try again.")
            continue

        if choice == '1':
            print(f"Big flex! Total is: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Ghosted! Leftover is: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Bag stacked! Product is: {num1} * {num2} = {multiply(num1, num2)}")

if __name__ == "__main__":
    main()
