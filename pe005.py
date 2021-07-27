### Project Euler Problem 005
##
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# After running this for a few hours, I now know what the number is. I changed the starting "int_range" variable to be 
# a bit closer so that you can see how the program runs, but don't have to wait as long as I did. 


def smallest_div_int():
	r = 1 # we'll use this value in our "while" loop to conditionally keep things running
	int_range = int(232500000) # starting number, also referred to later as "Key"
	div = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # list of divisors
	while r == 1 and int_range < 1000000000: # lets keep it under 1 trillion combinations
		print("-------------------------------------------------------") # separate each instance so it's easier to see
		int_range+=1 # increment the key upwards by one
		mod_list = [] # list of outputs produced by dividing starts out blank
		count = 0 # start our count at zero
		print("Key = {}\n\n".format(int_range)) # print what number we're working on
		new_list = [int_range / y for y in div] # make a new list by dividing the key by each number in the list of divisors
		for k in new_list: # for each number (k) in the list above, do:
			if k % 1 == 0: # if k modulo 1 is a whole number, then:
				mod_list.append(k) # add that number to the other list
				count += 1 # increment up our count by 1
			elif k % 1 != 1: # if k modulo 1 is NOT a whole number, then:
				mod_list.clear() # clear our mod_list
				break # break out of the comparison loop
		if len(mod_list) == 20 and count == 20: # if the length of our mod_list is 20 and our count is also 20, do:
			print("The answer is {} \n\n".format(int_range)) # print the key number
			print("mod_list = ",mod_list) # print the list of alternate divisors acquired that triggered our answer so we can check for accuracy
			print("Count = ",count) # print the count that triggered our answer to check for accuracy
			r = 0 # stop our "while" loop
smallest_div_int() # now that our function is defined, call it into action