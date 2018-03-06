#coding:gbk
import codecs
import urllib.request
import sys
type = sys.getfilesystemencoding()
fo=codecs.open('herosnameandid.txt','r','utf-8')
fo1=open('anti.txt','w')
fo2=open('comb.txt','w')
herosnameandid=[]
for line in fo:
    line=line.split()
    herosnameandid.append(line)
anti=[]
comb=[]
for nameeg in herosnameandid[1]:
    print(nameeg)
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib.request.Request(
        'http://www.dotamax.com/hero/detail/match_up_anti/'+nameeg+'/', headers=headers)
    html = str(urllib.request.urlopen(req).read().decode('utf-8').splitlines())
    ad=html.find('职业比赛',0)
    anti.append(html[ad:])
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib.request.Request(
        'http://www.dotamax.com/hero/detail/match_up_comb/' + nameeg + '/', headers=headers)
    html = str(urllib.request.urlopen(req).read().decode('utf-8').splitlines())
    ad = html.find('职业比赛', 0)
    comb.append(html[ad:])
for i in anti:
    fo1.write(i+'\n')
for i in comb:
    fo2.write(i+'\n')
fo.close()
fo1.close()
fo2.close()



