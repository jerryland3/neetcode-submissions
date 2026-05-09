class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_data = list(zip(position, speed))
        car_data.sort(key=lambda x: x[0], reverse=True)

        # fleet_count = 0
        # highest_time = 0
        stack = []
        for position, speed in car_data:
            time = (target - position) / speed
            # if time > highest_time:
            #     fleet_count += 1
            #     highest_time = time
            if not stack or time > stack[-1]:
                stack.append(time)

        # return fleet_count
        return len(stack)

"""
[(1 1)]
2
"""   