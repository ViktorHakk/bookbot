def get_book_text(path):
    with open (path) as f:
        file_contents = f.read()
    return file_contents

def count(path):
    book_text = get_book_text(path)
    words = book_text.split()
    word_count = len(words)
    return word_count

def count_characters(path):
    book_text = get_book_text(path)
    small_text = book_text.lower()
    letters = {}
    for text in small_text:
        if text in letters:
            letters[text] += 1
        else:
            letters[text] = 1
    return letters

def count_characters_sorted(path):
    list_of_pairs = []
    list_of_characters = list(count_characters(path).items())
    for character in list_of_characters:
        dict_1 = {}
        dict_1["char"] = character[0]
        dict_1["num"] = character[1]
        list_of_pairs.append(dict_1)
        sorted_list = sorted(list_of_pairs, key=lambda x: x["num"], reverse=True)
    return (sorted_list)

def print_characters(path):
    for row in count_characters_sorted(path):
        if row['char'].isalpha():
            print(f"{row['char']}: {row['num']}")
