from utils import arrs


def test_get(array_fixture, array_full_fixture):
    assert arrs.get(array_full_fixture, 1, "test") == 2
    assert arrs.get(array_fixture, 0, "test") == "test"


def test_slice(array_fixture, array_full_fixture):
    assert arrs.my_slice(array_full_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_full_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(array_fixture) == []
    assert arrs.my_slice(array_full_fixture, end=2) == [1, 2]
