"""
Leetcode Submission Detail

Runtime: 802ms, faster than 69.26% of Python 3 online submissions.
Memory Usage: 28.5 MB, less than 89.90% of Python 3 online submissions.
https://leetcode.com/submissions/detail/731013502/
"""


def furthest_building(heights: list[int], bricks: int, ladders: int) -> int:
    import heapq
    from itertools import pairwise

    jumps = [b - a if b > a else 0 for a, b in pairwise(heights + [0])]

    min_heap: list[int] = []

    for idx, jump in enumerate(jumps):
        if jump <= 0:
            continue

        if jump > 0:
            heapq.heappush(min_heap, jump)

        if len(min_heap) > ladders:
            brick_need = heapq.heappop(min_heap)
            bricks -= brick_need

        if bricks < 0:
            return idx

    return idx


if __name__ == "__main__":

    assert furthest_building(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1) == 4
    assert furthest_building(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2) == 7
    assert furthest_building(heights=[14, 3, 19, 3], bricks=17, ladders=0) == 3
    assert furthest_building(heights=[1, 5, 1, 2, 3, 4], bricks=4, ladders=1) == 5
