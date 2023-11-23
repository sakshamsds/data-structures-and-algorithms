# lee215 solution

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText)//rows
        res = []
        for i in range(cols):
            for j in range(i, len(encodedText), cols + 1):
                res.append(encodedText[j])
        return "".join(res).rstrip()