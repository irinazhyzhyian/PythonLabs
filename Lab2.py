import random

print('**********TASK #1**********', end='\n\n')

n = int(input('Enter n: '))

X = [[random.randrange(0,10) for y in range(n)] for x in range(n)]

for i in range (n):
	print (X[i])

print('\n\n')

def find_max(matrix):
	m = matrix[0][0]
	for i in range (len(matrix)):
		if max(matrix[i])>m:
			m=max(matrix[i])
	return m

def sort_matrix(matrix):
	m = find_max(matrix)
	for i in range (len(matrix)):
		if m in matrix[i]:
			matrix[i].sort()
	return matrix

X = sort_matrix(X)

for i in range (n):
	print (X[i])
print('Perfect option and my personaly favorite:\n\n')

n = int(input('Enter n: '))

X = [[random.randrange(0,10) for y in range(n)] for x in range(n)]

print(X)

max_value = max(max(X))
print(max_value)
for row in X:
    if max_value in row:
        row.sort()

print(X)

print('**********TASK #2**********', end='\n\n')
import math

n = int(input('Enter n: '))
m = int(input('Enter m: '))

def count1(m):
	return m if m==1 or m==0 else count1(m-1) + count1(m-2)
def count2(n):
	return  math.sqrt(math.factorial(n) + count2(n-1)) if n!=1 else 1 

print((count1(m)/count2(n)))


