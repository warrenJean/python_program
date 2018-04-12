# -*- coding:utf-8 -*-

# This program is for 0/1 knapsack problem
# Input :
# n    how many goods
# wi   weight
# vi   value
# W    total weight constraint

n = 4
W = 5
w = [2,1,3,2]
v = [3,2,4,2]

def rec():
    dp = [[0 for clo in range(W + 1)] for row in range(n + 1)]
    for i in range(n):
        for j in range(W+1):
            if j >= w[i]:
                dp[i+1][j] = max(dp[i][j],dp[i][j-w[i]] + v[i])
            else:
                dp[i+1][j] = dp[i][j]
            
    print(dp[n][W])
    print(dp)

if __name__ == '__main__':
    rec()
