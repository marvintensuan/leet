"""
Leetcode Submission Detail

Runtime: 00ms, faster than 00.00% of Python 3 online submissions.
Memory Usage: 00.0 MB, less than 00.00% of Python 3 online submissions.
https://leetcode.com/submissions/detail/
"""


def func() -> int:
    return -1


if __name__ == "__main__":

    CASES = (
        (func(), -1)
    )
    
    def test_cases() -> None:
        for assertion, rv in CASES:
            try:
                assert assertion == rv, f"{assertion = }, {rv = }"
            except AssertionError as e:
                print(e)

    test_cases()