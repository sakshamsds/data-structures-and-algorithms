class Solution {
    public int minJumps(int[] arr) {
        // idx -> idxes
        Map<Integer, List<Integer>> idxMap = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            idxMap.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }
        
        // bfs
        boolean[] visited = new boolean[arr.length];
        Deque<Integer> queue = new ArrayDeque<>();
        visited[0] = true;
        queue.offerLast(0);
        int steps = 0;
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                int curIdx = queue.pollFirst();
                if (curIdx == arr.length - 1) return steps;

                if (idxMap.containsKey(arr[curIdx])) {
                    for (int nbr : idxMap.get(arr[curIdx])) {
                        if (!visited[nbr]) {
                            visited[nbr] = true;
                            queue.offerLast(nbr);
                        }
                    }
                    idxMap.remove(arr[curIdx]);
                }

                if (curIdx + 1 < arr.length && !visited[curIdx + 1]) {
                    visited[curIdx + 1] = true;
                    queue.offerLast(curIdx + 1);
                }

                if (curIdx - 1 >= 0 && !visited[curIdx - 1]) {
                    visited[curIdx - 1] = true;
                    queue.offerLast(curIdx - 1);
                }
            }
            steps += 1;
        }

        return -1;
    }
}