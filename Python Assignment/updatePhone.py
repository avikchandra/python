#!/usr/bin/env python3

'''
read all contact numbers and update them from 7 digit to
8 digit numbers by adding 9 in front to existing numbers
'''

# Phone numbers
phone_list=['8764532', '8273864', '7864578']
updated_list=[]

# Get each number
for num in phone_list:
    # Make an array with numbers
    digit_list=[digit for digit in num]

    # Insert 9
    digit_list.insert(0,'9')

    # Convert to string 
    updated_list.append("".join(digit_list))

print("Original numbers: \n",phone_list)
print("Updated numbers: \n",updated_list)
