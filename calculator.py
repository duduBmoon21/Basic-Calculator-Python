#!/usr/bin/env python3
"""
Basic Calculator with Validated Inputs
"""

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Not a valid number")

def get_operation() -> str:
    valid_ops = {"+", "-", "*", "/"}
    while True:
        op = input("Enter operator (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        print(f"Error: Use one of {valid_ops}")

def calculate(num1: float, num2: float, op: str) -> float:
    match op:
        case "+": return num1 + num2
        case "-": return num1 - num2
        case "*": return num1 * num2
        case "/": 
            if num2 == 0:
                raise ZeroDivisionError("Can't divide by zero")
            return num1 / num2

def main():
    print("=== Calculator ===")
    num1 = get_number("First number: ")
    num2 = get_number("Second number: ")
    op = get_operation()
    
    try:
        result = calculate(num1, num2, op)
        print(f"Result: {num1} {op} {num2} = {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()