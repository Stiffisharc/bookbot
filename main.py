from stats import count_words
from stats import count_letters
from stats import sort_letters
from stats import list_letters
from stats import rem_labels

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()
        return book_text

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    counted_letters = count_letters(book_text)
    listed_letters = list_letters(counted_letters)
    listed_letters.sort(reverse=True, key=sort_letters)
    letters = rem_labels(listed_letters)
    print(" ")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in letters:
        print(letter)
    print("============= END ===============")
    print(" ")

main()
