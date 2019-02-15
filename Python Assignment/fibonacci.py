#!/usr/bin/env python

# Fibonacci function
def fibonacci(num):
    firstNum=0
    secondNum=1
    result = [1]

    for loop in range(0, num-1):
        yield secondNum
        sum=firstNum + secondNum
        firstNum = secondNum
        secondNum = sum
        

fibonacci(5)


