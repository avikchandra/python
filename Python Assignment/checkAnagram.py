#!/usr/bin/env python3

'''
check if a given string is an anagram of another given string.
'''

# Take inputs
str1=input("Enter the first string: ")
str2=input("Enter the second string: ")

# Remove spaces if any and convert to list
list1=[letter for letter in str1.replace(" ",'')]
list2=[letter for letter in str2.replace(" ",'')]

# Compare the lists
for entry in list1:
    if entry not in list2:
        print("\"{}\" and \"{}\" are not anagrams".format(str1,str2))
        break
else:
    print("\"{}\" and \"{}\" are anagrams".format(str1,str2))
