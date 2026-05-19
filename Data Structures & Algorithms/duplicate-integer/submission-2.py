class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numssep = set()
        for i in nums:
            if i in numssep:
                return True
            
            numssep.add(i)
        return False