class Solution:
    def countEven(self, num: int) -> int:
        count=0
        
        for i in range(1,num+1):
            temp=i
            s=0
            while temp>0:
                digit=temp%10
                s+=digit
                temp//=10
            if s%2==0:
                count+=1
        return count


        