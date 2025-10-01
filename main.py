# 🚀 Enhanced Calculator Example
# Hacktoberfest 2025 Edition

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "❌ Error: Division by zero!"

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b if b != 0 else "❌ Error: Modulo by zero!"

# Map operations dynamically (scalable)
operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Power", power),
    "6": ("Modulus", modulus),
    "q": ("Quit", None)
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))   # Handles integers & decimals
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")

def main():
    print("\n🔢 Simple Calculator (Upgraded Edition) 🔢\n")
    while True:
        print("Select Operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        
        choice = input("\nEnter choice: ").strip().lower()

        if choice == "q":
            print("👋 Exiting Calculator. Have a great day!")
            break

        if choice not in operations:
            print("⚠️ Invalid choice. Please try again.\n")
            continue

        x = get_number("Enter first number: ")
        y = get_number("Enter second number: ")

        operation_name, func = operations[choice]
        result = func(x, y)
        print(f"\n✅ {operation_name} Result: {result}\n")

if __name__ == "__main__":
    main()
