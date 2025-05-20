from stats import count_words
from stats import count_letters

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()
        return book_text

def main():
    print(f"{count_words(get_book_text("books/frankenstein.txt"))} words found in the document")
    print(count_letters(get_book_text("books/frankenstein.txt")))

main()
