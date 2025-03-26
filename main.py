from stats import get_num_words, get_character_count, sort_by_value
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    filepath = sys.argv[1]
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = get_num_words(text)
    character_count = get_character_count(text)
    values = sort_by_value(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for value in values:
        if value["char"].isalpha():
            print(f"{value["char"]}: {value["count"]}")
    print("============= END ===============")


main()
