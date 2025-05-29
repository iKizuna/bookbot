def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def words(text):
    words = text.split()
    return len(words)