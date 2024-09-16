'''
17:22
07:21
'''

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # sort
        # check right, check diff between first and last 

        timePoints.sort()
        min_mins = 24 * 60

        def getMinutesDiff(t1, t2):
            h1, m1 = map(int, t1.split(':'))
            h2, m2 = map(int, t2.split(':'))
            return (h2 - h1) * 60 + m2 - m1

        for i in range(0, len(timePoints) - 1):
            min_mins = min(
                min_mins, 
                getMinutesDiff(
                    timePoints[i], 
                    timePoints[i + 1]
                )
            )

        # last check
        h0, m0 = map(int, timePoints[0].split(':'))

        return min(
            min_mins, 
            getMinutesDiff(timePoints[-1], "24:00") + h0 * 60 + m0
        )