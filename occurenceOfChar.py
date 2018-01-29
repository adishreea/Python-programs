#Exercise 2

sentence = raw_input("Enter a sentence: ")
character = raw_input("Enter a character to find its frequency: ")

#function
def find_frequency(ch, s):
	count = 0
	for i in range(len(s)):
		if(ch == s[i]):
			count += 1
	return count

val = find_frequency(character, sentence)
print val

#Input: t, this is a test
#Output: 3

#Input: y, this is a test
#Output: 0