import numpy as np
import random
from sklearn import svm

def readfile(name):
    with open(name) as fo:
        data=fo.readlines()
    for line in data:
        with open('Y.txt', 'a') as foY:
            with open('X.txt', 'a') as foX:
                line=line.split()
                foY.write(str(max(int(line[0]),0))+'\n')
                for i in range(len(line)-1):
                    foX.write(line[i+1].split(':')[1]+' ')
                foX.write('\n')

def PSO(ads,n):
    y, x = svm_read_problem(ads)
    margin=0
    if len(y)>10000:
        margin=len(y)-10001
    if len(y)<=10000:
        margin=int(len(y)/2)
    canshu=np.zeros((2,n))
    canshu[0,0]=1
    canshu[1,0]=0.07
    bestc=canshu[0,0]
    bestg=canshu[1,0]
    bestsinglecv=np.zeros((1,n))
    bestsinglec=np.zeros((1,n))
    bestsingleg=np.zeros((1,n))
    bestcv=0
    v=np.zeros((2,n))
    for i in range(1,n):
        canshu[0,i]=0.2+3.5*random.random()
        canshu[1,i]=0.5*random.random()
    while 1==1:
        for i in range(0,n):
            c=canshu[0,i]
            g=canshu[1,i]
            print("bestc:",bestc)
            print("bestg:",bestg)
            print("bestcv:",bestcv)
            print('-----------------')
            cmd='-c '+str(c)+' -g '+str(max(g,0.001))+' -h 0'
            start=int(margin*random.random())

            model = svm_train(y[start:min(start+10000,len(y)-1)], x[start:min(start+10000,len(y)-1)], cmd)

            # clf = svm.SVC()
            # clf.fit(x[start:min(start+10000,len(y)-1),:], y[start:min(start+10000,len(y)-1)])
            start = start+10000
            # Y_ = clf.predict(x[start:min(start+10000,len(y)-1),:])
            p_label, p_acc, p_val = svm_predict(y[10000:], x[start:min(start+10000,len(y)-1)], model)
            cv=p_acc[0]




            # for k in range(len(Y_)):
            #     if y[k + start] == Y_[k]:
            #         Y_[k] = 1
            #     else:
            #         Y_[k] = 0
            # cv=np.mean(Y_)
            if cv>=bestsinglecv[0,i]:
                bestsinglecv[0,i] = cv
                bestsinglec[0,i] = c
                bestsingleg[0,i] = g
        print('bestsinglecv:', bestsinglecv)
        print('bestsinglec:', bestsinglec)
        print('bestsingleg:', bestsingleg)
        index = np.argmax(bestsinglecv)
        bestcv = max(bestsinglecv)
        bestc = bestsinglec[0, index]
        bestg = bestsingleg[0, index]
        for i in range(n):
            v[0, i] = 0.5 * v[0, i] + random.random() * (bestsinglec[0, i] - canshu[0, i]) + random.random() * (
            bestc - canshu[0, i])
            if v[0, i] >= 0.5:
                v[0, i] = 0.5
            elif v[0, i] <= -0.5:
                v[0, i] = -0.5
            canshu[0, i] = canshu[0, i] + v[0, i]
            v[1, i] = 0.5 * v[1, i] + random.random() * (bestsingleg[0, i] - canshu[1, i]) + random.random() * (
            bestg - canshu[1, i])
            if v[1, i] >= 0.5:
                v[1, i] = 0.5
            elif v[1, i] <= -0.5:
                v[1, i] = -0.5
            canshu[1, i] =max( canshu[1, i] + v[1, i],0.0001)
        print(canshu)

def readoldfile(ads):
    with open(ads) as fo:
        lines=fo.readlines()
        X=np.zeros((len(lines),len(lines[1].split())-1))
        print(X.shape)
        Y=np.zeros((1,len(lines)))
        for h in range(len(lines)):
            line=lines[h].split()
            Y[0,h]=int(line[0])
            for i in range(len(line)):
                if i>0:
                    # print(float(line[i][line[i].find(':')+1:]))
                    X[h,i-1]=float(line[i][line[i].find(':')+1:])
            # print(Y)
        np.save('X_myway_whole',X)
        np.save('Y_myway_whole',Y[0])

