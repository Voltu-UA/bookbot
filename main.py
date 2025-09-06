import sys
from stats import get_num_words, get_num_characters, get_sorted_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    return file_path.read()

def main():
    with open(sys.argv[1]) as file:
        book_text = get_book_text(file)
        characters_dict = get_num_characters(book_text)
        sorted_characters = get_sorted_characters(characters_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(get_num_words(book_text))
        print("--------- Character Count -------")
        for item in sorted_characters:
            if item['char'].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
main()