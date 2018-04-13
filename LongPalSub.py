# -*- coding:utf-8 -*-

# This program is for Longest Palindrome Substring
#
# Input :
# s    str
#
# OUT :
# Palindrome Substring

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        assert type(s)==type('str'),'Please input a string'

        slen = len(s)
        if slen == 0:
            return 0
        
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
            return s[0]
        else:
            return lps[-1]
        

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            s = next(lines)
            
            out = Solution().longestPalindrome(s)
            if out == 0:
                break

            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
                