def onehotstand(ads):
    with open(ads) as fo:
        lines=fo.readlines()
        X=np.zeros((len(lines),228))
        Y=np.zeros((1,len(lines)))
        n=0
        for line in lines:
            line=line.split()
            for j in range(5):
                X[n,int(line[j])-1]=1
            for j in range(5,10):
                X[n, int(line[j]) +113] = 1
            Y[0,n]=int(line[10])
            n+=1
        np.save('X_whole', X)
        np.save('Y_whole', Y[0])

def chulitadeshuju(x):
    def newmax(A):
        tmp = []
        for i in A:
            tmp.append(max(i))
        return max(tmp)
    def newmin(A):
        tmp = []
        for i in A:
            tmp.append(min(i))
        return min(tmp)
    bayes = []
    with open('bayes.txt') as fobayes:
        for line in fobayes:
            line = line.split()
            bayes.append(line)
        mark = []
    with open('newmark1_back.txt') as fo2:
        for line in fo2:
            mark.append(line.split())
    with open('antinum.txt') as foat:
        with open('combnum.txt') as focb:
            anti_tmp = []
            comb_tmp = []
            anti = []
            comb = []
            for line in foat:
                line = line.split()
                for i in range(0, len(line)):
                    line[i] = float(line[i])
                anti_tmp.append(line)
            for line in focb:
                line = line.split()
                for i in range(0, len(line)):
                    line[i] = float(line[i])
                comb_tmp.append(line)
    anti=anti_tmp
    comb=comb_tmp
    with open('dota2heroduiying.txt') as fo:
        outx=[]
        fre=[int(i) for i in fo.readlines()[1].split()]
        n=0
        for Line in x:
            line = []
            for i in fre:
                if Line[i-1]==1:
                    line.append(i)
            for i in fre:
                if Line[i+113]==1:
                    line.append(i)
            n+=1
            xsanti = []
            xscomb = []
            pradiant = 0.5568
            pdire = 0.4432
            for i in range(0, 114):
                if str(i + 1) not in line[0:10]:
                    pradiant *= float(bayes[4][i])
                    pdire *= float(bayes[5][i])
                elif str(i + 1) in line[0:5]:
                    pradiant *= float(bayes[0][i])
                    pdire *= float(bayes[2][i])
                elif str(i + 1) in line[5:10]:
                    pradiant *= float(bayes[1][i])
                    pdire *= float(bayes[3][i])
            pradiant = pradiant / (pradiant + pdire)
            pdire = 1 - pradiant
            for i in range(0, 10):
                tmp1 = 0
                tmp2 = 0
                if i <= 4:
                    for j in range(0, 10):
                        if j <= 4:
                            tmp2 = tmp2 + float(comb[int(line[i]) - 1][int(line[j]) - 1])
                        else:
                            tmp1 = tmp1 + float(anti[int(line[i]) - 1][int(line[j]) - 1])
                else:
                    for j in range(0, 10):
                        if j <= 4:
                            tmp1 = tmp1 + float(anti[int(line[i]) - 1][int(line[j]) - 1])
                        else:
                            tmp2 = tmp2 + float(comb[int(line[i]) - 1][int(line[j]) - 1])
                xsanti.append(tmp1)
                xscomb.append(tmp2)
            maxsss = max([max(xsanti), max(xscomb)])
            minsss = min([min(xsanti), min(xscomb)])
            for i in range(len(xscomb)):
                xscomb[i] = (xscomb[i] - minsss) / (maxsss - minsss)
                xsanti[i] = (xsanti[i] - minsss) / (maxsss - minsss)
            submark1 = []
            for i in range(0, 5):
                for j in range(0, len(mark)):
                    submark1.append(float(mark[j][int(line[i]) - 1]))
                submark1.append(xsanti[i])
                submark1.append(xscomb[i])
            submark2 = []
            for i in range(5, 10):
                for j in range(0, len(mark)):
                    submark2.append(float(mark[j][int(line[i]) - 1]))
                submark2.append(xsanti[i])
                submark2.append(xscomb[i])
            tmp = []
            for i in range(0, (len(submark1))):
                tmp.append(float(submark1[i]))
            tmp.append(pradiant)
            for i in range(0, (len(submark2))):
                tmp.append(float(submark2[i]))
            tmp.append(pdire)
            outx.append(tmp)
    outx=np.array(outx)
    return outx


