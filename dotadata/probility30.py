from __future__ import division

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
            out[0]=int(out[0])
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

import numpy as np
fo3=open('dota2heroduiying.txt')
dy=[]
for line in fo3:
    line=line.split()
    dy.append(line)
try:
    pre=np.load('pre30.npy')
    pre=pre.tolist()
except:
    pre = [[] for i in range(114)]

fo = open('highnewdata2.txt')
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
        for substrs in substr:
            out = findsubstrnum(substrs,line)
            if out!=0:
                tmp_mex.append(out)
            else:
                tmp_mex=[]
                break
        if len(tmp_mex)>1:
            dur=findsubstrnum('duration', line)
            tmp_mex=mysort1(tmp_mex,dy)
            if tmp_mex[4]==-1:
                for ind in range(5):
                    try:
                        pre[int(tmp_mex[1][ind])-1][int(dur[0]/60)]+=1
                    except:
                        n=int(dur[0]/60)
                        while len(pre[int(tmp_mex[1][ind]) - 1])<n+1:
                            pre[int(tmp_mex[1][ind]) - 1].append(0)
                        pre[int(tmp_mex[1][ind]) - 1][int(dur[0] / 60)] += 1
            if tmp_mex[4]==1:
                for ind in range(5,10):
                    try:
                        pre[int(tmp_mex[1][ind])-1][int(dur[0]/60)]+=1
                    except:
                        n = int(dur[0] / 60)
                        while len(pre[int(tmp_mex[1][ind]) - 1]) < n+1:
                            pre[int(tmp_mex[1][ind]) - 1].append(0)
                        pre[int(tmp_mex[1][ind]) - 1][int(dur[0] / 60)] += 1
print(pre)
np.save('pre30.npy',pre)





