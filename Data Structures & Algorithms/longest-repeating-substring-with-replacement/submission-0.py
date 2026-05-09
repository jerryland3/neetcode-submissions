from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        result = 0
        max_freq = 0
        left = 0

        for right, character in enumerate(s):
            freq_map[character] += 1
            max_freq = max(max_freq, freq_map[character])

            # invalid window
            if (right - left + 1) - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1

            result = max(result, (right - left + 1))
            
        return result
"""
AAABABBBBBAB
k = 1

right = 11
freq_map = {
    A: 1
    B: 6
}
max_freq = 6
left = 5

window_length = 7
result = 7



A valid window is when every character within that window is the same and we used all k replacements.

target character within our window is the character that have the most occurance.

valid window:
    window length - frequency of target character <= k

window_length = right - left + 1
frequency_map = dict
"""