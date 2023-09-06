import pytest

ARRAY = []
ARRAY_FULL = [1, 2, 3, 4]


@pytest.fixture
def array_fixture():
    return ARRAY.copy()


@pytest.fixture
def array_full_fixture():
    return ARRAY_FULL.copy()
