# variable_swap.py
# Purpose: swap two user inputs
# Author: Niyubwayo Irakoze Elie
# Date: 2025-07-24

a = int(input("Enter the first variable: "))
b = int(input("Enter the second variable: "))

# temp = a
# a = b
# b = temp

# Swapping using tuple unpacking
a, b = b, a  

print(f"After swapping: a = {a}, b = {b}")
