def mergelist(li1,li2):
    li3=[]
    for i in range(len(li1)):
        if li1[i]%2==0:
            li3.append(li1[i])
    for j in range(len(li2)):
        if li2[j]%2==0:
            li3.append(li2[j])
    for k in range(len(li1)):
        if li1[k]%2!=0:
            li3.append(li1[k])
    for l in range(len(li2)):
        if li2[l]%2!=0:
            li3.append(li2[l])
    print(li3)
    return
mergelist([12,25,88,1],[51,29,81,54,96])