def rawstand(dataads):
    out=[]
    # def newmax(A):
    #     tmp = []
    #     for i in A:
    #         tmp.append(max(i))
    #     return max(tmp)
    # def newmin(A):
    #     tmp = []
    #     for i in A:
    #         tmp.append(min(i))
    #     return min(tmp)
    fo = open(dataads)
    fo2 = open('mark_random.txt')
    foat = open('antinum.txt')
    focb = open('combnum.txt')
    fobayes = open('bayes.txt')
    bayes = []
    for line in fobayes:
        line = line.split()
        bayes.append(line)
    mark = []
    cnn=0
    seq=[]
    a = random.random()
    for line in fo2:
        cnn+=1
        if random.random()<a:
            seq.append(cnn)
            mark.append(line.split())
    anti_tmp = []
    comb_tmp = []
    for line in foat:
        line = line.split()
        for i in range(0, len(line)):
            line[i] = float(line[i])
        anti_tmp.append(line)
    for line in focb:
        line = line.split()
        for i in range(0, len(line)):
            line[i] = float(line[i])
        comb_tmp.append(line)
    anti = anti_tmp
    comb = comb_tmp
    Y=[]
    for line in fo:
        line = line.split(" ")
        Y.append(int(line[len(line)-1]))
        xsanti = []
        xscomb = []
        pradiant = 0.5568
        pdire = 0.4432
        for i in range(0, 114):
            if str(i + 1) not in line[0:10]:
                pradiant *= float(bayes[4][i])
                pdire *= float(bayes[5][i])
            elif str(i + 1) in line[0:5]:
                pradiant *= float(bayes[0][i])
                pdire *= float(bayes[2][i])
            elif str(i + 1) in line[5:10]:
                pradiant *= float(bayes[1][i])
                pdire *= float(bayes[3][i])
        pradiant = pradiant / (pradiant + pdire)
        pdire = 1 - pradiant
        for i in range(0, 10):
            tmp1 = 0
            tmp2 = 0
            if i <= 4:
                for j in range(0, 10):
                    if j <= 4:
                        tmp2 = tmp2 + float(comb[int(line[i]) - 1][int(line[j]) - 1])
                    else:
                        tmp1 = tmp1 + float(anti[int(line[i]) - 1][int(line[j]) - 1])
            else:
                for j in range(0, 10):
                    if j <= 4:
                        tmp1 = tmp1 + float(anti[int(line[i]) - 1][int(line[j]) - 1])
                    else:
                        tmp2 = tmp2 + float(comb[int(line[i]) - 1][int(line[j]) - 1])
            xsanti.append(tmp1)
            xscomb.append(tmp2)
        maxa = max([max(xsanti), max(xscomb)])
        mina = min([min(xsanti), min(xscomb)])
        for i in range(len(xscomb)):
            xscomb[i] = (xscomb[i] - mina) / (maxa - mina)
            xsanti[i] = (xsanti[i] - mina) / (maxa - mina)
        submark1 = []
        for i in range(0, 5):
            for j in range(0, len(mark)):
                submark1.append(float(mark[j][int(line[i]) - 1]))
            submark1.append(xsanti[i])
            submark1.append(xscomb[i])
        submark2 = []
        for i in range(5, 10):
            for j in range(0, len(mark)):
                submark2.append(float(mark[j][int(line[i]) - 1]))
            submark2.append(xsanti[i])
            submark2.append(xscomb[i])
        line = []
        for i in range(0, (len(submark1))):
            line.append(float(submark1[i]))
        line.append(pradiant)
        for i in range(0, (len(submark2))):
            line.append(float(submark2[i]))
        line.append(pdire)
        out.append(line)
    fo.close()
    # np.save('tmpX.npy',np.array(out))
    # np.save('tmpY.npy',np.array(Y))
    return np.array(out),np.array(Y),seq



# readoldfile('standata_myway_whole.txt')