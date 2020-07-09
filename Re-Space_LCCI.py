class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dp = [inf] * (len(sentence) + 1)
        dp[0] = 0
        for i in range(1, len(sentence) + 1):
            dp[i] = dp[i - 1] + 1
            for word in dictionary:
                if ((i - len(word)) >= 0) and (word == sentence[i - len(word): i]):
                    dp[i] = min(dp[i], dp[i - len(word)])
        return dp[len(sentence)]
