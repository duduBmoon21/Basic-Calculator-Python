#!/usr/bin/env python3
"""
Basic Command-Line Calculator
Python Intro Assignment
"""

def get_number(prompt: str) -> float:
    """Safely gets a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number!")

def get_operation() -> str:
    """Validates and returns the arithmetic operation."""
    valid_ops = {'+', '-', '*', '/'}
    while True:
        op = input("Enter operation (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        print(f"Error: '{op}' is invalid. Use {valid_ops}")

def calculate(num1: float, num2: float, op: str) -> float:
    """Performs the arithmetic operation with error handling."""
    match op:
        case '+': return num1 + num2
        case '-': return num1 - num2
        case '*': return num1 * num2
        case '/': 
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            return num1 / num2

def main():
    """Main execution flow with user I/O and formatted output."""
    print("\n=== Python Calculator ===")
    
    # User Input
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    op = get_operation()
    
    # Calculation and Output
    try:
        result = calculate(num1, num2, op)
        print(f"\nResult: {num1} {op} {num2} = {result:.2f}")  
    except ZeroDivisionError as e:
        print(f"\nError: {e}")
    finally:
        print("\nCalculation complete.")

if __name__ == "__main__":
    main()