def find(a,t):
    print('this',a[0])
    if a == []:
        return False
    if len(a) == 1:
        if int(a[0]) == t:
            return True
        else:    
            return False
    else:
        if int(a[0]) == t:
            return True
        else:    
            find(a[1:],t)
print(find([1,2,3,3,4,5],5))       
