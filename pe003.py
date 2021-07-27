### Project Euler Problem 003
##
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

n = int(input("Enter the number to factor for primes: \n\n"))
for i in range(2,n+1):
	if n % i == 0:
		count = 1
		for j in range(2,(i//2 + 1)):
			if(i % j == 0):
				count = 0
				break
		if(count ==1):
			print(i)