class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)):
            if command[i] == '(' and command[i+1] == ')':
                ans += 'o'
            if command[i] == '(':
                continue
            if command[i] == ')':
                continue
            else:
                ans += command[i]

        return ans