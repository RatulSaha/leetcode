"""
STATEMENT
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

CLARIFICATIONS
- I am assuming there is no redundant duplicate in the list? Sure.
- Can the list be empty? No.
- I am assuming the list is not sorted? Sure.
- Should I return the lines, or the 'area' of water? The area is fine.

EXAMPLES
[2, 11, 13, 9] -> 18 (9*2, for lines [11,9])

COMMENTS
- We can try with the widest container and move the lines in if that gives a container with more area.
- Both the minimum height among the lines and the width matter, so we can keep the current area.
- O(n) time complexity and constant space complexity.
- Unless the list is sorted, I don't see any way to improve the complexity.
"""

def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        area_so_far = 0
    	while left < right:
    		h = min(height[left], height[right])
    		area_so_far = max(area_so_far, (right-left)*h)
    		while (height[left] <= h and left < right):
    			left += 1
    		while (height[right] <= h and left < right):
    			right -= 1
    	return area_so_far
