class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[nums[0]]
        post=[nums[-1]]
        output=[]
        for i in range(1,len(nums)):
            pre.append(pre[i-1]*nums[i])
            post.insert(0,post[-i]*nums[-i-1])
        print(pre)
        print(post)
        output.append(post[1])
        for i in range(1,len(nums)-1):
            output.append(pre[i-1]*post[i+1])
        output.append(pre[-2])
        return output

