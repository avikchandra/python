#!/usr/bin/env python3

'''
Password Generator - Should be random and a combination of
Upper and lowercase, special symbol and numbers
'''

import string
import random

combination=string.ascii_uppercase + \
string.ascii_lowercase + \
string.punctuation + \
string.digits

letterList=list()
for num in range(8):
    letterList.append(random.choice(combination))

passString="".join(letterList)

print("Random password: {}".format(passString))
    