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


fo=open('cleardatabig_whole.txt')
fo1=open('standata_myway_whole.txt','w')
fo2=open('newmark1_back.txt')
foat=open('antinum.txt')
focb=open('combnum.txt')
fobayes=open('bayes.txt')
bayes=[]
for line in fobayes:
    line=line.split()
    bayes.append(line)


mark=[]
for line in fo2:
    mark.append(line.split())
anti_tmp=[]
comb_tmp=[]
# anti=[]
# comb=[]
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
anti=anti_tmp
comb=comb_tmp
# maxanti = newmax(anti_tmp)
# minanti = newmin(anti_tmp)
# maxcomb = newmax(comb_tmp)
# mincomb = newmin(comb_tmp)
#
# for i in anti_tmp:
#     tmp = []
#     for j in i:
#         tmp.append(float((j - minanti) / (maxanti - minanti)))
#     anti.append(tmp.copy())
# for i in comb_tmp:
#     tmp = []
#     for j in i:
#         tmp.append(float((j - mincomb) / (maxcomb - mincomb)))
#     comb.append(tmp.copy())

count=0
for line in fo:
    count=count+1
    if count==110000:
        break
    line=line.split(" ")
    fo1.write('%d' % int(line[len(line) - 1]) + ' ')
    xsanti=[]
    xscomb=[]
    pradiant=0.5568
    pdire=0.4432
    for i in range(0, 114):
        if str(i+1) not in line[0:10]:
            pradiant *= float(bayes[4][i])
            pdire *= float(bayes[5][i])
        elif str(i+1) in line[0:5]:
            pradiant *= float(bayes[0][i])
            pdire *= float(bayes[2][i])
        elif str(i+1) in line[5:10]:
            pradiant *= float(bayes[1][i])
            pdire *= float(bayes[3][i])
    pradiant=pradiant/(pradiant+pdire)
    pdire = 1-pradiant
    for i in range(0,10):
        tmp1 = 0
        tmp2=0
        if i<=4:
            for j in range(0,10):
                if j<=4:
                    tmp2=tmp2+float(comb[int(line[i])-1][int(line[j])-1])
                else:
                    tmp1 = tmp1 + float(anti[int(line[i]) - 1][int(line[j]) - 1])
        else:
            for j in range(0,10):
                if j<=4:
                    tmp1=tmp1+float(anti[int(line[i])-1][int(line[j])-1])
                else:
                    tmp2 = tmp2 + float(comb[int(line[i]) - 1][int(line[j]) - 1])
        xsanti.append(tmp1)
        xscomb.append(tmp2)
    maxa=max([max(xsanti),max(xscomb)])
    mina = min([min(xsanti), min(xscomb)])

    for i in range(len(xscomb)):
        xscomb[i]=(xscomb[i]-mina)/(maxa-mina)
        xsanti[i] = (xsanti[i] - mina) / (maxa - mina)


    submark1=[]
    for i in range(0,5):
        for j in range(0,len(mark)):
            submark1.append(float(mark[j][int(line[i])-1]))
        submark1.append(xsanti[i])
        submark1.append(xscomb[i])
    submark2 = []
    for i in range(5, 10):
        for j in range(0, len(mark)):
            submark2.append(float(mark[j][int(line[i])-1]))
        submark2.append(xsanti[i])
        submark2.append(xscomb[i])
    line=[]
    for i in range(0,(len(submark1))):
        line.append(float(submark1[i]))
    line.append(pradiant)
    for i in range(0, (len(submark2))):
        line.append(float(submark2[i]))
    line.append(pdire)

    for i in range(0,len(line)):
        fo1.write('%d'%(i+1)+':'+str(line[i])+' ')
    fo1.write('\n')
fo.close()
fo1.close()