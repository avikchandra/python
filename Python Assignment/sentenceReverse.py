#!/usr/bin/env python3

'''
Reverse words in sentence
'''

# Take input from user
orig_string=input("Enter the string: ")
str_list=orig_string.split()

# Option1
str_list.reverse()
print(' '.join(str_list))

# Option2
#reversed_list=list(str_list[::-1])
#print(' '.join(reversed_list))
