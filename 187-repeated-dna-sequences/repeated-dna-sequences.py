class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        store = set()
        for i in range(len(s) - 9):
            # print(s[i:i+10])
            seq = s[i:i + 10]
            if seq in store:        # appeared more than once
                res.add(seq)
            else:
                store.add(seq)      # add new sequences
        # print(store)
        return list(res)