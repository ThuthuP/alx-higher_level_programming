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
