class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while  j < k:
                if nums[i]+nums[j]+nums[k] == 0:
                    ans.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return ans

"""
nums = [-1,0,1,2,-1,-4]
nums = [-2,0,1,1,2]
"""

nums = [-2,0,1,1,2]
sol = Solution()
print(sol.threeSum(nums))
