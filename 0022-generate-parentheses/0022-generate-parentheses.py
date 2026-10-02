class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        results = []

        def backtrack(current_str: str, open_c: int, close_c: int):
            if len(current_str) == 2 * n:
                results.append(current_str)
                return

            if open_c < n:
                backtrack(current_str + "(", open_c + 1, close_c)

            if close_c < open_c:
                backtrack(current_str + ")", open_c, close_c + 1)

        backtrack("", 0, 0)
        return results