# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


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



>### Challenge 2

#### Problem: 

- *Construct a function called mid which accepts a string as its argument. Your function should identify and return the middle character of the string. If the string doesn't have a middle character (i.e., its length is even), your function should return an empty string. For instance, calling `mid("abc")` should yield `"b"`, while calling `mid("aaaa")` should yield `""`.*.

#### Solution: 



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



>### Challenge 4

#### Problem: 

- *Create a function named `random_number` that doesn't take any arguments. The function should generate and return a random integer between `1 and 100`, inclusive.*
- *When you call the function multiple times, it should (in most cases) return different numbers.*
- *For instance, if you call `random_number()` several times, it might initially return 42, then 63, and then 1.*

#### Solution: 



___
<!-- Add more challenges in the same way -->

## Running Tests

To run the tests, navigate to the root directory of the project and run the following command:

```bash
```
