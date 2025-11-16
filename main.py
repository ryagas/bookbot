from stats import char_freq, char_freq_list, char_freq_list, word_count
import sys

# function to get the book text from a file
def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) != 2:
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)
	book_path = sys.argv[1]
	print('============ BOOKBOT ============')
	print(f'Analyzing book found at {book_path}...')
	book_txt = get_book_text(book_path)
	print('----------- Word Count ----------')
	print(f"Found {word_count(book_txt)} total words")
	print('--------- Character Count -------')
	char_frequencies = char_freq(book_txt)	
	sorted_char_freq = char_freq_list(char_frequencies)
	for item in sorted_char_freq:
		if not item["char"].isalpha():
				continue
		print(f'{item["char"]}: {item["num"]}')

main()