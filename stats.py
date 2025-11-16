# function to return the number of words in a string
def word_count(text):
	words = text.split()
	return len(words)

# function to take a given string and return the number of times each unique character appears
def char_freq(text):
	freq = {}
	for c in text:
		if c.lower() in freq:
			freq[c.lower()] += 1
		else:
			freq[c.lower()] = 1
	return freq

# function that takes a dictionary of characters and their frequencies and returns a sorted list of dictionaries with the format: {'char': character, 'num': frequency}
def char_freq_list(freq_dict):
	freq_list = []
	for char, num in freq_dict.items():
		freq_list.append({'char': char, 'num': num})
	# sort the list from greatest to least frquency, using separate helper function
	freq_list.sort(key=sort_on, reverse=True)
	return freq_list

# helper to return the "num" value from a dictionary
def sort_on(item):
	return item['num']
	