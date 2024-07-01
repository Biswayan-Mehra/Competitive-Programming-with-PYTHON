class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans = set()
        nums.sort()
        if len(nums) < 4:
            return ans
        for i in range(len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]:
                    continue
            for j in range(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                new_target = target - nums[i] - nums[j]
                while k < l:
                    if nums[k] + nums[l] == new_target:
                        ans.add(tuple([nums[i], nums[j], nums[k], nums[l]]))
                        k += 1
                        l -= 1
                    elif nums[k] + nums[l] < new_target:
                        k += 1
                    else:
                        l -= 1
        return ans

nums = [1,0,-1,0,-2,2]
target = 0
sol = Solution()
print(sol.fourSum(nums, target))