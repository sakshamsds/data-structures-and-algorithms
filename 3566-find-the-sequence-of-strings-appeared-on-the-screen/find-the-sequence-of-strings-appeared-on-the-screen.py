class Solution:
    def stringSequence(self, target: str) -> List[str]:
        cur, res = [], []
        for i in range(len(target)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                cur.append(c)
                res.append(''.join(cur))
                if c == target[i]:
                    break
                else:
                    cur.pop()
        return res