def subsequences(str1,str2):
    if len(str1)==0 or len(str2)==0:
        return ['']

    if str1[-1]==str2[-1]:
        x=subsequences(str1[:-1], str2[:-1])
        return [sub + str1[-1] for sub in x] + x
    else:
        subs1=subsequences(str1[:-1], str2)
        subs2=subsequences(str1, str2[:-1])
        return subs1 + subs2
    
    
str1="abcd"
str2="axbdc"
c=subsequences(str1,str2)
print(c)

                                                                                                                                                                                                                                        
