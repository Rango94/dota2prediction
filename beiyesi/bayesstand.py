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

fobayes=[]
fo=open('cleardatabig.txt')
fo1=open('standatatrain.txt','w')
fobayes.append(open('bayes.txt'))

bayesall=[]
for j in fobayes:
    bayes = []
    for i in j:
        i = i.split()
        bayes.append(i)
    bayesall.append(bayes)


for line in fo:
    line = line.split(" ")
    fo1.write('%d' % int(line[len(line) - 1]) + ' ')
    out=[]
    for bayes in bayesall:
        pradiant=float(bayes[6][0])
        pdire=float(bayes[7][0])
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
        out.append(pradiant)
    for i in range(0,len(out)):
        fo1.write('%d'%(i+1)+':'+str(out[i])+' ')
    fo1.write('\n')
fo.close()
fo1.close()