from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        table = dict()
        min_cards = float("inf")
        
        for i in range(len(cards)):
            card = cards[i]
            if card in table:
                min_cards = min(min_cards, i - table[card] + 1)
            table[card] = i
                
        return min_cards if min_cards != float("inf") else -1
            
        
        