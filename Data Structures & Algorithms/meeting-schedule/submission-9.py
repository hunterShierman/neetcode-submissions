"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sorted_list = sorted(intervals, key=lambda x: x.start)
        for n in sorted_list:
            print(n.start, n.end)

        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):

                # check for if the start time of end times fall within the range of the current meeting
                currentMeeting = sorted_list[i]
                nthMeeting = sorted_list[j]

                if nthMeeting.start < currentMeeting.end:
                    return False

                

        return True