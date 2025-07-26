#!/usr/bin/env python3
"""
Basic Command-Line Calculator
Python Intro Assignment

Features:
- Arithmetic operations (+, -, *, /) with input validation
- Clean number formatting in results
- Comprehensive error handling
"""

def get_number(prompt: str) -> float:
    """
    Safely gets and validates a numeric input from the user.
    
    Args:
        prompt (str): The message displayed to the user
        
    Returns:
        float: Validated number
        
    Note:
        Continually prompts until valid number is entered
    """
    while True:
        try:
            # Convert input to float, handling locale-specific decimal separators
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number (e.g., 5 or 3.14)")

def get_operation() -> str:
    """
    Gets and validates the arithmetic operation from the user.
    
    Returns:
        str: Valid operator (+, -, *, /)
        
    Note:
        Only accepts defined mathematical operators
    """
    valid_ops = {'+', '-', '*', '/'}
    while True:
        # Strip whitespace and validate against allowed operators
        op = input("Enter operation (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        print(f"Error: '{op}' is invalid. Please use one of: {valid_ops}")

def calculate(num1: float, num2: float, op: str) -> float:
    """
    Performs the requested arithmetic calculation with error handling.
    
    Args:
        num1 (float): First operand
        num2 (float): Second operand
        op (str): Operator symbol
        
    Returns:
        float: Result of the calculation
        
    Raises:
        ZeroDivisionError: For division by zero attempts
    """
    match op:  
        case '+': return num1 + num2
        case '-': return num1 - num2
        case '*': return num1 * num2
        case '/': 
            # Explicit division by zero check
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return num1 / num2

def main():
    """Main program execution flow with formatted I/O."""
    print("\n=== Python Calculator ===")
    print("Enter two numbers and an operation\n" + "-"*30)
    
    # Get validated user inputs
    num1 = get_number("First number: ")
    num2 = get_number("Second number: ")
    op = get_operation()
    
    try:
        # Perform calculation and format display numbers
        result = calculate(num1, num2, op)
        display_num1 = int(num1) if num1.is_integer() else num1
        display_num2 = int(num2) if num2.is_integer() else num2
        
        # Format output with aligned columns
        print(f"\n{'Calculation':<12}: {display_num1} {op} {display_num2}")
        print(f"{'Result':<12}: {result:.2f}")
        
    except ZeroDivisionError as e:
        print(f"\nError: {e}")
    finally:
        print("\nOperation complete.")

if __name__ == "__main__":
    main()