class Solution:
    def countCommas(self, n: int) -> int:
        string = str(n)
        if n < 1000:
            return 0
        elif 1000<=n<=100000:
            return (n-1000+1)
        


