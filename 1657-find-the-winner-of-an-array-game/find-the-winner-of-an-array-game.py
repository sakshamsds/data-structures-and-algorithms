class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current_winner = arr[0]
        wins = 0

        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                wins += 1
            else:
                current_winner = arr[i]
                wins = 1
            
            if wins == k:
                return current_winner
        
        return current_winner