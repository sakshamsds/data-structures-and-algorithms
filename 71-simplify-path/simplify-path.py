class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for s in path.split('/'):
            if not s or s == '.':  
                continue
            elif s == '..':
                if res:
                    res.pop()
            else:
                res.append(s)
            # print(res)

        return '/' + '/'.join(res)
