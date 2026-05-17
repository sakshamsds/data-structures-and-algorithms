class Solution {
    public boolean canReach(int[] arr, int start) {
        // bfs
        // visited idxs
        // queue

        Deque<Integer> queue = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<>();
        queue.offerLast(start);

        while (!queue.isEmpty()) {
            int cur = queue.pollFirst();
            if (arr[cur] == 0) {
                return true;
            }
            int[] nbrs = new int[] {cur - arr[cur], cur + arr[cur]};
            for (int nbr : nbrs) {
                if (nbr < 0 || nbr > arr.length - 1 || visited.contains(nbr)) {
                    continue;
                }
                visited.add(nbr);
                queue.offerLast(nbr);
            }
        }

        return false;
    }
}