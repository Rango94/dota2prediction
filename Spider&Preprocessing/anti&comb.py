#coding:gbk
import codecs
def findnum(s,line):
    ad=line.find(s,0)
    ad=line.find('"height: 10px">',ad)
    ad=ad+len('"height: 10px">')
    tmp=''
    while line[ad].isdigit() or line[ad]=='-' or line[ad]=='.':
        tmp=tmp+line[ad]
        ad=ad+1
    if tmp=='':
        return str(0)
    else:
        return tmp
fo=codecs.open('herosnameandid.txt','r','utf-8')
fo1=open('anti.txt')
fo2=open('comb.txt')
fo11=open('antinum.txt','w')
fo21=open('combnum.txt','w')
nameandid=[]
cell='0'
anti=[]
comb=[]
for i in range(0,114):
    line = []
    for j in range(0,114):
        line.append(cell)
    anti.append(line.copy())
comb=anti.copy()
for line in fo:
    line=line.split()
    nameandid.append(line)
n=0
for line in fo1:
    if n==23:
        n = n + 1
        continue
    for i in range(0,114):
        if i == 23:
            continue
        if n!=i:
            anti[n][i]=findnum(nameandid[2][i],line)
    n=n+1

for i in anti:
    print(len(i))
    for line in i:
        fo11.write(line+' ')
    fo11.write("\n")
n=0
for line in fo2:
    if n==23:
        n = n + 1
        continue
    for i in range(0,114):
        if n!=i:
            if i==23:
                continue
            comb[n][i]=findnum(nameandid[2][i],line)
    n=n+1
for i in comb:
    for line in i:
        fo21.write(line+' ')
    fo21.write("\n")


