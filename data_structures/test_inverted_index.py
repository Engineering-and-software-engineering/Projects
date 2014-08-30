from inverted_index import (
    inverted_index,
    get_words_set,
    get_index_list,
    create_index,
)

def test_get_words_set():
    text = 'it is what it is'
    expected = set(['it', 'is', 'what'])
    assert get_words_set(text) == expected

def test_get_index_list():
    t = ["it is what it is", "what is it", "it is a banana"]
    expected = [0, 1, 2]
    assert get_index_list(t, 'is') == expected

def test_create_index():
    words_sets = [set(['a', 'b']), set(['b', 'c'])]
    merged_words_set = set(['a', 'b', 'c'])
    expected = {
        'a': [0],
        'b': [0, 1],
        'c': [1]
    }
    actual_result = create_index(words_sets, merged_words_set)
    assert type(actual_result) == dict
    assert actual_result == expected

def test_inverted_index():
    t = ["it is what it is", "what is it", "it is a banana"]
    expected = {
        'a': [2],
        'banana': [2],
        'is': [0, 1, 2],
        'it': [0, 1, 2],
        'what': [0, 1]
    }
    assert inverted_index(t) == expected
    assert inverted_index([]) == {}
    assert inverted_index(["", "", ""]) == {}
