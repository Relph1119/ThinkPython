"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

import ch12.ex2.anagram_sets as anagram_sets

def metathesis_pairs(d):
    """Print all pairs of words that differ by swapping two letters.

    d: map from word to list of anagrams
    """
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


def word_distance(word1, word2):
    """Computes the number of differences between two words.

    word1, word2: strings

    Returns: integer
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


if __name__ == '__main__':
    import os, sys
    sets = anagram_sets.all_anagrams(os.path.dirname(sys.path[2]) + os.sep + "resource"+ os.sep +"words.txt")
    metathesis_pairs(sets)