"""
output:

=================================== test session starts ===================================
collected 1 item

test_experiment.py F                                                                 [100%]

======================================== FAILURES =========================================
____________________________________ test_no_path_fail ____________________________________
test_experiment.py:4: in test_no_path_fail
    cards.CardsDB()
E   TypeError: CardsDB.__init__() missing 1 required positional argument: 'db_path'
================================= short test summary info =================================
FAILED test_experiment.py::test_no_path_fail - TypeError: CardsDB.__init__() missing 1 required positional argument: 'db_path'
==================================== 1 failed in 0.30s ====================================

"""


import cards


def test_no_path_fail():
    cards.CardsDB()


# poetry run pytest --tb=short test_experiment.py
