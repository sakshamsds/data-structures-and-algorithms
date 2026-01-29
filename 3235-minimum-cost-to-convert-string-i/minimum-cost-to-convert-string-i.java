/*
b -> c = 10
b -> a -> c = 5

Floyd Warshall Algorithm
    a   b   c   d   e
a   0   2   
b       0   5    
c       5   0       1
d               0   20
e       2           0

abcd
acbe
*/

class Solution {
    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        long[][] dist = new long[26][26];
        for (int i = 0; i < 26; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
            dist[i][i] = 0;
        }

        int n = source.length();        // vertices
        int num_edges = original.length;        // edges
        for (int i = 0; i < num_edges; i++) {
            int src = original[i] - 'a';
            int dst = changed[i] - 'a';
            dist[src][dst] = Math.min(dist[src][dst], (long) cost[i]);
        }

        // Floyd Warshall
        for (int k = 0; k < 26; k++) {
            for (int src = 0; src < 26; src++) {
                for (int dst = 0; dst < 26; dst++) {
                    if (dist[src][dst] > dist[src][k] + dist[k][dst]) {
                        dist[src][dst] = dist[src][k] + dist[k][dst];
                    }
                }
            }
        }

        long min_cost = 0;
        for (int i = 0; i < n; i++) {
            int src = source.charAt(i) - 'a';
            int dst = target.charAt(i) - 'a';
            if (dist[src][dst] >= Integer.MAX_VALUE) {
                return -1;
            }
            min_cost += dist[src][dst];
        }

        // System.out.println(Arrays.deepToString(dist));
        return min_cost;
    }
}