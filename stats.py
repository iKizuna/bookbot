def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def words(text):
    words = text.split()
    return len(words)

def character_appears(book_text):
    lower_text = book_text.lower()
    character_appears = {}
    for char in lower_text:
        if char.isalpha():
            character_appears[char] = character_appears.get(char, 0) + 1  
    return character_appears

def sort_on(dict):
    return dict["num"]

def pretty_dictionary(dictionary):
    # Create a list of {'char': ..., 'num': ...} dictionaries
    character_list = [{'char': char, "num": count} for char, count in dictionary.items()]
    # Sorts the character_list
    character_list.sort(reverse=True, key=sort_on)
    return character_list
