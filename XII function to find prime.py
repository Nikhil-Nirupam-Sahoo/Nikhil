def prime(no):
    c=0
    for i in range(1,no+1):
        if no%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
#main
no=int(input('Enter a no:'))
s=prime(no)
print(s)
    
