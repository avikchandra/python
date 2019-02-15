#!/usr/bin/env python3
# Author        : Avik Chandra
# Script        : assingment01.py
# Description   : Reverse words in sentence. 

def main():
    origString="This is a reverse order sentence"
    wordList=origString.split()
    reverseList=wordList[::-1]
    
    print("Input: {}".format(origString))
    print("Output: {}".format(" ".join(reverseList)))
    
if __name__ == '__main__':main()