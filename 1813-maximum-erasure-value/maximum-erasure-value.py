class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])

        indices_map = collections.defaultdict(int)      # window num -> idx mapping
        indices_map[nums[0]] = 0

        l, mx_score = 0, nums[0]
        for r in range(1, len(nums)):
            cur = nums[r]
            if cur in indices_map:
                l = max(l, indices_map[cur] + 1)
            # if cur in indices_map:
            #     if indices_map[cur] < l:
            #         indices_map.pop(cur)
            #     else:
            #         l = indices_map[cur] + 1
            indices_map[cur] = r            
            # print(l, r, prefix_sum[r] - prefix_sum[l] + nums[l])
            mx_score = max(mx_score, prefix_sum[r] - prefix_sum[l] + nums[l])

        return mx_score


