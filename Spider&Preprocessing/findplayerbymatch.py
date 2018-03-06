from __future__ import division
import urllib.request
def findsubstrnum(s,ss):
    out = []
    ad=ss.find(s,0)
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
        if (tmp<50 or tmp>1200) and s!='hero_id' and s!='account_id' and s!='radiant_score' and s!='dire_score':
            return 0
        out.append(tmp)
        ad=ss.find(s,ad)


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

fo=open('accountid.txt','w')
fo1=open('laoji.txt')
for line in fo1:
    line=line.split()

for i in line:
    try:
     resp=urllib.request.urlopen('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=EFB29011FFD46B347C9E9DEE8A1F4252&match_id='+i,timeout=30)
     html=resp.read()
     for tt in html.splitlines():
         fo.write(tt.decode())
     fo.write('\n')
    except:
        continue




