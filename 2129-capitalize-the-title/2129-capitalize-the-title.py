class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=title.split()
        o=""

        for i in l:
            
            if len(i)<=2:
                for j in i:
                    if 65<=ord(j)<=90:
                        p=ord(j) + 32
                        o=o+chr(p)
                    else:
                        o=o+j
            else:
                if 97<=ord(i[0])<=122:
                    p=ord(i[0])-32
                    o=o+chr(p)
                else:
                    o=o+i[0]
                
                for k in i[1:]:
                    if 65<=ord(k)<=90:
                        p=ord(k)+32
                        o=o+chr(p)
                    else:
                        o=o+k
            o=o+" "
        o=o.strip()
        return o
            