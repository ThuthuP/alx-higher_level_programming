#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # Handle the case when x is greater than the length of my_list
    finally:
        print()  # Print a newline to end the line of printed elements
    return count
