import math
import string

print("**********TASK #1**********\n")
a = float(input('Enter a: '))
x = float(input('Enter x: '))
e = float(input("Enter e: "))

sum1, k = 0, 0

sum2 = ((a+x)**(-k))/(a**(2*k) + math.factorial(k))

while(math.fabs(sum2) > e):
	sum1+=sum2
	sum2 = ((a+x)**(-k))/(a**(2*k) + (math.factorial(k)))
	k=k+1

print('Sum = ', sum1+sum2, '\nSteps = ', k+1, end='\n\n')

print("**********TASK #2**********\n")

str = input('Enter string: ')
words = [word.strip(string.punctuation) for word in str.split()]

for word in words:
	if len(word) % 2 == 1:
		midlen = len(word)//2
		str = str.replace(word, (word[:midlen] + word[midlen+1:]), 1)

print("New string: ", str)
	