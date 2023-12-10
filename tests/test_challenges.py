import pytest
from src.challenges import get_capital_indexes
from src.challenges import mid
from src.challenges import online_count
from src.challenges import random_number


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
        get_capital_indexes(123)  # type: ignore
        get_capital_indexes(None)  # type: ignore
        get_capital_indexes([1, 2, 3])  # type: ignore


def test_mid() -> None:
    """
    This is the test created to test "mid" function.
    """
    assert mid("123") == "2"
    assert mid("Hello") == "l"
    assert mid("hi") == ""
    assert mid("This is Srushanth") == "S"
    assert mid("12345") == "3"
    assert mid("") == ""

    # Test with non-string inputs
    with pytest.raises(TypeError):
        mid(123)  # type: ignore
        mid(None)  # type: ignore
        mid([1, 2, 3])  # type: ignore


@pytest.mark.parametrize("input_string, output",
                         [("123", "2"),
                          ("Hello", "l"),
                          ("hi", ""),
                          ("This is Srushanth", "S"),
                          ("", "")])
def test_mid(input_string: str, output: str) -> None:
    """
    This is the test created to test "mid" function.
    """
    assert mid(input_string) == output

    # Test with non-string inputs
    with pytest.raises(TypeError):
        mid(123)  # type: ignore
        mid(None)  # type: ignore
        mid([1, 2, 3])  # type: ignore


@pytest.mark.parametrize(
    "input_dict, output",
    [
        ({}, 0),
        ({"Alice": "online"}, 1),
        ({"Bob": "offline", "Charlie": "online"}, 1),
        ({"David": "offline", "Eve": "online", "Frank": "offline"}, 1),
        ({"Grace": "online", "Heidi": "offline", "Ivan": "online", "Judy": "offline"}, 2),
        ({"Mallory": "online", "Nina": "offline", "Oscar": "online", "Peggy": "offline", "Quincy": "online"}, 3),
        ({"Randy": "offline", "Steve": "online", "Tina": "offline", "Ursula": "online", "Victor": "offline",
          "Wendy": "online", "Xavier": "offline"}, 3)
    ]
)
def test_online_count(input_dict: dict, output: int):
    """
    This is the test created to test "online_count" function.

    Args:
        input_dict (dict): _description_
        output (int): _description_
    """
    assert online_count(input_dict) == output

    # Test with non-dict inputs.
    with pytest.raises(TypeError):
        online_count(123)  # type: ignore
        online_count(None)  # type: ignore
        online_count([1, 2, 3])  # type: ignore


@pytest.mark.parametrize("input_int", range(10))
def test_random_number(input_int: int) -> None:
    """
    This is the test created to test "random_number" function.

    Args:
        input_int (int): Random number.
    """
    number = random_number()
    assert isinstance(number, int)
    assert number in list(range(1, 101))


# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
