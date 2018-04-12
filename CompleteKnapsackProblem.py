# -*- coding:utf-8 -*-

# This program is for Complete Knapsack Problem
#
# Input :
# n    how many goods
# wi   weight
# vi   value
# W    total weight constraint
#
# OUT :
# Max value


def rec():
    n = 3
    W = 7
    w = [3,4,2]
    v = [4,5,3]
    dp = [[0 for clo in range(W + 1)] for row in range(n + 1)]

    for i in range(n):
        for j in range(W+1):
            if j >= w[i]:
                dp[i+1][j] = max(dp[i][j],dp[i + 1][j-w[i]] + v[i])
            else:
                dp[i+1][j] = dp[i][j]
            
    print(dp[n][W])
    print(dp)


def large():
    '''
    when W is very large, then O(nW) is too big
    '''
    n = 4
    W = 5
    w = [2,1,3,2]
    v = [3,2,4,2]
    dp = [[0 for clo in range(3*5 + 1)] for row in range(n + 1)]
    dp[0][1:] = [float('inf') for i in range(3*5)]

    for i in range(n):
        for j in range(3*5 + 1):
            if j < v[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = min(dp[i][j],dp[i][j-v[i]]+w[i])

    
    print([i for i in range(3*5+1) if dp[n][i] <= W][-1])
    print(dp)
  



if __name__ == '__main__':
    rec()
    large()
