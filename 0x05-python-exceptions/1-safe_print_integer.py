#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Attempt to format and print the value as an integer
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        print()  # Print a newline
        return True
    except (ValueError, TypeError):
        return False

# Example usage:
value1 = 42
value2 = "not an integer"

if safe_print_integer(value1):
    print("Value1 is an integer")
else:
    print("Value1 is not an integer")

if safe_print_integer(value2):
    print("Value2 is an integer")
else:
    print("Value2 is not an integer")
