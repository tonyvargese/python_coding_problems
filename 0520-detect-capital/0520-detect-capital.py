class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap=False

        for i in word:
            if ord(i)<=90:
                cap=True
            else:
                cap=False
                break
        if cap:
            return True
        
        for i in range(1,len(word)):
            if ord(word[i])<97:
                return False
        return True