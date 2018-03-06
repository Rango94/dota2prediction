fo=open('dotaheros.txt')
fo1=open('herosnameandid.txt','w')
hero=''
for line in fo:
    hero=hero+str(line.splitlines())
print(hero)
ad=0
name=[]
id=[]
while ad!=-1:
    ad=hero.find('hero_',ad)
    if ad==-1:
        break
    tmpname=''
    ad=ad+5
    print(ad)
    while hero[ad]!='"':
        tmpname=tmpname+hero[ad]
        ad=ad+1
    name.append(tmpname)
    print(tmpname)
    ad=hero.find('id":', ad)
    tmpid=''
    ad = ad + 4
    while hero[ad].isdigit():
        tmpid=tmpid+hero[ad]
        ad=ad+1
    id.append(tmpid)
for i in id:
        fo1.write(i + ' ')
fo1.write('\n')
for i in name:
    fo1.write(i+' ')

