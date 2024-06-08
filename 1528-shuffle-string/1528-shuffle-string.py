class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [0] * len(s)

        for i in range(len(s)):
            char = s[i]
            correct = indices[i]
            result[correct] = char
        
        return ''.join(result)
