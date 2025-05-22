import sys
from stats import count_words
from stats import count_letters
from stats import sort_letters
from stats import list_letters

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()
        return book_text

def print_report(book_path, word_count, letter_list):
    print(" ")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in letter_list:
        print(f"{letter["letter"]}: {letter["count"]}")
    print("============= END ===============")
    print(" ")

def main():
    err = "Usage: python3 main.py <path_to_book>"
    try:
        if sys.argv[1] == None:
            trigger = None
    except IndexError:
        print(err)
        sys.exit(1)
    try:
        if sys.argv[2] != None:
            print(err)
            sys.exit(1) 
    except IndexError:
        trigger = None
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    counted_letters = count_letters(book_text)
    listed_letters = list_letters(counted_letters)
    listed_letters.sort(reverse=True, key=sort_letters)
    print_report(book_path, word_count, listed_letters)

main()
