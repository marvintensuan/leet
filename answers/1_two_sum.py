"""
Leetcode Submission Detail

Runtime: 80ms, faster than 76.77% of Python 3 online submissions.
Memory Usage: 15.2 MB, less than 24.24% of Python 3 online submissions.
https://leetcode.com/submissions/detail/738198048/
"""


def two_sum(nums: list[int], target: int) -> list[int]:

    ## f = filter(lambda x: True if x[1] <= target else False, enumerate(nums))
    # e = combinations(enumerate(nums), 2)
    # g = filter(lambda x: x[0][1] + x[1][1] == target, e)
    # (i, x), (j, y) = next(g)

    ndict: dict[int, int] = {}

    for idx, num in enumerate(nums):
        diff = target - num
        if diff in ndict:
            return [ndict[diff], idx]

        ndict[num] = idx

    return [-999, -999]


if __name__ == "__main__":

    CASES = (
        (two_sum(nums=[2, 7, 11, 15], target=9), [0, 1]),
        (two_sum(nums=[3, 2, 4], target=6), [1, 2]),
        (two_sum(nums=[3, 3], target=6), [0, 1]),
        (two_sum(nums=[-3, 4, 3, 90], target=0), [0, 2]),
    )

    def test_cases() -> None:
        for assertion, rv in CASES:
            try:
                assert assertion == rv, f"{assertion = }, {rv = }"
            except AssertionError as e:
                print(e)

    test_cases()
