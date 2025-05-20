def count_words(book_text):
    word_count = 0
    book = book_text
    words = book.split()
    for word in words:
        word_count += 1
    return word_count

def count_letters(book_text):
    chars = {}
    for char in book_text:
         char = char.lower()
         if char in chars:
             chars[char] += 1
         else:
             chars[char] = 1
    return chars
