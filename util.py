import os
import time
import pickle
from argparse import ArgumentParser
from hashlib import sha1


def get_args():
    """Parse command line arguments."""
    parser = ArgumentParser(description="Anagram finder - This software find if a word has anagrams or not")

    parser.add_argument("-dict_path",
                        type=str,
                        default="dictionary.txt",
                        help="Dictionary path",
                        required=False)

    return parser.parse_args()


def show_time(function):
    def timed_func(*args, **kw):
        start = time.time()
        result = function(*args, **kw)
        end = time.time()
        print("Time taken to", function.__name__, "-", int((end - start) * 1_000), "ms")
        return result
    return timed_func


class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


def cache_disk(cache_folder="."):
    """Caching functions for 5 days"""
    def do_cache(function):
        def inner_function(*args, **kwargs):
            """Calculate a cache key based on the decorated method signature
            args[1] indicates the domain of the inputs, we hash on domain!
            """
            key = sha1((str(args) + str(kwargs)).encode('utf-8')).hexdigest()
            filepath = os.path.join(cache_folder, key)

            # verify that the cached object exists
            if os.path.exists(filepath):
                return pickle.load(open(filepath, "rb"))

            # call the decorated function...
            result = function(*args, **kwargs)
            # ... and save the cached object for next time
            pickle.dump(result, open(filepath, "wb"))
            return result
        return inner_function
    return do_cache





