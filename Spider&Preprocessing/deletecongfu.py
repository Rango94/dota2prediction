fo=open('matchid.txt')
fo1=open('matchid1.txt')
fo2=open('matchidaft.txt','w')
for one in fo:
    one=one.split()
for two in fo1:
    two=two.split()

for i in two:

    if i not in one:
        fo2.write(i+' ')

fo.close()
fo1.close()
fo2.close()