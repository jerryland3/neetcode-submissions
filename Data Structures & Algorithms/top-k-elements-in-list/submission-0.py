from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for number in nums:
            frequency[number] += 1

        occurrence_list = [[] for index in range(len(nums) + 1)]
        for number, occurrences in frequency.items():
            occurrence_list[occurrences].append(number)

        results = []
        for element in reversed(occurrence_list):
            for number in element:
                results.append(number)
                k -= 1

                if k == 0:
                    return results

        

        