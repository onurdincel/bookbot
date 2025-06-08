import sys
from stats import get_num_words, get_sorted_chars

def get_book_text(filepath):
    with open(filepath, encoding = "utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    content = get_book_text(file_path)

    words = get_num_words(content)
    chars = get_sorted_chars(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for x in chars:
        char, num = x["char"], x["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()
