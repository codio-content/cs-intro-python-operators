def get_max(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return min(nums[0], get_max(nums[1:]))
      