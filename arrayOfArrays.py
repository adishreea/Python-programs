#Exercise 1

#Create an array
x = list()

#Get user input for the array
i = 0
print("Enter '!' to end the array")
while True:
	d = raw_input("Enter an integer: ")
	if(d == "!"):
		break
	x.append(int(d))
	i += 1

#function
def arrOperations(x):
	#sort array
	x.sort()
	
	arr1 = list()
	arr2 = list()
	arr3 = list()
	#create an array of arrays
	arrArrays = [arr1, arr2, arr3]

	l = len(x) / 3
	rem = len(x) % 3
	
	#to evenly distribute the elements in 3 smaller arrays
	if(rem == 0):
		for i in range(l):
				arr1.append(x[i])
		for j in range(l, 2*l):
				arr2.append(x[j])
		for k in range(2*l, 3*l):
				arr3.append(x[k])

	elif(rem == 1):
		for i in range(l+1):
				arr1.append(x[i])
		for j in range(l+1, 2*l+1):
				arr2.append(x[j])
		for k in range(2*l+1, 3*l+1):
				arr3.append(x[k])

	elif(rem == 2):
		for i in range(l+1):
				arr1.append(x[i])
		for j in range(l+1, 2*l+2):
				arr2.append(x[j])
		for k in range(2*l+2, 3*l+2):
				arr3.append(x[k])

	return arrArrays

z = arrOperations(x)
print z

#Input: [2,1,3,4,7,5,9,6,8,13,12,11,10,0,15,16,14]
#Output: [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16]]