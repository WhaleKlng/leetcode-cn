# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出
# 这个数字。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [0,1,3]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8 
# 
#  奇数长度时
# 
#  限制： 
# 
#  1 <= 数组长度 <= 10000 
#  Related Topics 数组 二分查找 
#  👍 51 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1  # [left,right]
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == mid:  # 前面不缺 要找的在后面
                left = mid + 1
            else:
                right = mid - 1
        return left
# leetcode submit region end(Prohibit modification and deletion)
