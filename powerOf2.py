#Exercise 3

#Get user input
x = raw_input("Enter an integer: ")

#function to check if the integer is a power of 2
def is_power_two(x):
	if(x == 0):
		return False
	else:
		while(x != 1):
			if(int(x) % 2 != 0):
				return False
			x = int(x) / 2
		return True

val = is_power_two(x)
print val

#Input: 6
#Output: False

#Input: 16
#Output: True

#Input: 0
#Output: False