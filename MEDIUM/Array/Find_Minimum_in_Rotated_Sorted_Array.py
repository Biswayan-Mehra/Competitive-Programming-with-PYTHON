'''
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
'''

# Code
class Solution:
    def findMin(self, nums: list[int]) -> int:
        return min(nums)

sol = Solution()
nums = [4,5,6,7,0,1,2]
print(sol.findMin(nums))
