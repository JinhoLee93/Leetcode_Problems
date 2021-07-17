class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = s[::-1]
        win1 = 0
        maximum = 0
        
        for i in range(len(palindrome)):
