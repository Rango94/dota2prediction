import sys
import random
import numpy as np
sys.path.append('F:\libsvm-3.22\python')
from svmutil import *
# y,x= svm_read_problem('D:/pythonwork/svm/standatatrain.txt')
# m=svm_train(y[:2000],x[:2000],"-c 1 -g 0.07")
# p_label,p_acc,p_val=svm_predict(y[2000:5000],x[2000:5000],m)
def dotaPSO(ads,n):
    y, x = svm_read_problem(ads)
    margin = 0
    if len(y) > 10000:
        margin = len(y) - 10001
    if len(y) <= 10000:
        margin = int(len(y) / 2)
    canshu = np.zeros((2, n))
    canshu[0, 0] = 2.7942
    canshu[1, 0] = 0.0342
    bestc = canshu[0, 0]
    bestg = canshu[1, 0]
    bestsinglecv = np.zeros((1, n))
    bestsinglec = np.zeros((1, n))
    bestsingleg = np.zeros((1, n))
    bestcv = 0
    v = np.zeros((2, n))
    for i in range(1, n):
        canshu[0, i] = 0.2 + 8 * random.random()
        canshu[1, i] = 0.5 * random.random()
    while 1 == 1:
        for i in range(0, n):
            c = canshu[0, i]
            g = canshu[1, i]
            print("bestc:", bestc)
            print("bestg:", bestg)
            print("bestcv:", bestcv)
            print('-----------------')

            cmd = '-c ' + str(c) + ' -g ' + str(max(g, 0.001)) + ' -h 0'
            start = int(margin * random.random())
            model = svm_train(y[start:min(start + 10000, len(y) - 1)], x[start:min(start + 10000, len(y) - 1)], cmd)
            start = start + 10000
            p_label, p_acc, p_val = svm_predict(y[start:min(start + 10000, len(y) - 1)],
                                                x[start:min(start + 10000, len(y) - 1)], model)
            cv = p_acc[0]
            print('xxxxxxxxxxxxxxxxxxxx',cv)
            if cv >= bestsinglecv[0, i]:
                bestsinglecv[0, i] = cv
                bestsinglec[0, i] = c
                bestsingleg[0, i] = g
        print('bestsinglecv:', bestsinglecv)
        print('bestsinglec:', bestsinglec)
        print('bestsingleg:', bestsingleg)

        index = np.argmax(bestsinglecv)
        bestcv = max(bestsinglecv)
        bestc = bestsinglec[0, index]
        bestg = bestsingleg[0, index]
        with open('log.txt','a') as fo:
            fo.write(str(bestcv)+' '+str(bestc)+' '+str(bestg))
        for i in range(n):
            v[0, i] = 0.5 * v[0, i] + random.random() * (bestsinglec[0, i] - canshu[0, i]) + random.random() * (
            bestc - canshu[0, i])
            if v[0, i] >= 0.5:
                v[0, i] = 0.5
            elif v[0, i] <= -0.5:
                v[0, i] = -0.5
            canshu[0, i] = max(canshu[0, i] + v[0, i],0.0001)
            v[1, i] = 0.5 * v[1, i] + random.random() * (bestsingleg[0, i] - canshu[1, i]) + random.random() * (
            bestg - canshu[1, i])
            if v[1, i] >= 0.5:
                v[1, i] = 0.5
            elif v[1, i] <= -0.5:
                v[1, i] = -0.5
            canshu[1, i] = max(0.0001,canshu[1, i] + v[1, i])
            print(canshu)

