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
        tmp=int(tmp)
        out.append(tmp)
        ad=ss.find(s,ad)
    if len(out)==10 or len(out)==1:
        return out
    else:
        return False

def findsubstrnum1(s,ss):
    out = []
    ad=ss.find(s,0)
    if s=='"radiant_win":':
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
            if (tmp<50 or tmp>1200) and s!='"hero_id":' and s!='"account_id":' and s!='"radiant_score":' and s!='"dire_score":':
                return 0
            out.append(tmp)
            ad=ss.find(s,ad)
        if len(out)==10 or len(out)==1:
            return out
        else:
            return False


def filtration(ss):
    if len(ss) > 80 and (findsubstrnums('"game_mode":',ss)=='3' or findsubstrnums('"game_mode":',ss)=='2' or findsubstrnums('"game_mode":',ss)=='22') and findsubstrnums('"leaver_status":',ss)=='0' and findsubstrnums('"human_players":',ss)=='10':
        return True
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
initdata=open('highnewdata.txt')
aftdata=open('aftdata.txt','w')
str='"duration":'
zero=0
winhero=[]
notwinhero=[]
for i in range(0,114):
    winhero.append(zero)
    notwinhero.append(zero)


for line in initdata:
    out = []
    if filtration(line):
        dur=findsubstrnum(str, line)
        if int(dur[0])>3600:
            continue
        substr = []
        substr.append('"hero_id":')
        out.append(findsubstrnum1('"radiant_win":', line))
        tmp=findsubstrnum1(substr[0], line)
        if tmp==False:
            continue
        for i in tmp:
            out.append(i)

        if len(out)==11:
            if out[0]==1:
                for i in range(6,11):
                    winhero[out[i]-1]=(winhero[out[i]-1])+1
                for i in range(1,6):
                    notwinhero[out[i]-1]=notwinhero[out[i]-1]+1
            if out[0]==-1:
                for i in range(1,6):
                    winhero[out[i]-1]=winhero[out[i]-1]+1
                for i in range(6,11):
                    notwinhero[out[i]-1]=notwinhero[out[i]-1]+1

for i in winhero:
    aftdata.write('%d'%i+' ')
aftdata.write('\n')
for i in notwinhero:
    aftdata.write('%d'%i + ' ')