class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        head = 0
        tail = len(nums)
        output_list = []
        while tail - head > 1:
            for i in range(head+1, tail):
                if nums[head]+nums[tail - 1]+nums[i] == 0:
                    temp_list = [nums[head],nums[tail - 1],nums[i]]
                    temp_list.sort()
                    if not temp_list in output_list:
                        output_list.append(temp_list)
                        head += 1
                        tail -= 1
                        break
                elif nums[head]+nums[tail - 1]+nums[i] < 0:
                    head += 1
                elif nums[head]+nums[tail - 1]+nums[i] > 0:
                    tail -= 1
        return output_list

nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))