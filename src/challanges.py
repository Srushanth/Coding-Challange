from typing import List


def get_capital_indexes(input_string: str) -> List[int]:
    """
    This function returns the indices of all the uppercase letters in a string.

    Args:
        input_string (str): The string to be processed.

    Returns:
        List[int]: A list of indices where uppercase letters are found.
    """
    return [index for index, char in enumerate(input_string) if char.isupper()]


def mid(input_string: str) -> str:
    """
    This function returns the middle character of a given string.
    If the middle character is not found, an empty string is returned.

    Args:
        input_string (str): The string to be processed.

    Returns:
        str: An empty string or a character.
    """
    len_input_string = len(input_string)
    return input_string[len_input_string // 2] if len_input_string % 2 == 1 else ""
