import sys
from stats import count_words, count_characters, sort_count

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    f.close()
    return contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    file_path = sys.argv[1]
    contents = get_book_text(file_path)
    num_words = count_words(contents)
    # print(f"{num_words} words found in the document")
    num_chars = count_characters(contents)
    # print(num_chars)
    sorted_count = sort_count(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



main()

