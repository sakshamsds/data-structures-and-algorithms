class Solution {
    private List<List<String>> solutions;
    private Set<Integer> cols;
    private Set<Integer> pos_diag;
    private Set<Integer> neg_diag;
    private int N;
    private char[][] board;

    public List<List<String>> solveNQueens(int n) {
        solutions = new ArrayList<>();
        cols = new HashSet<>();
        pos_diag = new HashSet<>();
        neg_diag = new HashSet<>();
        N = n;
        board = new char[n][n];
        // fill in the board
        for (int r = 0; r < n; r++){
            Arrays.fill(board[r], '.');
        }
        backtrack(0);
        return solutions;        
    }

    private List<String> createBoard() {
        List<String> output = new ArrayList<>();
        for (int row = 0; row < N; row++) {
            output.add(new String(board[row]));
        }
        return output;
    }

    private void backtrack(int row) {
        if (row == N) {
            solutions.add(createBoard());
            return;
        }

        for (int col = 0; col < N; col++) {
            if (cols.contains(col) || 
                pos_diag.contains(row - col) || 
                neg_diag.contains(row + col)
            ) {
                continue;
            }
            cols.add(col);
            pos_diag.add(row - col);
            neg_diag.add(row + col);
            board[row][col] = 'Q';
            backtrack(row + 1);
            board[row][col] = '.';
            cols.remove(col);
            pos_diag.remove(row - col);
            neg_diag.remove(row + col);
        }

    }
}