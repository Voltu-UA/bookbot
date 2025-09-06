def get_num_words(book_text):
    words = len(book_text.split())
    return f"Found {words} total words"

def get_num_characters(book_text):
    words = book_text.split()
    characters = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def get_sorted_characters(character_dict):
    list_of_dicts = []
    for item in character_dict:
        list_of_dicts.append({"char": item, "num": character_dict[item]})

    list_of_dicts.sort(key=sort_on, reverse=True)

    return list_of_dicts

def sort_on(items):
    return items["num"]
