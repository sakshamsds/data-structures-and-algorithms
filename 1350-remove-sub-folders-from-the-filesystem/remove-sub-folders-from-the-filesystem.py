class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        folder.sort()
        res.append(folder[0])

        def isParentfolder(d1, d2):
            d1 = d1.split('/')[1:]
            d2 = d2.split('/')[1:]
            for i in range(len(d1)):
                if d1[i] != d2[i]:
                    return False
            return True

        for i in range(1, len(folder)):
            if not isParentfolder(res[-1], folder[i]):
                res.append(folder[i])
        return res