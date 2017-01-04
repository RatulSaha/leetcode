"""
STATEMENT
Given a collection of intervals, merge all overlapping intervals.

CLARIFICATIONS
- If two intervals touch on the boundary, are they considered overlapping? Yes.
- Are the intervals sorted in any way? Not necessarily.
- Are the intervals given as object instantiations of some class or an array of start and end?
  An object, define that too.

EXAMPLES
[1,3],[2,6],[8,10],[15,18] -> [1,6],[8,10],[15,18].

COMMENTS
- We should start with the leftmost interval possible. Let's sort the intervals by their start.
- Then we would iterate the list of intervals and merge until we get an interval whose start is
  at right of the current interval end.
- O(n log n) time complexity and O(n) space complexity, assuming in-place sort.
"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x.start)
        to_return = []
        current_interval = intervals[0]
        current_start = current_interval.start
        current_end = current_interval.end
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= current_end:
                current_end = max(current_end, interval.end)
            else:
                to_add = Interval()
                to_add.start = current_start
                to_add.end = current_end
                to_return.append(to_add)
                current_start = interval.start
                current_end = interval.end
        to_add = Interval()
        to_add.start = current_start
        to_add.end = current_end
        to_return.append(to_add)
        
        return to_return
