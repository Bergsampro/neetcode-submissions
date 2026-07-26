class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        
        for n in nums:
            # If count is 0, we choose a new candidate
            if count == 0:
                res = n
            
            # Increment if matching candidate, decrement otherwise
            count += (1 if n == res else -1)
            
        return res