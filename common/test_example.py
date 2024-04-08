import pytest
import example


def test_fib():
    inputs_and_expected_outputs = {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 8}
    for input, expected_output in inputs_and_expected_outputs.items():
        actual_output = example.memoed_fib(input)
        assert actual_output == expected_output
