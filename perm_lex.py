def perm_gen_lex(a):
    
    if  len(a) <= 0:
        return ''
    elif len(a)==1:
        return a
    
    newList = []
    for x in range(len(a)):
        temp = list(a)
        temp.pop(x)
        newList.append(str(a[x])+perm_gen_lex("".join(temp)))
    return newList

 

