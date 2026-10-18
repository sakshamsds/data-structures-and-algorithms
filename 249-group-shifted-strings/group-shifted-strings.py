class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        groups = collections.defaultdict(list)
        
        for s in strings:
            encoding = []
            for c in s:
                encoded = ord(c) - ord(s[0])
                if encoded < 0:
                    encoded += 26
                encoding.append(encoded)
            groups[tuple(encoding)].append(s)

        return list(groups.values())
