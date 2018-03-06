def newmax(A):
    tmp=[]
    for i in A:
        tmp.append(max(i))
    return max(tmp)
def newmin(A):
    tmp = []
    for i in A:
        tmp.append(min(i))
    return min(tmp)
fo=open('cleardatabig.txt')
fo1=open('standatatrain.txt','w')
foat=open('antinum.txt')
focb=open('combnum.txt')
anti_tmp=[]
comb_tmp=[]
anti=[]
comb=[]
for line in foat:
    line=line.split()
    for i in range(0,len(line)):
        line[i]=float(line[i])
    anti_tmp.append(line)
for line in focb:
    line=line.split()
    for i in range(0,len(line)):
        line[i]=float(line[i])
    comb_tmp.append(line)
maxanti=newmax(anti_tmp)
print(maxanti)
minanti=newmin(anti_tmp)
maxcomb=newmax(comb_tmp)
mincomb=newmin(comb_tmp)
print(minanti)
print(maxcomb)
print(mincomb)
for i in anti_tmp:
    tmp=[]
    for j in i:
        tmp.append(float((j-minanti)/(maxanti-minanti)))
    anti.append(tmp.copy())
for i in comb_tmp:
    tmp=[]
    for j in i:
        tmp.append(float((j-mincomb)/(maxcomb-mincomb)))
    comb.append(tmp.copy())


for line in fo:
    line = line.split(" ")
    fo1.write('%d'%int(line[len(line) - 1])+' ')
    out=[]
    for i in range(0,10):
        if i<5:
            for j in range(0,10):
                if j<5:
                    out.append(float(comb[int(line[i])-1][int(line[j])-1]))
                else:
                    out.append(float(anti[int(line[i])-1][int(line[j])-1]))
        else:
            for j in range(0,10):
                if j<5:
                    out.append(float(anti[int(line[i]) - 1][int(line[j]) - 1]))
                else:
                    out.append(float(comb[int(line[i]) - 1][int(line[j]) - 1]))

    # for i in out:
    #     newout.append(float((i-min(out))/(max(out)-min(out))))
    # print(newout)
    for i in range(0,len(out)):
        fo1.write('%d'%(i+1)+':'+str(out[i])+' ')
    fo1.write('\n')
fo1.close()



