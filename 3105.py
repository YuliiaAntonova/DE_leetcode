# Example 1:
#
# Input: nums = [1,4,3,3,2]
#
# Output: 2
#
# Explanation:
#
# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
#
# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
#
# Hence, we return 2.

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        max_len = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                inc += 1
                dec = 1

            elif nums[i - 1] > nums[i]:
                dec += 1
                inc = 1

            else:
                inc = 1
                dec = 1

            max_len = max(max_len, inc, dec)

        return max_len

res = Solution().longestMonotonicSubarray(nums=[1, 4, 3, 2, 1])
