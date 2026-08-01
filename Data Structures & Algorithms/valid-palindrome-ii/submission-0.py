class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Option 1: Delete the left character by skipping it
                skip_left = s[left + 1 : right + 1]
                
                # Option 2: Delete the right character by skipping it
                skip_right = s[left:right]
                
                # Check if reversing either option produces a match
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            
            left += 1
            right -= 1
            
        return True