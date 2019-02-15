#!/usr/bin/env python3
# Author        : Avik Chandra
# Script        : assingment02.py
# Description   : Password Generator

import string
from random import *

def main():
    combination=string.ascii_uppercase + \
    string.ascii_lowercase + \
    string.punctuation + \
    string.digits
    
    letterList=list()
    for num in range(8):
        letterList.append(choice(combination))
    
    passString="".join(letterList)
    
    print("Random password: {}".format(passString))
    
if __name__ == '__main__':main()