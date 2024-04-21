def vowel(s):
    curr_length=0
    max_length=0
    start_index=0
    sequence=''
    vowel=['a','e','i','o','u']

    for i in range(len(s)):
        char=s[i]
        if char in vowel:
            curr_length+=1
            if curr_length>max_length:
                max_length=curr_length
                start_index=i-curr_length+1
                sequence=s[start_index:start_index+max_length]
        else:
            curr_length=0
    
    if max_length==0:
        return 'No vowel'
    else:
        return sequence
    
s=input()
print(vowel(s))