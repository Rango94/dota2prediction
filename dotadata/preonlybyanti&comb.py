


data=open('cleardatatest.txt')
antif=open('antinum.txt')
combf=open('combnum.txt')
anti=[]
comb=[]

for line in antif:
    line=line.split()
    anti.append(line)
for line in combf:
    line=line.split()
    comb.append(line)

count=0
c=0
for line in data:
    c=c+1
    line=line.split(" ")
    xs=[]
    for i in range(0,10):
        tmp = 0
        if i<=4:
            for j in range(0,10):
                if j<=4:
                    tmp=tmp+float(comb[int(line[i])-1][int(line[j])-1])
                else:
                    tmp = tmp + float(anti[int(line[i]) - 1][int(line[j]) - 1])
        else:
            for j in range(0,10):
                if j<=4:
                    tmp=tmp+float(anti[int(line[i])-1][int(line[j])-1])
                else:
                    tmp = tmp + float(comb[int(line[i]) - 1][int(line[j]) - 1])
        xs.append((tmp))
    # print(xs)
    ra=0
    di=0
    for i in range(0,10):
        if i<=4:
            ra=ra+xs[i]
        else:
            di=di+xs[i]
    out=0
    if ra<di:
        out=1
    else:
        out=-1
    if str(out)==line[len(line)-1].strip('\n'):

        count=count+1
print(count)
print(float(count/c))