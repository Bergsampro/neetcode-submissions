class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = set(nums)
        sorted_uniques = sorted(list(unique_set))
        
        # Step 3: Copy elements back into the original list in-place
        for i in range(len(sorted_uniques)):
            nums[i] = sorted_uniques[i]
            
        return len(sorted_uniques)