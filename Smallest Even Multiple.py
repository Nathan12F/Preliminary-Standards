class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        result = n if n % 2 == 0 else 2 * n
        return result
