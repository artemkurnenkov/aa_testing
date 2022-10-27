from src.main import *
import pytest


def test_sum_for_api():
    assert sum_for_api(1, 1) == 2


@pytest.mark.hello
def test_hello():
    assert hello() == "Hello, Glowbyte!"
        