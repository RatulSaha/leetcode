"""
STATEMENT
The Hamming distance between two integers is the number of positions
at which the corresponding bits are different. Find the total
Hamming distance between all pairs of the given numbers.

CLARIFICATIONS
- The numbers are given as positive integers? Yes.

EXAMPLES
[4, 14, 2] -> 6

COMMENTS
- The naive solution is to do n choose 2 XOR operations.
- A better solution is to keep a cache of XOR operations of the first element
  and the rest of the elements. The idea is to use the result
  XOR(XOR(a,b), XOR(b,c)) = XOR(a,c). The space complexity is O(n) and time 
  complexity is O(n^2)
- An even better solution is to use the very nifty trick that i-th position in
  the result is the combinations of ways to choose two values from the i-th
  positions in all the values (constant space complexity and linear time
  complexity).
"""

def totalHammingDistance(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = map(lambda x: bin(x)[2:].zfill(32), nums)
        to_return = 0
        for i in range(32):
            zero_count, one_count = 0, 0
            for num in nums:
                if num[i] == '0':
                    zero_count += 1
                else:
                    one_count += 1
            to_return += zero_count*one_count
        return to_return

def totalHammingDistance(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        n, to_return = len(nums), 0
        cache = [0 for _ in range(n)]

        for i in range(n):
            cache[i] = nums[i]^nums[0]
            to_return += bin(cache[i]).count("1")

        for i in range(1,n):
            for j in range(i+1,n):
                to_return += bin(cache[i]^cache[j]).count("1")
        return to_return
