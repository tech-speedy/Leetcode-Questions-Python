class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = {}
        n = len(nums)
        s = set()

        for i, num in enumerate(nums):
            h[num] = i
        
        for i in range(n):
            for j in range(i + 1, n):
                desired = -nums[i] - nums[j]
                if desired in h and h[desired] != i and h[desired] != j:
                    a, b, c = nums[i], nums[j], desired
                    if a > b: 
                        a, b = b, a
                    if b > c: 
                        b, c = c, b
                    if a > b: 
                        a, b = b, a
                    s.add((a, b, c))

        return [list(t) for t in s]