import svmdota_win
import sys
import random
import numpy as np
sys.path.append('F:\libsvm-3.22\python')
from svmutil import *
# svmdota_win.dotaPSO('C:/Users/NanZhi Wang/PycharmProjects\svmdota/standatatrain_wonbs.txt',10)
# svmdota_win.dotaPSO('standata.txt',10)


# y, x = svm_read_problem('standatatrain.txt')
with open('standatatrain.txt') as fo:
    for i in fo.readlines():
        print(i)
print(1)
model = svm_train(y[0:30000], x[0:30000], '-c 1 -g 0.07')
print(2)
p_label, p_acc, p_val = svm_predict(y[30001:],x[30001:], model)
cv = p_acc[0]
print(cv)