def findsubstrnum(s,ss):
    out = []
    if s=='canzhan':
        out1=findsubstrnum('kills":',ss)
        out2=findsubstrnum('assists":',ss)
        out3=findsubstrnum('radiant_score":',ss)
        out4=findsubstrnum('dire_score":',ss)
        try:
            for i in range(0,5):
                out.append(float((out1[i]+out2[i])/out3[0]))
            for i in range(5,10):
                out.append(float((out1[i] + out2[i]) / out4[0]))
            return out
        except:
            return False
    else:
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

fo=open('newdatafirst.txt')
fo1=open('herosmark.txt','w')
tmp=[]
mex=[]
xx=[]
for i in range(0,114):
    xx.append(0)
for i in range(0,114):
    tmp.append(i+1)
for i in range(0, 6):
    mex.append(xx.copy())
mex[0]=tmp
substr = []
substr.append('"hero_id":')
substr.append('"hero_damage":')
substr.append('"tower_damage":')
substr.append('"hero_healing":')
substr.append('canzhan')
for line in fo:
    tmp_mex=[]
    for substrs in substr:
        out = findsubstrnum(substrs, line)
        if out!=False:
            tmp_mex.append(out)
        else:
            tmp_mex=0
            break
    if tmp_mex!=0:
        for i in range(0,10):
            mex[1][tmp_mex[0][i]-1]=mex[1][tmp_mex[0][i]-1]+tmp_mex[1][i]
            mex[2][tmp_mex[0][i] - 1] = mex[2][tmp_mex[0][i] - 1] + tmp_mex[2][i]
            mex[3][tmp_mex[0][i] - 1] = mex[3][tmp_mex[0][i] - 1] + tmp_mex[3][i]
            mex[4][tmp_mex[0][i] - 1] = mex[4][tmp_mex[0][i] - 1] + tmp_mex[4][i]
            mex[5][tmp_mex[0][i] - 1] = mex[5][tmp_mex[0][i] - 1] + 1

for i in range(0,6):
    for j in range(0,114):
        if j!=23:
            fo1.write(str(float(mex[i][j]/mex[5][j]))+" ")
        else:
            fo1.write(str(0) + " ")
    fo1.write('\n')
fo1.close()
fo.close()