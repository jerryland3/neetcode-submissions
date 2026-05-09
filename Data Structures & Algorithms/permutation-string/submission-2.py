from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        match_count = 0
        s1_map = defaultdict(int)
        window_map = defaultdict(int)
        for char in s1:
            s1_map[char] += 1

        for right, char in enumerate(s2):
            if char in s1_map:
                window_map[char] += 1
                match_count += 1
                while window_map[char] > s1_map[char]:
                    window_map[s2[left]] -= 1
                    left += 1
                    match_count -= 1
            else:
                left = right + 1
                match_count = 0
                window_map = defaultdict(int)

            if match_count == len(s1):
                return True

        return False



"""
lecadacbee


"""