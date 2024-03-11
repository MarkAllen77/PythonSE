import pytest
import functions as instance_test_demo


@pytest.fixture
def correct_rectangle():
    return instance_test_demo.Rectangle(10, 20)


@pytest.fixture
def improper_rectangle():
    return instance_test_demo.Rectangle(5, 20)
