class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int prevEnd = Integer.MIN_VALUE;
        for (int i = 0; i < intervals.length; i++) {
            int nextStart = intervals[i][0], nextEnd = intervals[i][1];
            if (nextStart < prevEnd) {
                return false;
            }
            prevEnd = nextEnd;
        }
        return true;
    }
}