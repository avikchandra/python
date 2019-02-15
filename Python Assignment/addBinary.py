#!/usr/bin/env python3

'''
add two binary numbers
'''

# User input
bin_num1=input("Enter the first binary number: ")
bin_num2=input("Enter the second binary number: ")

# Convert to int and add
add_result=int(bin_num1,2) + int(bin_num2,2)
bin_result="{0:b}".format(add_result)

# Print result
print("{} + {} = {}".format(bin_num1, bin_num2, bin_result))
