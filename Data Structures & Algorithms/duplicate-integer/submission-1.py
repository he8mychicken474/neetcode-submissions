class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numssep = []
        for i in nums:
            if i in numssep:
                return True
            
            numssep.append(i)
        return False