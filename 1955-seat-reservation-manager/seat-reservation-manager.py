class SeatManager:

    def __init__(self, n: int):
        # heap of unreserved seats
        # all seats are unreserved initially
        self.available = [i for i in range(1, n + 1)]
        heapq.heapify(self.available)

    def reserve(self) -> int:
        # get the min from available
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)