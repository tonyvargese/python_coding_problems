class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff],i]
            else:
                seen[nums[i]]=i
        return []
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)

        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []


        