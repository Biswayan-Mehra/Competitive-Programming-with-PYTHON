class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        temp_list = prices
        profit = 0
        while len(temp_list) > 1:
            min_val = min(temp_list)
            min_index = temp_list.index(min_val)
            if min_index != len(temp_list)-1:
                max_val = max(temp_list[min_index + 1:])
                net_profit = max_val - min_val
                if profit < net_profit:
                    profit = net_profit
                    if min_index == 1:
                        break
            temp_list = temp_list[:min_index]
        return profit

prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))