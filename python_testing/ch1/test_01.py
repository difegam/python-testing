def test_01_passing():
    assert (500 + 500) == 1000


def test_02_failing():
    assert (500 + 499) == 1000


def test_03_error():
    raise Exception("This is a test exception")


def test_04_tuple_equality():
    assert (1, 2, 3) == (1, 2, 3)


def test_05_list_inequality():
    assert [1, 2, 3] != [1, 2, 4]


def test_06_list_failure():
    assert [1, 2, 3] == [1, 2, 4]
