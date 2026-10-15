
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])

                # Move to the next index because each number
                # can be used only once
                backtrack(i + 1, current, total + candidates[i])

                current.pop()

        backtrack(0, [], 0)
        return result
