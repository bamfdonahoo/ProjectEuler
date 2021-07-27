### Project Euler Problem 001
##
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def find_nums():
	len_list = set(range(1,1000)) # our range of numbers
	result1 = list(filter(lambda x: (x%3==0 or x%5==0), len_list)) # filter our range of numbers for the ones that are evenly modulo 3 and modulo 5
	print("result1 = ", result1) # print all of our numbers to check for accuracy
	print(sum(result1)) # add all of our numbers together and print the sum
find_nums() # run the function we just defined