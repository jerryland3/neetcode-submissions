class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        longest = 0
        consecutive_count = 1

        if len(sorted_nums) == 0:
            return longest

        prev_num = sorted_nums[0]
        for cur_num in sorted_nums:
            if cur_num == prev_num:
                continue
            
            if cur_num == prev_num + 1:
                consecutive_count += 1
            else:
                longest = max(longest, consecutive_count)
                consecutive_count = 1
            
            prev_num = cur_num

        return max(longest, consecutive_count)


"""
[1, 2, 5, 6, 7]

longest_sequence = 0


"""