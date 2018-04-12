# -*- coding:utf-8 -*-

# This program is for Longest Palindrome Substring
#
# Input :
# s    str
#
# OUT :
# Palindrome Substring

def Palsub(s):
    assert type(s)==type('str'),'Please input a string'
    slen = len(s)
    dp = [[row == clo for clo in range(slen)] for row in range(slen)]
    maxlen = 1
    lps = []

    for j in range(slen):
        for i in range(j):    
            if j-i == 1:
                dp[i][j] = (s[i] == s[j])
                if dp[i][j] == True and maxlen <= 2:
                    lps.append(s[i:j+1])
                    maxlen = 2
            else:
                dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                if dp[i][j] == True and j + 1 - i >= maxlen:
                    lps.append(s[i:j+1])
                    maxlen = j + 1 - i
            
    if len(lps) == 0:
        print(s[0])
    else:
        print(lps[-1])



if __name__ == '__main__':
    Palsub('nooooon')
                
