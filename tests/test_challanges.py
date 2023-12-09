import pytest
from src.challanges import get_capital_indexes


def test_get_capital_indexes() -> None:
    """
    This is the test created to test "get_capital_indexes" function.
    """
    assert get_capital_indexes("HelLo") == [0, 3]
    assert get_capital_indexes("Hello, World") == [0, 7]
    assert get_capital_indexes("no capitals here") == []
    assert get_capital_indexes("") == []
    
    # Test with non-string inputs
    with pytest.raises(TypeError):
        get_capital_indexes(123)
        get_capital_indexes(None)
        get_capital_indexes([1, 2, 3])


# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
