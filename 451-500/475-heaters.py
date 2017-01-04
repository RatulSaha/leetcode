"""
STATEMENT
Given positions of houses and heaters on a horizontal line,
find out minimum radius of heaters so that all houses could be covered by those heaters.

CLARIFICATIONS
- The radius that needs to be found would be universal for all heaters? Yes.
- Is there a bound on range of houses/heaters? The number will be less than 25000 and the positions below 10^9.
- Is the list of positions sorted? Let's start with that they are not sorted.

EXAMPLES
(house list, heater list)
[1,2,3], [2] -> 1
[1,2,3,4], [1,4] -> 1

COMMENTS
- We should start with sorting the list of heaters.
- For each house, we can find the closest heater by binary search on the sorted list of heaters.
- We'd keep a minimum radius so far, and the current radius for the heater.
- The global minimum radius has to be definite small, so we can do float("-inf") or if the positions are non-negative, -1.
- The time complexity is O (n log n + n log m) in terms of size of the heater list (n) and house list (m).
"""

def findRadius(houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if not heaters or not houses:
            return 0
        heaters.sort()
        min_radius = -1

        for house in houses:
            radius_so_far = abs(heaters[0]-house)
            start, end = 0, len(heaters)-1
            while start <= end:
                mid = (start+end)/2
                current_radius = abs(heaters[mid]-house)
                if current_radius < radius_so_far:
                    radius_so_far = current_radius
                if not current_radius:
                    break
                else:
                    if house < heaters[mid]:
                        end = mid-1
                    else:
                        start = mid+1
            if min_radius < radius_so_far:
                min_radius = radius_so_far
        return min_radius
