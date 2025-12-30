import sys
from stats import count_characters, sort_characters


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    book_text = get_book_text(book_path)

    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    character_counts = count_characters(book_text)
    sorted_characters = sort_characters(character_counts)

    for item in sorted_characters:
        char = item["char"]
        count = item["num"]

        if not char.isalpha():
            continue

        print(f"{char}: {count}")

    print("============= END ===============")
    

main()

