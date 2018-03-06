from __future__ import division

def guolv(ss):
    return True
    outr = findsubstrnum('radiant_score', ss)
    outd = findsubstrnum('dire_score', ss)
    outg = findsubstrnum('gold_per_min',ss)
    outt = findsubstrnum('duration',ss)
    gr=0
    gd=0
    if outg!=0:
        for i in range(0,10):
            if i<5:
                gr=int(outg[i])+gr
            else:
                gd=int(outg[i])+gd
        if outr != False and outd != False and outr[0] != 0 and outd[0] != 0:
            if int(outr[0]) > int(outd[0]):
                if float((int(outr[0]) - int(outd[0])) / int(outd[0])) < 1:
                    #or gr - gd < 0.4 * gd
                    return False
            else:
                if float((int(outd[0]) - int(outr[0])) / int(outr[0])) < 1 :
                    #or gd - gr < 0.4 * gr
                    return False
        else:
            return False
        return True
    else:
        return False

def findsubstrnum(s,ss):
    out = []
    ad=ss.find(s,0)
    if s=='radiant_win':
        if ss[ad+len(s)]=='t':
            return -1
        else:
            return 1
    else:
        tmp=''
        while ad!=-1:
            ad=ad+len(s)
            tmp=''
            while ss[ad].isdigit():
                tmp = tmp + ss[ad]
                ad = ad + 1
            if tmp=='4294967295':
                tmp='0'
            tmp=int(tmp)
            if (tmp<50 or tmp>1200) and s!='hero_id' and s!='account_id' and s!='radiant_score' and s!='dire_score' and s!='duration':
                return 0
            out.append(tmp)
            ad=ss.find(s,ad)
        if s=='duration':
            while len(out)!=1:
                del out[len(out)-1]
        # print(out)
        if len(out)==10 or len(out)==1:
            return out
        else:
            return False


def findsubstrnums(s,ss):
    ad = ss.find(s, 0)
    ad = ad + len(s)
    tmp = ''
    while ss[ad].isdigit():
        tmp = tmp + ss[ad]
        ad = ad + 1
    return tmp

def filtration(ss):
    if len(ss) > 80 and (findsubstrnums('game_mode',ss)=='3' or findsubstrnums('game_mode',ss)=='2' or findsubstrnums('game_mode',ss)=='22') and findsubstrnums('leaver_status',ss)=='0' and findsubstrnums('human_players',ss)=='10':
        return True
    else:
        return False


def mysort(A):
    gpm=A[2]
    xpm=A[3]
    avg=[]
    for i in range(0,4):
        avg.append((gpm[i]+xpm[i])/2)
    for i in range(0,4):
        for j in range(i,4):
            if avg[i]<avg[j]:
                tmp=A[0][i]
                A[0][i]=A[0][j]
                A[0][j]=tmp
                tmp = A[1][i]
                A[1][i] = A[1][j]
                A[1][j] = tmp
    avg = []
    for i in range(5,9):
        avg.append((gpm[i]+xpm[i])/2)
    for i in range(5,9):
        for j in range(i,9):
            if avg[i-5]<avg[j-5]:
                tmp=A[0][i]
                A[0][i]=A[0][j]
                A[0][j]=tmp
                tmp = A[1][i]
                A[1][i] = A[1][j]
                A[1][j] = tmp
    return A

def mysort1(A,dy):
    for i in range(0, 5):
        for j in range(i, 5):
            if dy[1].index(str(A[1][i])) > dy[1].index(str(A[1][j])):
                tmp = A[0][i]
                A[0][i] = A[0][j]
                A[0][j] = tmp
                tmp = A[1][i]
                A[1][i] = A[1][j]
                A[1][j] = tmp
    for i in range(5, 10):
        for j in range(i, 10):
            if dy[1].index(str(A[1][i])) > dy[1].index(str(A[1][j])):
                tmp = A[0][i]
                A[0][i] = A[0][j]
                A[0][j] = tmp
                tmp = A[1][i]
                A[1][i] = A[1][j]
                A[1][j] = tmp
    return A
fo3=open('dota2heroduiying.txt')

dy=[]
for line in fo3:
    line=line.split()
    dy.append(line)


fo = open('newdataxxx.txt')
fo1=open('cleardatabig.txt','a')
# fo3=open('accountid.txt','w')
delet = list('{"[,:')
accountid=[]
for line in fo:
    for i in delet:
        line = line.replace(i, '')
    if filtration(line):
        substr=[]
        substr.append('account_id')
        substr.append('hero_id')
        substr.append('gold_per_min')
        substr.append('xp_per_min')
        substr.append('radiant_win')
        tmp_mex=[]
        if guolv(line):
            for substrs in substr:
                out = findsubstrnum(substrs,line)
                if out!=0:
                    tmp_mex.append(out)
                else:
                    tmp_mex=[]
                    break
        if len(tmp_mex)>1:
            tmp_mex=mysort1(tmp_mex,dy)
            for i in tmp_mex[0]:
                accountid.append(i)
            for i in tmp_mex[1]:
                fo1.write(str(i)+' ')
            fo1.write(str(tmp_mex[4])+'\n')
# accountid=list(set(accountid))
# for i in accountid:
#     fo3.write(str(i)+' ')
fo1.close()
fo.close()
# fo2.close()
# fo3.close()



