#!/usr/bin/env python3

'''
"centered" average of an array of integers
'''

# Declare the list
num_list=[-10, -4, -2, -4, -2, 0]

# Find length
list_len=len(num_list)

# Check if length is odd or even
if list_len%2 == 0:
    # For even length, find average of two centred numbers
    mean_result=(num_list[list_len//2 -1] + num_list[list_len//2]) // 2
else:
    # For odd length, find the centred number
    mean_result=num_list[list_len//2]

# Print value
print("The given list is: \n", num_list)
print("Centered mean value is: ", mean_result)
    
