from p05_tests.hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("Yunqi") == "hello, Yunqi"


# Example 1
"""
def test_hello():
    assert hello("Yunqi") == "hello, Yunqi"
    assert hello() == "hello, world"
"""
