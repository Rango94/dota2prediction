def prior(data,result):
    count=0
    for item in data:
        if item[114]==result:
            count +=1
    return float(count/len(data))

def posterior(data,ai,i,result):
    count1=0
    count2=0
    for item in data:
        if item[114]==result:
            count1 +=1
            if item[i]==ai:
                count2 +=1
    return float(count2/count1)

def calculateprobability(datatrain,datatest,bayes):
    count=0
    for item in datatest:
        pradiant=prior(datatrain,'-1')
        pdire=prior(datatrain,'1')
        for i in range(0,len(item)-1):
            if item[i]==0:
                pradiant*=bayes[4][i]
                pdire *=bayes[5][i]
            elif item[i]=='1':
                pradiant *=bayes[0][i]
                pdire *= bayes[2][i]
            elif item[i]=='-1':
                pradiant *= bayes[1][i]
                pdire *= bayes[3][i]
            # pradiant *=posterior(datatrain,item[i],i,'-1')
            # pdire *=posterior(datatrain,item[i],i,'1')
        radiant=pradiant/(pradiant+pdire)
        dire=pdire/(pradiant+pdire)
        print(radiant)
        print(dire)
        if radiant>dire and item[114]=='-1':
            count +=1
        if radiant<=dire and item[114]=='1':
            count +=1
        # print(count)
    return count/len(datatest)

data=open('cleardatabig8888.txt')
datata=[]
datate=[]
c=0
for line in data:
    c +=1
    line=line.split()
    tmp=[0 for i in range(115)]
    if c < 10001:
        for i in range(0,10):
            if i<5:
                tmp[int(line[i])-1]='1'
            else:
                tmp[int(line[i]) - 1] = '-1'
        tmp[114]=line[10]
        # print(tmp)
        datata.append(tmp)
    else:
        for i in range(0,10):
            if i<5:
                tmp[int(line[i])-1]='1'
            else:
                tmp[int(line[i]) - 1] = '-1'
        tmp[114] = line[10]
        datate.append(tmp)

pradiant1=[]
pradiant2=[]
pdire1=[]
pdire2=[]
zero0=[]
zero1=[]
bayes=[]
for i in range(0,114):
    pradiant1.append(posterior(datata, '1', i, '-1'))
    pradiant2.append(posterior(datata, '-1', i, '-1'))
    pdire1.append(posterior(datata, '1', i, '1'))
    pdire2.append(posterior(datata, '-1', i, '1'))
    zero0.append(posterior(datata,0, i, '-1'))
    zero1.append(posterior(datata, 0, i, '1'))
print(pradiant1)
print(pradiant2)
print(pdire1)
print(pdire2)
print(zero0)
print(zero1)
bayes.append(pradiant1)
bayes.append(pradiant2)
bayes.append(pdire1)
bayes.append(pdire2)
bayes.append(zero0)
bayes.append(zero1)
fo=open('bayes8888.txt','w')
for i in bayes:
    for j in i :
        if j==0.0:
            j=0.001
        fo.write(str(j)+' ')
    fo.write('\n')
fo.write(str(prior(datata,'-1')))
fo.write('\n')
fo.write(str(prior(datata,'1')))
fo.close()
# print(float(calculateprobability(datata,datate,bayes)))


