class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numssep = []
        for i in nums:
            if i not in numssep:
                numssep.append(i)
        if numssep == nums:
            return False
        else:
            return True