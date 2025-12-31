class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5, count_10 = 0, 0

        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                if count_5 == 0:
                    return False
                count_5 -= 1
                count_10 += 1
            else:       # 20
                # case 1
                if count_10 > 0 and count_5 > 0:
                    count_10 -= 1
                    count_5 -= 1
                elif count_5 > 2:
                    count_5 -= 3
                else:
                    return False
            
        return True