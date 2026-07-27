class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numy=[]
        for i in nums:
            if i != val:
                numy.append(i)
        for i in range(len(numy)):
                 nums[i]=numy[i]
        return len(numy)   