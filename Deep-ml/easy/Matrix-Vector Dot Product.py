# https://www.deep-ml.com/problems/1
from __future__ import annotations


def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(a[0]) != len(b):
        return -1
    return [sum(row[i] * b[i] for i in range(len(b))) for row in a]

