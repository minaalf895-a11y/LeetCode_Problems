class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        elif n <= 999999:
            return (n - 1000 + 1)
        elif n <= 999999999:
            return 999000 + (n - 1000000 + 1) * 2
        elif n <= 999999999999:
            return 999000 + 1998000000 + (n - 1000000000 + 1) * 3
        elif n <= 999999999999999:
            return 999000 + 1998000000 + 2997000000000 + (n - 1000000000000 + 1) * 4
        else:
            previous_commas = 999000 + 1998000000 + 2997000000000 + 3996000000000000
            return previous_commas + (n - 1000000000000000 + 1) * 5
