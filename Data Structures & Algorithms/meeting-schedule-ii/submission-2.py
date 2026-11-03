"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

|============|
  |========|
      |==|

      |==|
  |========|
|============|

ending time this is the way to go
|====|
       |==|
   |=======|
  |=========|
 |==============|

2 rooms works
|=|
 |====|
    |================|
           |=======|
sort by starting time
and go from the end, checking start time for conflicts


starting time
|====|
 |==============|
  |=========|
   |=======|
       |==|

"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = defaultdict(int)
        for interval in intervals:
            times[interval.start] += 1
            times[interval.end] -= 1
        interest = sorted(times.keys())
        hi = 0
        cur = 0
        for time in interest:
            cur += times[time]
            hi = max(hi, cur)

        return hi

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        