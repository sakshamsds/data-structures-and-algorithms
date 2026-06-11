class Solution {

    private static final int MOD = 1_000_000_007;

    public int assignEdgeWeights(int[][] edges) {
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        for (int[] edge : edges) {
            int start = edge[0];
            int end = edge[1];

            adjList.putIfAbsent(start, new ArrayList<>());
            adjList.putIfAbsent(end, new ArrayList<>());

            adjList.get(start).add(end);
            adjList.get(end).add(start);
        }

        Deque<Integer> queue = new ArrayDeque<>();
        queue.offerLast(1);
        Set<Integer> visited = new HashSet<>();
        visited.add(1);
        int depth = -1;

        while (!queue.isEmpty()) {
            depth++;
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                int currentNode = queue.pollFirst();
                for (int nbr : adjList.get(currentNode)) {
                    if (!visited.contains(nbr)) {
                        queue.offerLast(nbr);
                        visited.add(nbr);
                    }
                }
            }
        }

        // System.out.println(depth);

        long ans = 1;
        for (int i = 0; i < depth - 1; i++) {
            ans = (ans * 2) % MOD;
        }
        return (int) ans;
    }
}