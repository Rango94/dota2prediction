import matplotlib.pyplot as plt
import numpy as np
pre=np.load('pre30.npy')
maxl=0
for i in range(len(pre)):
    tmp=pre[i].copy()
    for j in range(len(pre[i])):
        tmp[j]=(pre[i][j]-min(pre[i]))/(max(pre[i])-min(pre[i]))
    pre[i]=tmp
    if len(pre[i])>maxl:
        maxl=len(pre[i])

n=0
for y in [pre[66],pre[24],pre[76]]:
    n+=1
    print(y)
    print(n)
    x=np.arange(0, len(y), 1)
    # fig = plt.figure()
    # plt.figure(figsize=(19, 12))
    plt.axis([0, maxl, 0, 1])
    plt.xlabel('time (min)')
    plt.ylabel('frequency')
    plt.plot(x, y)
    # plt.savefig("C:/Users/NanZhi Wang\Desktop\dota2plot/"+str(n)+'.jpg')
plt.show()
