### Project Euler Problem 004
##
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def pal_num():
	num_1 = list(set(range(100,1000))) # first set of integers
	num_2 = list(set(range(100,1000))) # second set of integers
	str_list = [] # start out with our list of strings blank
	for x in num_1: # for each number (x) in the list "num_1", do:
		numlst = [x*y for y in num_2] # create a new list of each number in num_1 multiplied by each number in num_2 
		for k in numlst: # for each new number in the list "numlst", do:
			number = str(k) # convert it to a string data type
			number_2 = "".join(reversed(number)) # reverse it, and assign the value to a new variable
			if number == number_2: # if the original string is equal to the reversed string, do:
				str_list.append(number_2) # add it to the list of numerical pallindrome strings
	candidates = list(map(int,str_list)) # convert our pallindrome strings back to integers in a new list
	candidates.sort() # sort our new list by value so that the largest value is at the end
	solution = candidates[-1] # our largest pallindrome is now at the end of the list
	print("The answer is: {}".format(solution)) # print our solution
pal_num() # now that our function is defined, run it