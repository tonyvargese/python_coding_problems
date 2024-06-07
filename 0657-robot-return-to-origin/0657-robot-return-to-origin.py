class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ud=0
        lr=0
        for m in moves:
            if m=='U':
                ud+=1
            elif m=='D':
                ud-=1
            elif m=="L":
                lr+=1
            elif m=="R":
                lr-=1
        if ud==0 and lr==0:
            return True
        else:
            return False

        