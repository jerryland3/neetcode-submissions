class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for item in nums:
            if item in hash_set:
                return True
            
            hash_set.add(item)

        return False
        