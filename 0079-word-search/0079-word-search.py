class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            # All characters have been found
            if index == len(word):
                return True

            # Check boundaries
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Check character
            if board[r][c] != word[index]:
                return False

            # Save the current character
            temp = board[r][c]

            # Mark the cell as visited
            board[r][c] = "#"

            # Search in four directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Restore the original character
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False