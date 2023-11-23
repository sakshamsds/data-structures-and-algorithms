class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText)//rows
        # print('numCols', cols)

        mat = [encodedText[cols*r:cols*r + cols] for r in range(rows)]
        # print(mat)

        res = []
        for i in range(cols):
            for j in range(rows):
                r, c = j, j + i
                # print(r, c)
                res.append(mat[r][c])
                if c == cols - 1:
                    break

        i = 0
        for i in range(len(res) - 1, -1, -1):
            if res[i] != ' ':
                break

        # print(i)
        return "".join(res[:i + 1])