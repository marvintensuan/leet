"""
Leetcode Submission Detail

Runtime: 53ms, faster than 84.62% of Python 3 online submissions.
Memory Usage: 13.9 MB, less than 75.84% of Python 3 online submissions.
https://leetcode.com/submissions/detail/726824318/
"""


def roman_to_int(s: str) -> int:
    from itertools import pairwise

    ref: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1_000,
    }

    numbers: list[int] = [ref[el] for el in s]

    signages: list[int] = [1 if a >= b else -1 for a, b in pairwise(numbers + [0])]

    return sum([a * b for a, b in zip(numbers, signages)])


if __name__ == "__main__":

    assert roman_to_int("III") == 3
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
