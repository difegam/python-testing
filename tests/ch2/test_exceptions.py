"""
See error in tests/ch2/test_experiment.py

cmd: poetry run pytest test_exceptions.py -vv

=================================== test session starts ===================================
collected 3 items

test_exceptions.py::test_no_path_raises PASSED                                       [ 33%]
test_exceptions.py::test_raises_with_info PASSED                                     [ 66%]
test_exceptions.py::test_raises_with_info_alt PASSED                                 [100%]

==================================== 3 passed in 0.13s ====================================
"""

import pytest
import cards


def test_no_path_raises():
    with pytest.raises(TypeError):
        cards.CardsDB()


def test_raises_with_info():
    match_regex = "missing 1 .* positional argument"
    with pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()


def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exc_info:
        cards.CardsDB()
    expected = "missing 1 required positional argument"
    assert expected in str(exc_info.value)
