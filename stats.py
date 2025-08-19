def num_words_in_string(text):
        split = text.split()
        return len(split)

def num_characters_in_string(string):
	chars = {}
	for char in string:
		letter = char.lower()
		if letter in chars:
			chars[letter] += 1
		else:
			chars[letter] = 1
	return chars

def sort_on(items):
	return items["num"]

def sorted_list_of_dictionaries(dictionary):
	dictionary_list = []
	for pair in dictionary:
		dictionary_list.append({"char": pair, "num": dictionary[pair
]})
	dictionary_list.sort(reverse=True, key=sort_on)
	return dictionary_list
