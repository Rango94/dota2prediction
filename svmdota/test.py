import numpy as np
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.linear_model import Ridge
from sklearn.grid_search import GridSearchCV
X=np.load('X_.npy')
Y=np.load('Y.npy')

# scaler = StandardScaler()
# scaler.fit(X[:30000])
# X=scaler.transform(X)
model1 = LogisticRegression()
model2=RandomForestClassifier(n_estimators=250,n_jobs=-1)
model3 = MLPClassifier(solver='sgd', alpha=1e-5,hidden_layer_sizes=(100,2),learning_rate='adaptive',max_iter=200,tol=0.0001,
                      random_state=1)
model4=SVC()
model1.fit(X[:30000], Y[:30000])
model2.fit(X[:30000], Y[:30000])
model3.fit(X[:30000], Y[:30000])
model4.fit(X[:30000], Y[:30000])
print(model1)
# make predictions
expected = Y[30001:]
predicted = model1.predict(X[30001:])
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
with open('prediction.txt','a') as fo:
    for i in predicted:
        fo.write(str(i)+' ')
    fo.write('\n')
predicted = model2.predict(X[30001:])
out1=predicted.copy()
np.save('out1',out1)
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
with open('prediction.txt','a') as fo:
    for i in predicted:
        fo.write(str(i)+' ')
    fo.write('\n')
predicted = model3.predict(X[30001:])
out2=predicted.copy()
np.save('out2',out2)
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
with open('prediction.txt','a') as fo:
    for i in predicted:
        fo.write(str(i)+' ')
    fo.write('\n')
predicted = model4.predict(X[30001:])
out3=predicted.copy()
np.save('out3',out3)
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
with open('prediction.txt','a') as fo:
    for i in predicted:
        fo.write(str(i)+' ')
    fo.write('\n')



# aft_model=joblib.load('after_model.m')
# out1=np.load('out1.npy')
# out2=np.load('out2.npy')
# out3=np.load('out3.npy')
# out=[out1.copy(),out2.copy(),out3.copy()]
# out4=out3.copy()
# n=0
# N=0
# sta=[]
# for i in range(len(out1)):
#     one=0
#     zero=0
#     for j in range(3):
#         if out[j][i]==1:
#             one+=1
#         if out[j][i]==-1:
#             zero+=1
#     if zero==0:
#         out4[i]=1
#     if one==0:
#         out4[i]=-1
#     if one!=0 and zero!=0:
#         predicted = aft_model.predict(np.array([[out1[i],out2[i],out3[i]]]))
#         out4[i]=predicted[0]
        # sta.append([out1[i],out2[i],out3[i],expected[i]])
        # # print(out1[i],out2[i],out3[i],expected[i])
        # N+=1
        # if out4[i]==expected[i]:
        #     n+=1
# print(n/N)


# from sklearn.externals import joblib
# sta=np.array(sta)
# model=RandomForestClassifier(n_estimators=250,n_jobs=-1)
# model.fit(sta[:,:3],sta[:,3])
# joblib.dump(model, "after_model.m")
# with open('prediction.txt','a') as fo:
#     for i in out4:
#         fo.write(str(i) + ' ')
#     fo.write('\n')
# with open('prediction.txt', 'a') as fo:
#     for i in expected:
#         fo.write(str(i) + ' ')
# print(metrics.classification_report(expected, out4))
# print(metrics.confusion_matrix(expected, out4))
# summarize the fit of the model
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))




# with open('cleardatabig.txt') as fo:
#     fo=fo.readlines()
#     X_=[[int(line.split()[i]) for i in range(10)] for line in fo]
#     Y=[int(line.split()[10]) for line in fo]
#     X_ = np.array(X_)
#     Y = np.array(Y)
#     X=np.zeros((len(X_),228))
#     for i in range(len(X_)):
#         for j in range(5):
#             X[i,X_[i,j]-1]=1
#         for j in range(5,10):
#             X[i, X_[i, j]+113] = 1
#     np.save('X',X)
#     np.save('Y',Y)
