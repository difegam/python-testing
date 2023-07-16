"""
    > : Failure point
    E : Extra info about the assert failure

    cmd: poetry run pytest test_card_fail.py


    ________________________________________ test_card_fail ________________________________________

    def test_card_fail():
        c1 = Card("sit there", "Diego")
        c2 = Card("do something", "Gamboa")
>       assert c1 == c2
E       AssertionError: assert Card(summary='sit there', owner='Diego', state='todo', id=None) == Card(summary='do something', owner='Gamboa', state='todo', id=None)
E
E         Matching attributes:
E         ['state']
E         Differing attributes:
E         ['summary', 'owner']
E
E         Drill down into differing attribute summary:
E           summary: 'sit there' != 'do something'
E           - do something
E           + sit there
E
E         Drill down into differing attribute owner:
E           owner: 'Diego' != 'Gamboa'
E           - Gamboa
E           + Diego

test_card_fail.py:6: AssertionError

"""


from cards import Card


def test_card_fail():
    c1 = Card("sit there", "Diego")
    c2 = Card("do something", "Gamboa")
    assert c1 == c2
