# https://leetcode.com/problems/contiguous-array/description/
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # "balance" stores the difference between the number of 1s and 0s.
        # We treat:
        #   1 -> +1
        #   0 -> -1
        balance = 0

        # Stores the maximum length of a valid subarray found so far.
        max_len = 0

        # Dictionary that stores the FIRST index where each balance occurred.
        #
        # Example:
        # balance = 2 first appears at index 5
        # first_seen = {2: 5}
        #
        # We initialize balance 0 at index -1.
        # This represents the prefix BEFORE the array starts.
        # It allows us to correctly handle subarrays that begin at index 0.
        first_seen = {0: -1}

        # Traverse the array once.
        for i in range(len(nums)):

            # Update the running balance.
            # 1 increases the balance.
            # 0 decreases the balance.
            if nums[i] == 1:
                balance += 1
            else:
                balance -= 1

            # If we have seen this balance before,
            # then the subarray between the previous index
            # and the current index contains an equal number
            # of 0s and 1s.
            if balance in first_seen:

                # Compute the length of this valid subarray.
                current_len = i - first_seen[balance]

                # Update the maximum length.
                max_len = max(max_len, current_len)

            else:
                # Store ONLY the first occurrence of this balance.
                # Keeping the earliest index guarantees the longest
                # possible subarray when the same balance appears again.
                first_seen[balance] = i

        # Return the longest valid subarray.
        return max_len



res =  Solution().findMaxLength([0,1, 0])
res1 = Solution().findMaxLength([0,1,0])
res2 = Solution().findMaxLength([0,1,1,1,1,1,0,0,0])
res3 = Solution().findMaxLength([0,1])
print(res)
print(res1)
print(res2)
print(res3)
