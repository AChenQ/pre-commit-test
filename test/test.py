#!/usr/bin/env python3
#
# zhen.chen test.
#

"""test"""
import sys


def add_test(add_a: int, add_b: int) -> int:
    """
    return added number
    """
    return add_a + add_b


if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    print(add_test(int(a), int(b)))
