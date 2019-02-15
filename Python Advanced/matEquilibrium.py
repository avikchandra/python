#!/usr/bin/env python3

# Define Matrix
matrix = [[2, 7, 5],[3, 1, 1],[2, 1, -7],[0, 2, 1],[1, 6, 8]]

# Count the row number and column number
rowCount=len(matrix)
colCount=len(matrix[0])

# Initialize dictionary to store row and column wise sum
rowSum={}
colSum={}

# Calculating the sum of elements row and column wise
# and store into the corresponding dictionary
def calculateSum(arr):

	# Row wise sum of elements
	index = 0
	for rowNum in arr:
		rowSum[index]=storeSum(rowNum)
		index += 1
		
	# Column wise sum of elements
	for colNum in range(colCount):
		col=[]
		for rowNum in range(rowCount):
			col.append(arr[rowNum][colNum])

		colSum[colNum]=storeSum(col)

# Comparing the total of upper and lower
# left and right  
def compareSums(row,col):
	upper, lower, right, left = 0, 0, 0, 0
	
	#print("looping for", row, col)
	# Calculate upper and lower
	if row > 0:
		for num in range(row):
			upper += rowSum[num]

	if row < rowCount-1:
		for rest in range(row+1,rowCount):
			lower += rowSum[rest]

	#print(upper,lower)

    # Check if upper and lower are same
	if upper != lower:
		return False

	# Calculate left and right
	if col > 0: 
		for num in range(col):
			left += colSum[num]

	if col < colCount-1:
		for rest in range(col+1,colCount):
			right += colSum[rest]
			
	#print(left,right)

    # Check if upper and lower are same
	if left != right:
		return False
	else:
		return True

# Main function 
def findEquilibrium(arr):
	numEqui = 0

    # Calculate sum for all the rows and columns
	calculateSum(arr)
	
	for row in range(rowCount):
		for col in range(colCount):
			if compareSums(row,col):
				numEqui += 1

	return numEqui

def storeSum(arr):
	sum = 0
	for item in arr:
		sum += item
		
	return sum

# FIND the EQUILIBRIUM points
print(findEquilibrium(matrix))