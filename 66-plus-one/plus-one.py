class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                break
            cur_sum = digits[i] + carry
            digits[i] = cur_sum % 10
            carry = cur_sum // 10
            
        if carry > 0:
            return [carry] + digits
        return digits
            

                
            