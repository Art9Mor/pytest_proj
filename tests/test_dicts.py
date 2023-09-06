from utils.dicts import get_val

DATA = {'war': 'allways'}
DATA_empty = {}


def test_get_val():
    assert get_val(DATA, 'war') == 'allways'
    assert get_val(DATA, 'peace') == 'git'
    assert get_val(DATA_empty, 'war', 'git') == 'git'
    assert get_val(DATA_empty, 'war', 'chaos') == 'chaos'
