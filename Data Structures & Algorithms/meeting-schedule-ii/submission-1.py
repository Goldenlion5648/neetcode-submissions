"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


   |==========|
|======|

|============|
    |=============|
                |============|

    |==================|
        |============|
           |=====|
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        interest = []
        for inter in intervals:
            interest.append((inter.start, 1))
            interest.append((inter.end, -1))
        
        highest = 0
        interest.sort()
        cur = 0
        pos = 0
        while pos < len(interest):
            cur += interest[pos][1]
            highest = max(highest, cur)
            pos += 1
        return highest
            





















