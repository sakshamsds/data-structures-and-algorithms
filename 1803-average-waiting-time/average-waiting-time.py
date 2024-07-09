class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        freeT = 0
        totalT = 0
        for arrivalT, cookingT in customers:
            freeT = max(freeT, arrivalT)
            freeT += cookingT
            totalT += freeT - arrivalT
        return totalT / len(customers)
             