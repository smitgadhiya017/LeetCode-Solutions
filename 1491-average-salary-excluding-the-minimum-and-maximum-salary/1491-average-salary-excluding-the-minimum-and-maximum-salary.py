class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total = 0
        c = 0

        for i in range(1,len(salary)-1):
            total += salary[i]
            c += 1

        avg = total / c 

        return avg