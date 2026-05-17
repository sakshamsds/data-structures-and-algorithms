class Solution {
    public boolean canReach(int[] arr, int start) {
        // bfs

        Deque<Integer> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[arr.length];
        queue.offerLast(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int cur = queue.pollFirst();
            if (arr[cur] == 0) {
                return true;
            }
            int[] nbrs = new int[] {cur - arr[cur], cur + arr[cur]};
            for (int nbr : nbrs) {
                if (nbr < 0 || nbr > arr.length - 1 || visited[nbr]) {
                    continue;
                }
                visited[nbr] = true;
                queue.offerLast(nbr);
            }
        }

        return false;
    }
}