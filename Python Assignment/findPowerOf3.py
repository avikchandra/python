#!/usr/bin/env python3

'''
check if a given positive integer is a power of three
'''

def main():
    # User input
    num=int(input("Enter the integer number: "))

    # Check the number is divisible by 3 recursively
    while num > 0:
        if divByThree(num) == 0:
            num=num/3
            if num == 1:
                print("Power of 3.")
                break
        else:
            print("Not an power of 3.")
            break
    else:
        print("Number less than 1.")
        

def divByThree(num):
    return (num%3)

if __name__ == "__main__": main()
