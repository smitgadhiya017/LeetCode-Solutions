class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        c = 0
        r = 0
        for i in range(len(commands)):
            if commands[i] == "RIGHT":
                c += 1
            elif commands[i] == "LEFT":
                c -= 1
            elif commands[i] == "DOWN":
                r += 1
            else:
                r -= 1
        return (r * n) + c