def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    chars = {}
    for char in book_text:
        char = char.lower()
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        else:
            pass
    return chars

def list_letters(dict1):
    letter_list = []
    for letter in dict1:
        count = dict1[letter]
        dict2 = {}
        dict2["letter"] = letter
        dict2["count"] = count
        letter_list.append(dict2)
    return letter_list

def sort_letters(dictionary):
    return dictionary["count"]
