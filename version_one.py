from util import get_args
from util import show_time
from collections import defaultdict


@show_time
def load_dict(dict_path):
    dict_anagrams = defaultdict(lambda: list())
    with open(dict_path, "r") as file:
        for word in file.readlines():
            word = word.rstrip("\n")
            sorted_word = ''.join(sorted(word))
            dict_anagrams[sorted_word].append(word)

    return dict_anagrams


@show_time
def find_anagram(dict_anagrams, word):
    sorted_word = ''.join(sorted(word))
    return dict_anagrams.get(sorted_word)


if __name__ == '__main__':
    args = get_args()

    print("Welcome to anagram finder!")

    print("Wait loading dictionary")
    dict_anagrams = load_dict(args.dict_path)
    print("Dictionary loaded!")

    word = None
    while word != 'exit':
        word = input()
        anagrams = find_anagram(dict_anagrams, word)
        if anagrams:
            print("{len} Anagrams found for: {word} - {anagrams}".format(len=len(anagrams),
                                                                         word=word, anagrams=','.join(anagrams)))
        else:
            print("No anagrams found for {word}".format(word=word))





















