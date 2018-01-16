#Question2
#Algorithm to find the longest common prefix string in an array of strings

#Create an array
arr = list()

#Get user input for the array
i = 0
print("Enter '!' to end the array")
while True:
	x = raw_input("Enter a string: ")
	if(x == "!"):
		break
	arr.append(x)
	i += 1

#calculate longest common prefix
def calCommonPrefix(arr):
	if not arr:
		return ""
	prefix = ""
	for i in range(len(arr[0])):
		for j in range(1, len(arr)):
			if (i >= len(arr[j]) or arr[j][i] != arr[0][i]):
				return prefix
		prefix += arr[0][i]
	return prefix

prefix = calCommonPrefix(arr)
print "Longest common prefix: %s" % prefix

#Input: ["product", "prof", "production", "produce"]
#Output: ["pro"]
