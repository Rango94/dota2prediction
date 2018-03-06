import numpy as np
pre30=np.load('pre30.npy')
hero=np.zeros((114,))
n=0
for i in pre30:
    add=0
    for j in range(len(i)):
        add+=j*i[j]
    if n!=23:
        hero[n]=float(add/(np.mean(i)*len(i)))
    else:
        hero[n]=40
    n+=1
new=hero.copy()

for i in range(len(new)):
    new[i]=(hero[i]-min(hero))/(max(hero)-min(hero))
print(new.tolist())