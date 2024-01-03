class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices_per_row = []
        rows, cols = len(bank), len(bank[0])
        for r in range(rows):
            num_devices = 0
            for c in range(cols):
                num_devices += int(bank[r][c])
            devices_per_row.append(num_devices)

        prev, total_beams = 0, 0
        for devices in devices_per_row: 
            if devices > 0:
                total_beams += prev * devices
                prev = devices
        return total_beams