from util import get_args
from util import show_time
from functools import reduce
from collections import defaultdict


class AnagramKey:

    def __init__(self, word):
        if word:
            max_char = reduce(max, map(ord, word))
            counts = [0] * (max_char + 1)
            for word_char in word:
                counts[ord(word_char)] += 1

            self.ana_hash = tuple(counts)
        else:
            self.ana_hash = tuple()

    def __hash__(self):
        return self.ana_hash.__hash__()

    def __eq__(self, other):
        return self.ana_hash == other.ana_hash


@show_time
def load_dict(dict_path):
    dict_anagrams = defaultdict(lambda: set())
    with open(dict_path, "r") as file:
        for word in file.readlines():
            word = word.rstrip("\n").lower()
            dict_anagrams[AnagramKey(word)].add(word)

    return dict_anagrams


@show_time
def find_anagram(dict_anagrams, word):
    return dict_anagrams.get(AnagramKey(word.lower()))


if __name__ == '__main__':
    args = get_args()

    print("Welcome to anagram finder!")

    print("Wait! Loading dictionary...")
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




















