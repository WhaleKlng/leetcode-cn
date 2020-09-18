# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。 
# 
#  你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。 
# 
#  返回获得利润的最大值。 
# 
#  注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。 
# 
#  示例 1: 
# 
#  输入:
# 输出: 8
# 解释: 能够达到的最大利润:  
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8. 
# 
#  注意: 
# 
#  
#  0 < prices.length <= 50000. 
#  0 < prices[i] < 50000. 
#  0 <= fee < 50000. 
#  
#  Related Topics 贪心算法 数组 动态规划 
#  👍 238 👎 0
from typing import List

prices = [1, 3, 2, 8, 4, 9]
fee = 2


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 0] for _ in range(n + 1)]
        dp[1][0] = 0
        dp[1][1] = -prices[1 - 1]
        for i in range(2, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1])
        return dp[-1][0]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maxProfit(prices, fee))
