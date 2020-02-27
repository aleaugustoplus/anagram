import sys
import sympy
from util import get_args
from util import show_time
from util import cache_disk
from util import Memoize
from functools import reduce
from collections import defaultdict


class AnagramKey:

    def get_primes(self):
        @Memoize
        @cache_disk()
        def generate_primes():
            return {n - 1: sympy.prime(n) for n in range(1, 256)}
        return generate_primes()

    def __init__(self, word):
        bytes_word = word.encode()
        char_primes = self.get_primes()
        primes = [char_primes[byte] for byte in bytes_word]
        self.word_hash = reduce(lambda x, y: x * y, primes) if primes else 0

    def __hash__(self):
        return self.word_hash

    def __eq__(self, other):
        return self.word_hash == other.word_hash


@show_time
def load_dict(dict_path):
    dict_anagrams = defaultdict(lambda: list())
    with open(dict_path, "r") as file:

        for word in file.readlines():
            word = word.rstrip("\n").lower()
            dict_anagrams[AnagramKey(word)].append(word)

    return dict_anagrams


@show_time
def find_anagram(dict_anagrams, word):
    return dict_anagrams.get(AnagramKey(word.lower()))


if __name__ == '__main__':
    args = get_args()

    print("Welcome to anagram finder!")

    print("Wait loading dictionary")
    dict_anagrams = load_dict(args.dict_path)

    print("You can now enter a word:")
    word = None
    while word != 'exit':
        word = input()
        anagrams = find_anagram(dict_anagrams, word)
        if anagrams:
            print("{len} Anagrams found for: {word} - {anagrams}".format(len=len(anagrams),
                                                                         word=word, anagrams=','.join(anagrams)))
        else:
            print("No anagrams found for {word}".format(word=word))



# angor 10
# elaps 10
# armet 9
# asteer 9
# caret 9
# ester 9
# ante 8
# arist 8
# laster 8
# leapt 8
# abel 7
# acinar 7
# acrolein 7
# agnel 7
# albeit 7
# aldern 7
# alem 7
# alert 7
# alien 7
# argel 7











