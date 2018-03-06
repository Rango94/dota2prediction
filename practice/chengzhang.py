#coding:gbk
import codecs
import urllib.request
import sys
def findsubstrnum(s,ss):
    out = []
    ad=ss.find(s,0)
    tmp=''
    mark=0
    while ad!=-1:
        ad=ad+len(s)
        tmp=''
        while ss[ad].isdigit() or ss[ad]=='.' or ss[ad]=='-' or ss[ad]=='+':
            # if ss[ad]=='0' and mark==1:
            #     break
            # if ss[ad]=='.':
            #     mark=1
            if ss[ad]=='+':
                ad=ad+1
                tmp1 = ''
                while ss[ad].isdigit() or ss[ad] == '.' or ss[ad] == '-':
                    tmp1 = tmp1 + ss[ad]
                    ad = ad + 1
                tmp=float(tmp)*7+float(tmp1)
            else:
                tmp = tmp + ss[ad]
                ad = ad + 1
        print(tmp)
        tmp=float(tmp)
        out.append(tmp)
        ad=ss.find(s,ad)
    if len(out)==10 or len(out)==1:
        return out
    else:
        return False

type = sys.getfilesystemencoding()
fo=codecs.open('herosnameandid.txt','r','utf-8')
fo1=open('anti.txt','w')
fo2=open('comb.txt','w')
herosnameandid=[]
for line in fo:
    line=line.split()
    herosnameandid.append(line)

zero=0
tmp=[]
out=[]
for i in range(0,114):
    tmp.append(zero)
for i in range(0,6):
    out.append(tmp.copy())
str1=[]
str1.append('health_add = ')
str1.append('mana_add = ')
str1.append('armor_add = ')
str1.append('health_init = 150+')
str1.append('mana_init = ')
str1.append('armor_init = ')

for nameeg in herosnameandid[1]:
    if nameeg!='0':
        print(nameeg)
        print(herosnameandid[1].index(nameeg))
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        req = urllib.request.Request(
            'http://www.dotamax.com/hero/detail/'+nameeg+'/', headers=headers)
        html = str(urllib.request.urlopen(req).read().decode('utf-8').splitlines())
        ad=html.find('health_add',0)
        end=html.find('DOTA_ATTRIBUTE_INTELLECT',0)
        sub=html[ad:end]
        print(sub)
        for i in range(0,6):
            tmp=findsubstrnum(str1[i], sub)
            out[i][herosnameandid[1].index(nameeg)]=tmp[0]

print(out[0])
print(out[1])
print(out[2])
print(out[3])
print(out[4])
print(out[5])
# for i in anti:
#     fo1.write(i+'\n')
# for i in comb:
#     fo2.write(i+'\n')
# fo.close()
# fo1.close()
# fo2.close()



