class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total=0
        count=0

        for num in nums:
            if num%3==0 and num%2==0:
                total+=num
                count+=1
        
        if count>0:
            avg=total//count
            return avg
        else:
            return 0


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total=0
        count=0
        
        for num in nums:
            if num%2==0 and num%3==0:
                total+=num
                count+=1
        if count>0:
            return total//count
        else:
            return 0