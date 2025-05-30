import sys
from stats import words, get_book_text, character_appears, pretty_dictionary

def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        book_text = get_book_text(file_path)
        number_of_words = words(book_text)
        number_of_characters = character_appears(book_text)
        pretty_words = pretty_dictionary(number_of_characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("--------- Character Count -------")
        for entry in pretty_words:
            print(f"{entry['char']}: {entry['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()