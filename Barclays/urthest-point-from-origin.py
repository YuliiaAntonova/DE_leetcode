# https://leetcode.com/problems/furthest-point-from-origin/description/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left_moves = moves.count('L')
        right_moves = moves.count('R')
        dash_moves = moves.count('_')
        return abs(left_moves - right_moves) + dash_moves

# Example usage:

solution = Solution()
print(solution.furthestDistanceFromOrigin("L_RL__R"))  # Output: 3
print(solution.furthestDistanceFromOrigin("RRLRL"))    # Output: 1     




