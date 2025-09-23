class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')

        i = 0
        while i < len(revisions1) or i < len(revisions2):
            rev1 = int(revisions1[i]) if i < len(revisions1) else 0
            rev2 = int(revisions2[i]) if i < len(revisions2) else 0

            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
            i += 1

        return 0