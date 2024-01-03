class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows, cols = len(bank), len(bank[0])
        prev_devices, total_beams = 0, 0

        for r in range(rows):
            cur_devices = 0
            for c in range(cols):
                cur_devices += int(bank[r][c])
            if cur_devices > 0:
                total_beams += prev_devices * cur_devices
                prev_devices = cur_devices

        return total_beams