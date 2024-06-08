class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range (0,num//4+1):
            if i*i==num:
                return True
        return False
        

        
        
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        y=int(num**0.5)
        return num==(y)*(y)