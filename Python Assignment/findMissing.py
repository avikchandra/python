#!/usr/bin/env python3

'''
find a missing number from an ordered list
'''

# Declare ordered list
num_list=[34,35,37,40,42]

# Find the first and last elements
first_num=num_list[0]
last_num=num_list[len(num_list) - 1]

# Find missing numbers
missing_list=[]
for item in range(first_num,last_num+1): # range is exclusive of last item
    if item not in num_list:
        missing_list.append(item)

# Display result
print("Original list: \n",num_list)
print("Missing numbers: \n",missing_list)
