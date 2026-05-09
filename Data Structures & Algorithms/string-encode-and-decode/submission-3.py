class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            count = len(string)
            result += (str(count) + "#" + string)
        
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            count = ""
            while s[index] != "#":
                count += s[index]
                index += 1
            string = ""
            for _ in range(int(count)):
                index += 1
                string += s[index]
            
            result.append(string)
            index += 1

        return result



"""
[we, say, :, yes, !@#$%^&*()]

2#we3#say1#:3#yes10#!@#$%^&*()

"""