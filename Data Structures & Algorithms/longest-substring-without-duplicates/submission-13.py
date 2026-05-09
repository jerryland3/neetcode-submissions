class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        tracker = set()
        for right, char in enumerate(s):
            if char in tracker:
                while char in tracker:
                    tracker.remove(s[left])
                    left += 1
            tracker.add(char)
            longest = max(longest, right - left + 1)
        return longest
        