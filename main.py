from stats import words, get_book_text

def main():
    book_text = get_book_text('books/frankenstein.txt')
    number_of_words = words(book_text)
    print(f"{number_of_words} words found in the document")

main()