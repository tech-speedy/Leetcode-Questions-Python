class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        longest = 0

        # Iterating over the set directly skips duplicates in the outer loop
        for i in s:
            if i - 1 not in s:
                length = 1
                while i + length in s:
                    length += 1
                longest = max(longest, length)

        return longest