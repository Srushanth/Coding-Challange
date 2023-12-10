# Coding Challenges

This repository contains my solutions to various coding challenges.

## Structure

The code for the challenges is located in the `./src/challenges.py` file. Each challenge is solved in a separate function.

Tests for these functions are written using pytest and are located in the `./tests/test_challenges.py` file.

## Challenges

>### Challenge 1

#### Problem: 

- *Create a function called `capital_indexes`. This function should accept a single argument, a string. The function should return a list containing the indexes of all the uppercase letters in the string. For instance, if we call `capital_indexes("Hello, World!")`, it should return the `list [0, 7]`*.

#### Solution: 

- **Function**: [get_capital_indexes](./src/challenges.py)
- **Description**: This function returns the indices of all the uppercase letters in a string.
- **Status**: Completed
- **Test**: [test_get_capital_indexes](./tests/test_challenges.py)

>### Challenge 2

#### Problem: 

- *Construct a function called mid which accepts a string as its argument. Your function should identify and return the middle character of the string. If the string doesn't have a middle character (i.e., its length is even), your function should return an empty string. For instance, calling `mid("abc")` should yield `"b"`, while calling `mid("aaaa")` should yield `""`.*.

#### Solution: 

- **Function**: [mid](./src/challenges.py)
- **Description**: This function returns the middle character of a given string. If the middle character is not found, an empty string is returned.
- **Status**: Completed
- **Test**: [mid](./tests/test_challenges.py)

>### Challenge 3

#### Problem: 

- *Tracking Online Presence: The objective of this problem is to count the number of individuals who are online, given a dictionary representing people's online status. For instance, take the following dictionary:*
    
```python
status = {
       "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
   }
```
- *In this scenario, the count of people online is 2. You need to write a function called `online_count`. This function should accept one argument. The argument is a dictionary that associates names (strings) with either the string "online" or "offline". The function should return the count of individuals who are online.*

#### Solution: 

- **Function**: [online_count](./src/challenges.py)
- **Description**: Counts the number of individuals who are online.
- **Status**: Completed
- **Test**: [online_count](./tests/test_challenges.py)

>### Challenge 4

#### Problem: 

- *Create a function named `random_number` that doesn't take any arguments. The function should generate and return a random integer between `1 and 100`, inclusive.*
- *When you call the function multiple times, it should (in most cases) return different numbers.*
- *For instance, if you call `random_number()` several times, it might initially return 42, then 63, and then 1.*

#### Solution: 

- **Function**: [random_number](./src/challenges.py)
- **Description**: This function will return a random number between 0 and 101.
- **Status**: Completed
- **Test**: [test_random_number](./tests/test_challenges.py)

___
<!-- Add more challenges in the same way -->

## Running Tests

To run the tests, navigate to the root directory of the project and run the following command:

```bash
pytest ./tests/test_challenges.py
```
