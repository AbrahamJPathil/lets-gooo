class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = set()
        for i in range(len(position)):
            time.add((target-position[i])/speed[i])
        
        return len(time)