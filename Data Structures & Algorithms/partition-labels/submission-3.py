from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexDict = defaultdict(int)
        for index, char in enumerate(s):
            lastIndexDict[char] = index
        
        prevIndex = 0
        lastIndex = 0
        output = []
        for index, char in enumerate(s):
            lastIndex = max(lastIndex, lastIndexDict[char])
            if index == lastIndex:
                output.append(lastIndex - prevIndex + 1)
                prevIndex = index + 1
        
        return output
            
"""
given a string s
want to split the string into as many substring as possible, while ensure each letter apperas in at most one substring

return a list representing the size of the substring in order they appera.
-----------------------------------------------------------

            i
xyxxyzbzbbisl

prevIndex = 13
lastIndex = 13

size = lastIndex - prevIndex + 1
[5 5 1 1 1]

{
    x: 3
    y: 4
    z: 7
    b: 9
    i: 10
    s: 11
    l: 12
}

Complexity:
    - O(n) time since we need to loop through the string twice, once for hash table another for computing list values
    - O(1) aux space since lowercase english letter are O(26) for the hash table, O(1) output space since again
      the number of characters in the english character are O(26).

"""