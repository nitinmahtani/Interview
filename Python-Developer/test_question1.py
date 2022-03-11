from question1 import select_max


def test_1():
    assert select_max([1, 2, 3]) == 3


def test_2():
    assert select_max([0]) == 0


def test_3():
    assert select_max([0, 0, 0]) == 0


def test_4():
    assert select_max([-10, -2, -8]) == -2


def test_5():
    assert select_max([-10, -2, 1]) == 1


def test_6():
    assert select_max([]) == None



if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
