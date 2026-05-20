class Solution:
    def sortArray(self, nums: List[int]) -> List[int]: 
        def rec(nums):
            if len(nums)==1:
                return nums
            a1 = nums[0:len(nums)//2]
            a2 = nums[len(nums)//2:]

            a1 =rec(a1)
            a2 = rec(a2)
            arr=[]
            i=0
            j=0
            while i<len(a1) and j<len(a2):
                if a1[i]<a2[j]:
                    arr.append(a1[i])
                    i+=1
                else:
                    arr.append(a2[j])
                    j+=1

            while i < len(a1):
                arr.append(a1[i])
                i += 1

            while j < len(a2):
                arr.append(a2[j])
                j += 1
            return arr
            
        x = rec(nums)
        return x
