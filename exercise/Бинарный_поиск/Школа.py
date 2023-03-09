"""
В совет школы входят родители, учителя и учащиеся(всего n). Родителей должно
быть k >= 1/3*n

(k + M)/(N + M) >= 1/3
"""


def exercise_count(start, days):
    return (start + (start + days + 1)) // 2


def binary_search(start, N):
    low, high = 0, N
    while low <= high:
        m = (high + low) // 2
        num = exercise_count(start, m)
        if num >= N:
            return m

        if 3 * (k + m) < n + m:
            low = m + 1
        else:
            high = m - 1

