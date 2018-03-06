fo=open('class.txt')
fo1=open('herosmark.txt')
fo2=open('mark.txt','w')
# baofa=[]
# kongzhi=[]
# naijiu=[]
# taosheng=[]
# tuijin=[]
# xianshou=[]
# heixin=[]
# fuzhu=[]
# tuanzhan=[]
tmp=[]
mex=[]
k=0
n=0
for i in range(0,114):
    tmp.append(0)
for i in range(0,9):
    mex.append(tmp.copy())
print(mex)
for line in fo:
    line=line.split()
    for i in line:
        if k==0:
            mex[n][int(i)-1]=1.5
        if k==1:
            mex[n][int(i)-1]=1
        if k==2:
            mex[n][int(i)-1]=0.5
    if k<2:
        k=k+1
    else:
        k=0
        n=n+1
print(len(mex[1]))
for line in fo1:
    line=line.split()
    print(len(line))
    count=0
    for i in line:
        count=count+float(i)
    count=float(count/113)
    for i in range(0,114):
        line[i]=(float(line[i])/count)
    mex.append(line)
for i in range(len(mex)):
    for j in mex[i]:
        fo2.write(str(j)+' ')
    fo2.write('\n')
fo.close()
fo1.close()
