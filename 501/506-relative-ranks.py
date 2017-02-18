"""
STATEMENT
Given scores of N athletes, find their relative ranks and the people with the top three highest scores,
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

CLARIFICATIONS
- Are the scores unique? Yes.
- Are the scores bounded by some value? Not necessarily.
- Do I need to output the rank of those from 4th position onwards? Yes.

EXAMPLES
[5, 4, 3, 2, 1] -> ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

COMMENTS
- Since the scores are not bounded by any upper limit, it'd be hard, if not impossible,
  to improve time complexity than O(n log n).
- If space complexity is not an issue,
  we can store an array of (score, index), and then sort that array by score.
- Then we can build the output array based on the sorted by score array, but pulling out
  the elements by the index.
- We can "try" to put the medal information for top three. If the size of the list is less than three,
  it will raise an IndexError, in which case we can simply pass.
"""

def findRelativeRanks(nums):
      """
      :type nums: List[int]
      :rtype: List[str]
      """
      n = len(nums)
      if not n:
          return nums
      indexed_arr = [(nums[i],i) for i in range(n)]
      indexed_arr.sort(reverse=True,key=lambda x:x[0])
      to_return = [0 for _ in range(n)]
      for i in range(n):
          (score,index) = indexed_arr[i]
          to_return[index] = str(i+1)
      try:
          to_return[indexed_arr[0][1]] = "Gold Medal"
          to_return[indexed_arr[1][1]] = "Silver Medal"
          to_return[indexed_arr[2][1]] = "Bronze Medal"
      except IndexError:
          pass
      return to_return
