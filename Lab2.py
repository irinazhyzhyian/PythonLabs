import random

print('**********TASK #1**********', end='\n\n')

## власні функції пошуку максимуму в матриці та потрібного сортування
def find_max(matrix):
	m = matrix[0][0]
	for line in matrix:
		if m < max(line):
			m = max(line)
	return m

def sort_matrix(matrix, value):
	for line in matrix:
		if value in line:
			line.sort()
	return matrix
#-----------------------------------------------------------------


n = int(input('Enter n: '))

X = [[random.randrange(0,10) for y in range(n)] for x in range(n)]

for i in range (n):
	print (X[i])

print('\n\n')

# використання стандартної функцій пошуку максимуму 
#max_value = max(map(max, X))
#X = sort_matrix(X, max_value)

X = sort_matrix(X, find_max(X))

for i in range (n):
	print (X[i])

print('**********TASK #2**********', end='\n\n')
import math

n = int(input('Enter n: '))
m = int(input('Enter m: '))

def count1(m):
	return m if m==1 or m==0 else count1(m-1) + count1(m-2)
def count2(n):
	return  math.sqrt(math.factorial(n) + count2(n-1)) if n!=1 else 1 

print((count1(m)/count2(n)))


