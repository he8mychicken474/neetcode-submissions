class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        n = len(nums)
        ans[0:n] = nums
        ans[n:2*n] = nums
        return ans
        