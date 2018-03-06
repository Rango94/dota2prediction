fo=open('cleardata2.txt')
fo1=open('standata2.txt','w')
fo2=open('newmark.txt')

mark=[]
for line in fo2:
    mark.append(line.split())

print(len(mark[8]))
for line in fo:
    line=line.split(" ")
    fo1.write('%d'%int(line[len(line) - 1])+' ')
    submark1=[]
    for i in range(0,5):
        for j in range(0,len(mark)):
            submark1.append(mark[j][int(line[i])-1])

    submark2 = []
    for i in range(5, 10):
        for j in range(0, len(mark)):
            submark2.append(mark[j][int(line[i])-1])
    line=[0 for i in range(0,len(mark)*5)]
    for i in range(0,len(mark)*5):

        line[i]=float(submark1[i])-float(submark2[i])
    for i in range(0,len(line)):
        fo1.write('%d'%(i+1)+':'+str(line[i])+' ')
    fo1.write('\n')
fo.close()
fo1.close()


