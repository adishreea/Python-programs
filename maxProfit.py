#Question3
#Algorithm to find max profit

#Create an array
stockPrice = list()

#Get user input for the array
i = 0
print("Enter '!' to end the array")
while True:
	x = raw_input("Enter an integer: ")
	if(x == "!"):
		break
	stockPrice.append(x)
	i += 1

#calculate the maximum profit
minPrice = maxPrice = int(stockPrice[0])
for i in range(len(stockPrice)):
	if stockPrice[i] < minPrice:
		minPrice = stockPrice[i]
	if maxPrice < stockPrice[i]:
		maxPrice = stockPrice[i]
if maxPrice == stockPrice[0]:
	profit = 0
else:
	profit = int(maxPrice) - int(minPrice)

print "Maximum Profit = %d" % profit

#Input: [7,6,4,3,1]
#Output: Maximum Profit = 0

#Input: [1,2,4,5,8]
#Output: Maximum Profit = 7

#Input: [-1,2,4,8,1]
#Output: Maximum Profit = 9
