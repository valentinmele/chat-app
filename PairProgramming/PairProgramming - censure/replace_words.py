
def censor(text, word):
	word_list = text.split()
	result = ""
	stars = "*" * len(word)
	count = 0
	index = 0

	for i in word_list:
		if i == word:
			word_list[index] = stars
		index += 1

	result = " ".join(word_list)

	return result


# Driver code
if __name__ == "__main__":

	extract = "GeeksforGeeks is a computer science portal for geeks.I am pursuing my major in computer science."
	words = ["computer", "portal for"]

	for word in words:
		extract = censor(extract, word)
	print(extract)
