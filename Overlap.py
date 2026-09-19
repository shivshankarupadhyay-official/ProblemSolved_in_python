intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]
def merge(intervals):
    if not intervals:
        return []

    sorted_intervals = sorted(intervals,ke)