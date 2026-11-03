'''
|=====|
    |=====|

        |=====|
    |=====|

|=============|
    |=====|

    |=====|
|=============|
'''

class MyCalendar:
    
    def __init__(self):
        self.times = []

    def book(self, startTime: int, endTime: int) -> bool:
        gone_through = []
        did_append = False

        for i in range(len(self.times)):
            old_start, old_end = self.times[i]
            if startTime in range(old_start, old_end) or old_start in range(startTime, endTime):
                return False
                
            gone_through.append([old_start, old_end])
            should_insert = False
            if i + 1 < len(self.times):
                after_start, after_end = self.times[i+1]
                if startTime >= old_end and endTime <= after_start:
                    should_insert = True
            else:
                should_insert = True
            if should_insert:
                gone_through.append([startTime, endTime])
                self.times = gone_through + self.times[i+1:]
                return True
        self.times.append([startTime, endTime])
        return True








# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)