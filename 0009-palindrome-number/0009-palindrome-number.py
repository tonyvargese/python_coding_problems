class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reversed_sum=0
        temp=x
        while temp !=0:
            digit=temp%10

            reversed_sum = reversed_sum*10 + digit 
            temp//=10
        return reversed_sum==x


        

         
        