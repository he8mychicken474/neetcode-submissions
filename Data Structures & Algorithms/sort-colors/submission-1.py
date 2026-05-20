class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for n in nums:
            colors[n] += 1

        left = 0

        for j in range(len(colors)):
            for i in range(colors[j]):
                nums[left] = j
                left += 1
        
