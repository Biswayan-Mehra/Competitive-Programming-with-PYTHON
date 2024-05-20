class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i==0:
            nums[:] = nums[:][::-1]
            print(nums)
            return
        j = len(nums) - 1
        min = -1
        while j > i - 1 and min<1:
            min = nums[j] - nums[i-1]
            j -= 1
        nums[i-1],nums[j+1] = nums[j+1],nums[i-1]
        nums[i:] = nums[i:][::-1]
        print(nums)

sol = Solution()
"""
[5,4,7,5,3,2]  -----> [5,5,2,3,4,7]
[4,2,0,2,3,2,0] ----> [4,2,0,3,0,2,2]
[2,2,0,4,3,1]  -----> [2,2,1,0,3,4]
"""
nums = [4,2,0,2,3,2,0]
sol.nextPermutation(nums)
