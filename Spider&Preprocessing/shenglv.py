#coding:gbk
import codecs
def findnum(s,line):
    ad=line.find(s,0)
    ad=line.find('"height: 10px">',ad)
    ad=ad+len('"height: 10px">')
    tmp=''
    while line[ad].isdigit() or line[ad]=='.':
        tmp=tmp+line[ad]
        ad=ad+1
    if tmp=='':
        return str(0)
    else:
        return tmp

heroname=codecs.open('herosnameandid.txt','r','utf-8')
slys=open('shenglvyuanshi.txt')
shenglv=open('shenglv.txt','w')
slys1=slys.read()

z='0'
sl=[]

for i in range(0,114):
    sl.append(z)
tmp=[]

for i in heroname.readlines():
    i=i.split()
    tmp.append(i)


for i in range(0,114):
    if i!=23:
        sl[i]=findnum(tmp[2][i], slys1)

for i in sl:
    shenglv.write(i+' ')