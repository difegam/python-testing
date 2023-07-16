from cards import Card
import pytest


def test_card_fail():
    c1 = Card("sit there", "Diego")
    c2 = Card("do something", "Gamboa")
    if c1 != c2:
        pytest.fail("they don't match")
