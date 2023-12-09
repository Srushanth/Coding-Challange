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
