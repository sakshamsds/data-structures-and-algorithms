class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        handSize = len(hand)
        if handSize % groupSize != 0:
            return False

        count = collections.Counter(hand)
        freqsHeap = []
        for card, freq in count.items():
            freqsHeap.append((card, freq))
        heapq.heapify(freqsHeap)

        while freqsHeap:
            tmpFreqs = []
            prevCard = None
            for _ in range(groupSize):
                if not freqsHeap:       # consecutive element does not exists
                    return False
                curCard, freq = heapq.heappop(freqsHeap)
                if prevCard is not None and prevCard + 1 != curCard:
                    return False
                if freq > 1:
                    tmpFreqs.append((curCard, freq - 1))
                prevCard = curCard

            for card, freq in tmpFreqs:
                heapq.heappush(freqsHeap, (card, freq))

        return True