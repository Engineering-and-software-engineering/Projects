def get_words_set(text):
    "Returns the set of all words from a text"

    return set(text.split())

def get_index_list(words_sets, word):
    "Returns the list of indexes of sets containing a word"

    return [i for i, s in enumerate(words_sets) if word in s]

def create_index(words_sets, merged_words_set):
    "Returns the inverted index"

    return {word: get_index_list(words_sets, word) for word in merged_words_set}

def inverted_index(list_text):
    """
    Get a list of string and returns a dictionary
    containing an inverted index.

    http://en.wikipedia.org/wiki/Inverted_index
    """

    words_sets = map(get_words_set, list_text)

    merge_set = lambda a, b: a | b
    merged_words_set = reduce(merge_set, words_sets, set([]))

    return create_index(words_sets, merged_words_set)
