

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