"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from ch13.ex1_4.analyze_book1 import process_file
import os, sys

def subtract(d1, d2):
    """Returns a set of all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    return set(d1) - set(d2)


def main():
    hist = process_file(os.path.dirname(sys.path[2]) + os.sep + "resource"+ os.sep +"emma.txt", skip_header=True)
    words = process_file(os.path.dirname(sys.path[2]) + os.sep + "resource"+ os.sep +"words.txt", skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff:
        print(word, end=' ')


if __name__ == '__main__':
    main()
