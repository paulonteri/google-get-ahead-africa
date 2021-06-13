"""
Car Plate Vocabulary:

We need to find the shortest word from a vocabulary that includes all the letters from a given licence plate. 
The shorter the word, the better. 
The licence plates start with two or three letters, then they are followed by 5 characters, from which at most 2 are letters, the rest are digits.
Write a solution that will find the shortest words for 1000 licence plates. 
You are given a vocabulary containing all valid words. 
    Keep duplicate letters
    Ordering is irrelevant
    Case is irrelevant
    The vocabulary is sorted lexicographically
    The vocabulary contains about 4 million entries
Example: 
    For the licence plate RT 123SO the shortest word would be SORT:
    For RC 10014 the shortest word would be CAR.
"""


def is_valid_word(plate_letters, word):

    # get all letters from the word
    word_letters = {}
    for char in word:
        letter = char.lower()
        if letter in word_letters:
            word_letters[letter] = word_letters[letter] + 1
        else:
            word_letters[letter] = 1

    # check if it does not match all the letters from the plate
    for plate_letter, plate_letter_count in plate_letters.items():
        if plate_letter not in word_letters:
            return False
        if word_letters[plate_letter] < plate_letter_count:
            return False

    return True


def find_shortest_word(plate, vocabulary):
    shortest_valid_word = ""

    # get all letters from the plate
    plate_letters = {}
    for char in plate:
        if char.isalpha():
            letter = char.lower()
            if letter in plate_letters:
                plate_letters[letter] = plate_letters[letter] + 1
            else:
                plate_letters[letter] = 1

    for word in vocabulary:
        if is_valid_word(plate_letters, word) and (
                shortest_valid_word == "" or len(word) < len(shortest_valid_word)):
            shortest_valid_word = word

    return shortest_valid_word
