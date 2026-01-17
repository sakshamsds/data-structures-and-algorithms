class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int removals = 0;
        int prevEnd = Integer.MIN_VALUE;
        for (int i = 0; i <intervals.length; i++) {
            int nextStart = intervals[i][0];
            int nextEnd = intervals[i][1];

            if (prevEnd <= nextStart) {     // no overlap
                prevEnd = nextEnd;
            } else {
                removals++;
                prevEnd = Math.min(prevEnd, nextEnd);
            }
        }
        return removals;
    }
}