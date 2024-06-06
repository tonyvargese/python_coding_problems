class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        a=nums[0]
        b=nums[n-1]
        max_=0
        curr=0

        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                curr=i
                if curr>max_:
                    max_=curr
        return max_










        