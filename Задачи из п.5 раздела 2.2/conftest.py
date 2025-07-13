import pytest
import random

@pytest.fixture()
def random_int():
    return random.randint(0,100)
