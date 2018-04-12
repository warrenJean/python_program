# -*- coding:utf-8 -*-

# This program is for LCS(longest Common Subsequence)
# Input :
# n    len of str1
# m    len of str2
# s    str1
# t    str2

n = 4
m = 4
s = 'abcd'
t = 'becd'

def LCS():
    dp = [[0 for col in range(m + 1)] for row in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    print(dp[n][m])
    print(dp)



if __name__ == '__main__':
    LCS()
