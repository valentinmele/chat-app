# Python Program to censor a word
# with asterisks in a sentence


# Function takes two parameter
def censor(text, word):

	# Break down sentence by ' ' spaces
	# and store each individual word in
	# a different list
	word_list = text.split()

	# A new string to store the result
	result = ""

	# Creating the censor which is an asterisks
	# "*" text of the length of censor word
	stars = "*" * len(word)

	# count variable to
	# access our word_list
	count = 0

	# Iterating through our list
	# of extracted words
	index = 0
	for i in word_list:

		if i == word:

			# changing the censored word to
			# created asterisks censor
			word_list[index] = stars
		index += 1

	# join the words
	result = " ".join(word_list)

	return result


# Driver code
if __name__ == "__main__":

	extract = "GeeksforGeeks is a computer science portal for geeks.I am pursuing my major in computer science."
	words = ["computer", "portal"]

	for word in words:
		extract = censor(extract, word)
	print(extract)
