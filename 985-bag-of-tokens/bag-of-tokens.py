class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
            elif r - l > 1 and score > 0:   # borrow power from the end if first cond not met
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return score