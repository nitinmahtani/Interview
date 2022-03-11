from question_3 import minimum_points


def test_1():
    assert minimum_points(2, [1, 2, 3]) == 2


def test_2():
    assert minimum_points(4, [1, 2, 3, 4, 5]) == 3


def test_3():
    assert minimum_points(4, [1, 2, 3, 5, 8]) == 3


def test_4():
    assert minimum_points(12, [1, 2, 3, 5, 8, 13, 14, 15, 18]) == 4


def test_5():
    assert minimum_points(100, [1]) == 1


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
