import sys
from stats import num_words_in_string
from stats import num_characters_in_string
from stats import sorted_list_of_dictionaries

def get_book_text(file_path):
	with open(file_path) as f:
		return str(f.read())

def print_character_report(dictionary_list, total_words):
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {total_words} total words")
	print("--------- Character Count -------")
	for dict in dictionary_list:
		if dict["char"].isalpha():
			print(f"{dict["char"]}: {dict["num"]}")
	print("============= END ===============")

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	file_text = get_book_text(sys.argv[1])
	
	num_chars_dictionary = num_characters_in_string(file_text)
	num_chars_dictionary_sorted = sorted_list_of_dictionaries(num_chars_dictionary)
	print_character_report(num_chars_dictionary_sorted, num_words_in_string(file_text))

main()
