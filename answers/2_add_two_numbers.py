"""
Leetcode Submission Detail

Runtime: 00ms, faster than 00.00% of Python 3 online submissions.
Memory Usage: 00.0 MB, less than 00.00% of Python 3 online submissions.
https://leetcode.com/submissions/detail/
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    s = int(to_numberlike(l1)[::-1]) + int(to_numberlike(l2)[::-1])

    return to_node(str(s)[::-1])


def to_numberlike(node: ListNode) -> str:
    if node.next is None:
        return str(node.val)
    return f"{node.val}{to_numberlike(node.next)}"


def to_node(s: str) -> ListNode:
    if len(s) == 1:
        return ListNode(val=int(s[0]), next=to_node(s[1:]))
    return ListNode(val=int(s[0]), next=to_node(s[1:]))


if __name__ == "__main__":

    # CASES = (addTwoNumbers(), -1)

    def test_cases() -> None:
        # for assertion, rv in CASES:
        #     try:
        #         assert assertion == rv, f"{assertion = }, {rv = }"
        #     except AssertionError as e:
        #         print(e)
        ...

    test_cases()
