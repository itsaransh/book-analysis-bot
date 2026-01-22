import sys
from stats import count_words, count_characters, list_of_char_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

PATH_TO_BOOK = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return (file_contents)

def main():
    book_text = get_book_text(PATH_TO_BOOK)
    word_count = count_words(book_text)

    character_count = count_characters(book_text)
    sorted_list_of_char_dict = list_of_char_dict(character_count)

    #printing report
    print("============ BOOK-ANALYSIS-BOT ============")
    print(f"Analyzing book found at ${PATH_TO_BOOK}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_list_of_char_dict:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()