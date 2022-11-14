"""Count words in file."""

import sys

import string
""""
a_string = 'hi. wh?at is the weat [hIer lik?e.
new_string = a_string.translate(str.maketrans('',", string-punctuation))
"""
def tokenize(filename):
    """Return a list of words from the file at filename. For example:
    >>> tokenize("test.txt")
    ['As', 'I', 'was', 'going', 'to', 'St.', 'Ives', ..., 'many', 'were', 'Ives?']
    """
    with open(filename) as file:
        
        words = []
        for line in file:
            # create a list of words
            # line = ['a', 'b', 'c']
            line = line.rstrip().split(" ")
            for word in line:
                word = word.lower()
                word = word.translate(str.maketrans('','', string.punctuation))
                words.append(word)

        return words

# print(tokenize('test.txt'))

def count_words(filename):
    """Take in a list of strings and return a dictionary of each string and 
    the number of times it appears in the list. For example:
    >>> count_words(["apple", "berry", "cherry", "apple"])
    {'apple': 2, 'berry': 1, 'cherry': 1}"""
    
    words = {}
    words_list = tokenize(filename)
    for word in words_list:
       words[word] = words.get(word, 0) + 1 
    return words

# print(count_words('test.txt'))

def print_word_counts(filename):
    """Take in a dictionary of word counts and print each key and value from the dictionary.
    >>> print_word_counts({'apple': 2, 'berry': 1, 'cherry': 1})
    apple 2
    berry 1
    cherry 1
    """
    words = count_words(filename)
    for word, occur in words.items():
        print(f'{word}: {occur}')

print(print_word_counts('test.txt'))

# put your code here.
# def count_words(data_file):
#     with open(data_file) as file:
#         # create a dictionary to store the words and their occcurences 
#         # words = {'word': occur}
#         words = {}
#         for line in file:
#             # create a list of words
#             # line = ['a', 'b', 'c']
#             line = line.rstrip().split(" ") 
#             for word in line:
#                 words[word] = words.get(word, 0) + 1
#         for word, occur in words.items():
#             print(f'{word}: {occur}')
# count_words('twain.txt')

 
