class Solution {

    private static final List<int[]> DIRECTIONS = Arrays.asList(
        new int[] {-1, 0},
        new int[] {0, 1},
        new int[] {1, 0},
        new int[] {0, -1}
    );

    public void wallsAndGates(int[][] rooms) {
        // multi source bfs
        int rows = rooms.length;
        int cols = rooms[0].length;
        int EMTPY = Integer.MAX_VALUE;

        Queue<int[]> queue = new LinkedList<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (rooms[r][c] == 0) {
                    queue.add(new int[]{r, c});
                }
            }
        }
        
        while (!queue.isEmpty()) {
            int[] point = queue.poll();
            int r = point[0];
            int c = point[1];
            for (int[] direction : DIRECTIONS) {
                int nr = r + direction[0];
                int nc = c + direction[1];

                if (
                    nr < 0 || nr >= rows || nc < 0 || nc >= cols ||
                    rooms[nr][nc] != EMTPY
                ) {
                    continue;
                }
                rooms[nr][nc] = rooms[r][c] + 1;
                queue.add(new int[] {nr, nc});
            }
        }
    }
}