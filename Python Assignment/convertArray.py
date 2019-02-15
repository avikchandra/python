#!/usr/bin/env python3

'''
convert an array to
- an ordinary list with the same items
- an array of machine values and return the bytes representation
'''

# Declare an array
num_arr=[1,2,3,4,5]

# Convert to list
num_list=list()
bnum_list=list()
for num in num_arr:
    num_list.append(num)
    bnum_list.append(bytes(num))

print("Array: ",num_arr)
print("Converted List: ",num_list)
print("Converted Bytes List: \n",bnum_list)
