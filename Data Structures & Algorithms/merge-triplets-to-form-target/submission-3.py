class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result =[0, 0, 0]
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                result[0] = max(result[0], a)
                result[1] = max(result[1], b)
                result[2] = max(result[2], c)
        
        return result == target


"""
triplet[i] = [ai bi ci]
target = [x y z]

can merge two triplet by taking their maxes

Return True if its possible to form target by merging triplets, or False if we cannot

[2 5 6]
[1 4 4]
[5 7 5]

result = [1 4 4]

target = [5 4 6]



Strategy:
    - A triplet would not work if any of its values are greater than its corresponding value in target
    - We go through the list and merge all triplet that have values less than or equal to its corresponding value
      in target
    - at the end we can check if the resulting merged triplet matches target

Complexity:
    - O(n) time since we loop through triplets once
    - O(1) aux and output space since we are not using extra data structure
"""
