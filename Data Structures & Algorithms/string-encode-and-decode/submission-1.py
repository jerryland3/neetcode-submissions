class Solution:

    def encode(self, strs: List[str]) -> str:
        output_str = ""
        for string in reversed(strs):
            str_length = len(string)
            for char in reversed(string):
                output_str += char
            
            output_str += "#"
            for char in reversed(str(str_length)):
                output_str += char
        
        return output_str

    def decode(self, s: str) -> List[str]:
        results = []
        str_stack = list(s)

        while len(str_stack) > 0:
            number = ""
            while True:
                num_char = str_stack.pop()
                if num_char == "#":
                    break
                number += num_char
            
            number = int(number)
            string = ""
            for _ in range(number):
                string += str_stack.pop()
            
            results.append(string)

        return results


"""
["neettttttt", "code", "love", "you"]

str = 4neet4code4love3you

str_stack = [u, o, y, #, 3, e, v, o, l, #, 4, e, d, o, c, #, 4, t, t, t, t, t, t, t, e, e, n, # , 0, 1]

while str_stack is not empty:
    number = str_stack.pop()
    string = ""
    for _ in range(number):
        string += str_stack.pop()

    results.appen(string)


m = number of characters
n = number of string

Time complexity
encode - O(m)
decode - O(n + m)

Space complexity
encode - O(n + m)
decode - O(m)
"""