class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int n = intervals.length, i = 0;
        int ns = newInterval[0], ne = newInterval[1];
        List<int[]> res = new ArrayList<>();

        // before new interval
        while (i < n && intervals[i][1] < ns) {
            res.add(intervals[i]);
            i++;
        }

        // merging
        while (i < n && intervals[i][0] <= ne) {
            ns = Math.min(ns, intervals[i][0]);
            ne = Math.max(ne, intervals[i][1]);
            i++;
        }
        res.add(new int[]{ns, ne});

        // after new interval
        while (i < n){
            res.add(intervals[i]);
            i++;
        }

        return res.toArray(new int[res.size()][]);
    }
}