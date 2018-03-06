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
        tmp=int(tmp)
        out.append(tmp)
        ad=ss.find(s,ad)
    return list(set(out))

#根据选手id寻找最近的比赛
def findmatchbyplayer(id,num,out):
    for i in range(5,num):
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        req = urllib.request.Request('http://www.dotamax.com/player/match/'+id+'/?skill=&ladder=&hero=-1&p='+str(i+1), headers=headers)
        data=str(urllib.request.urlopen(req).read().splitlines())
        out.append(findsubstrnum('match/detail/',data))
    return out

# foaccount=open('accountid1.txt')
# for line in foaccount:
#     line = line.split()
# num=10

fo = open("highnewdata1.txt", "a")
fo1=open('matchidaft.txt')

# out=[]
# newout=[]
# for accountid in line:
#     print("id"+accountid)
#     findmatchbyplayer(accountid,num,out )
#     print(len(out))

# for i in range(0,len(out)):
#     for it in out[i]:
#         newout.append(it)
# print(len(newout))
# newout=list(set(newout))
# print(len(newout))
# for i in newout:
#     fo2.write(str(i)+' ')


# 根据比赛id获取比赛数据
for line in fo1:
    out=line.split()
i=0
for match_id_num in out:
    if match_id_num=='3291907408' or i==1:
        i=1
        match_id_str=str(match_id_num)
        print(match_id_str)
        try:
         resp=urllib.request.urlopen('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=EFB29011FFD46B347C9E9DEE8A1F4252&match_id='+match_id_str,timeout=30)
         html=resp.read()
         for tt in html.splitlines():
             fo.write(tt.decode())
         fo.write('\n')
        except:
            continue
    else:
        continue
fo.close()