import urllib.request
import time
# 2821430697
# 2821478315
fo1=open('laoji.txt')
i=3
i_str='%d'%i
fo = open("laoji"+i_str+".txt", "w")
count=0;
for line in fo1:
    line=line.split()
for match_id_num in line:
    start = time.clock()
    count=count+1
    if count==46000:
        count=0
        i=i+1
        i_str = '%d' % i
        fo = open("dotadata" + i_str + ".txt", "w")
    try:
     resp=urllib.request.urlopen('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=EFB29011FFD46B347C9E9DEE8A1F4252&match_id='+match_id_num,timeout=30)
     html=resp.read()
     for tt in html.splitlines():
         fo.write(tt.decode())
     fo.write('\n')
    except:
        continue
fo.close();