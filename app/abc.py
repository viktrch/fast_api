from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
        # for i, num in enumerate(nums):
        #     a = target - num
        #     if a in nums[i+1:]:
        #         return [i, nums.index(a, i+1)]
    return list(i + nums.index(target-num, i+1) for i, num in enumerate(nums) if target - num in nums[i+1:])

print(twoSum(nums=[2,7,11,15], target=9))

