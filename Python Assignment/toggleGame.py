#!/usr/bin/env python3

# Function to convert the decimal number to binary
# and split it into list of 1 and 0s
def convertToBinary(num):
    binNum="{0:b}".format(num)
    binLength=len(binNum)
    binNum=int(binNum)
    digits=[]
    for loop in range(0,binLength):
        digits.append(binNum%10)
        binNum=binNum//10
    digits=digits[::-1]

    return digits


# Toggling the left adjacent bit of m if it is equal to the mth bit; otherwise keep it as is.
# Toggling the right adjacent bit of m if it is equal to the mth bit; otherwise keep it as is.
# Toggling the mth bit  of the number.
def checkAndToggle(digits, mbit):
    mbitVal=digits[mbit]

    if mbit == 0:   # If mth bit is at first
        left=None
        if len(digits) == 1: right=None
        else: right=digits[mbit+1]
    elif mbit > 0 and mbit < len(digits)-1:
        left=digits[mbit-1]
        right=digits[mbit+1]
    else:           # If mth bit is at last
        left=digits[mbit-1]
        right=None

    # Toggling        
    if left != None and left == mbitVal:
        toggle(digits, mbit-1)
    
    if right != None and right == mbitVal:
        toggle(digits, mbit+1)
        
    toggle(digits,mbit)


# Function to toggle between 1 and 0
def toggle(digits,mbit):
    if digits[mbit] == 1: digits[mbit] = 0
    else: digits[mbit] = 1

# Function to convert the list of 1 and 0s to decimal number
def convertToDecimal(digits):
    decNum=0
    length=len(digits)
    for loop in range(0, length):
        decNum += digits[loop] * (2**(length-loop-1))
    
    return decNum

# Function to play the game
def playGame(digits):
    turnCount=len(digits)
    
    # Check and toggle in each turn
    for turn in range(0,turnCount):
        checkAndToggle(digits, turn)

# Main
def main():
    # Inputs
    rounds=int(input())
    numList=[]
    for r in range(0,rounds):
        numList.append(int(input()))
    
    # Rounds
    for num in numList:
        digits=convertToBinary(num)
    
        # Determine whos turn was last    
        last="X"
        other="Y"
        if len(digits)%2 == 0:
            last="Y"
            other="X"
        
        # Play the game
        playGame(digits)
        
        # Get the decimal value after the last turn
        lastNum=convertToDecimal(digits)
        
        #  Check winner
        if lastNum == num or lastNum == num-1 or lastNum == num+1: print(last)
        else: print(other)

if __name__ == '__main__': main()
    