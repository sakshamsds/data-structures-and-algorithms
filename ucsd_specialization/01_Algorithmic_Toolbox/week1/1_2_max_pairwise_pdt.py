def get_max_pairwise_pdt(nums):
    first, second = 0, 0
    for number in nums:
        if number > first:
            first, second = number, first
        elif number > second:
            second = number
    return first * second

    # max_num, max_idx, second_max_num = -1, -1, -1

    # for i in range(len(nums)):
    #     if nums[i] > max_num:
    #         max_num = nums[i]
    #         max_idx = i

    # for i in range(len(nums)):
    #     if nums[i] > second_max_num and i != max_idx:
    #         second_max_num = nums[i]
        
    # return max_num * second_max_num


# def get_max_pairwise_pdt(n, nums):
#     max_pdt = 0
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             max_pdt = max(max_pdt, nums[i] * nums[j]) 
#     return max_pdt

if __name__ == "__main__":
    _ = int(input())
    nums = list(map(int, input().split()))
    print(get_max_pairwise_pdt(nums))
