#!/usr/bin/env python3

'''
add the digits of a positive integer repeatedly
until the result has a single digit
'''

def main():
    # User input
    num=int(input("Enter the number: "))

    while 1:
        # Check if number is a single digit
        if num in range (1,10): # range is exclusive the last item
            print("The final result is: ", num)
            break
        else:
            num=addDigits(num)

def addDigits(num):
    # Convert to digits list
    numlist=list(str(num))
    add_result=0

    # Add the digits
    for item in numlist:
        add_result += int(item)
    print("Result of adding digits of {} is: {}".format(num,add_result))

    # Return the added value
    return (add_result)

if __name__ == "__main__": main()
