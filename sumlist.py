def sumlist(li,r,c):
    se=so=0
    for i in range(r):
        for j in range(c):
            if li[i][j] % 2 == 0:
                se += li[i][j]
            else:
                so += li[i][j]
    print("Sum of even numbers:", se)
    print("Sum of odd numbers:", so)
    return
#main
li=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
for l in range(r):
    new=[]
    for k in range(c):
        no=int(input("Enter number: "))
        new.append(no)
    li.append(new)
print("The list is:", li)
sumlist(li,r,c)