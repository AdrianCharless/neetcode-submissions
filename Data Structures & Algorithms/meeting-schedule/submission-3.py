"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        sortInts = sorted(intervals, key=lambda x: x.start)
        end = sortInts[0].start
        print(end)
        for interval in sortInts:
            if interval.start < end:
                return False
            else:
                end = interval.end
            
        return True
            