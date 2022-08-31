from ..average import average


def test_average():
    test_list = [1, 2, 3]
    assert average(test_list) == 2.0
