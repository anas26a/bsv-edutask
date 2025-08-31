import pytest
import random
from unittest.mock import patch

# Import the diceroll function from helpers instead of redefining it
from src.util.helpers import diceroll

@pytest.mark.demo
@pytest.mark.parametrize('value, expected', [(4, True), (5, True), (6, True)])
def test_diceroll_success(value, expected):
    with patch('src.util.helpers.random.randint') as mockrandint:
        mockrandint.return_value = value
        assert diceroll() == expected