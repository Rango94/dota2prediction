data=open('traindata.txt')
rwin=0
dwin=0
rhwin=[]
dhwin=[]
for i in range(0,114):
    rhwin.append(rwin)
dhwin=rhwin.copy()
count=rhwin.copy()
tmp=rhwin.copy()
pr=[]
pd=[]
for line in data:
    line=line.split()
    if line[10]=='-1':
        rwin=rwin+1
        for i in range(0,5):
            rhwin[int(line[i])-1]=rhwin[int(line[i])-1]+1
        for i in range(5,10):
            tmp[int(line[i]) - 1] = tmp[int(line[i]) - 1] + 1
    if line[10]=='1':
        dwin=dwin+1
        for i in range(5,10):
            dhwin[int(line[i]) - 1] = dhwin[int(line[i]) - 1] + 1
        for i in range(0,5):
            tmp[int(line[i]) - 1] = tmp[int(line[i]) - 1] + 1
    for i in range(0,10):
        count[int(line[i]) - 1]=count[int(line[i]) - 1]+1
print(rhwin)
print(dhwin)
rwin=float(rwin/(rwin+dwin))
dwin=float(dwin/(rwin+dwin))
print(rwin)
print(dwin)
print(count)
for i in range(0,114):
    pr.append(float(rhwin[i]/rwin)*10)
    pd.append(float(dhwin[i]/dwin)*10)
print(pr)
print(pd)

for line in data:
    line=line.split()
    tpr=rwin
    tpd=dwin
    for i in range(0,10):
        if i<5:
            tpr=tpr*rhwin[int(line[i])-1]
        else:
            tpd=tpd*dhwin[int(line[i]-1)]