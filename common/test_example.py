import pytest
from common import example


def test_fib():
    inputs_and_expected_outputs = zip(range(8), [0, 1, 1, 2, 3, 5, 8])
    for input, expected_output in inputs_and_expected_outputs:
        actual_output = example.memoed_fib(input)
        assert actual_output == expected_output
