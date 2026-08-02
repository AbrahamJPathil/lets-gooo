class Solution:

    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        maxLeft = [0] * n
        maxRight = [0] * n

        # Build maxLeft array from left to right: O(n)
        current_max = 0
        for i in range(n):
            maxLeft[i] = current_max
            current_max = max(current_max, height[i])

        # Build maxRight array from right to left: O(n)
        current_max = 0
        for i in range(n - 1, -1, -1):
            maxRight[i] = current_max
            current_max = max(current_max, height[i])

        # Calculate trapped water: O(n)
        total_water = 0
        for i in range(n):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water > 0:
                total_water += water

        return total_water