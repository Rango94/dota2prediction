import numpy as np
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
from sklearn.linear_model import Ridge
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
import cache
def acc(x,b):
    a=x.copy()
    for i in range(len(a)):
        if a[i]==b[i]:
            a[i]=1
        else:
            a[i]=0
    return a
max=0
while 1==1:
    print('读数据')
    X,Y,cnn=cache.rawstand('cleardatabig_whole.txt')
    # X=np.load('tmpX.npy')
    # Y=np.load('tmpY.npy')
    magin=int(len(Y)*0.85)
    expected = Y[magin:]
    # if __name__=='__main__':
    #     param_grid = {"C": [i*(1.5/100)+0.5 for i in range(100)],
    #                   "solver": ['lbfgs', 'sag'],
    #                  }
    print("开始预测")
    model = LogisticRegression(solver='sag',max_iter=200,n_jobs=-1)
    #     # clf=RandomizedSearchCV(model,param_grid,scoring='accuracy',n_jobs=6,cv=3)
    model.fit(X[:magin], Y[:magin])
    #     # print(clf.best_score_)
    #     # print(clf.best_params_)
    predicted = model.predict(X[magin:])
    accc=np.mean(acc(predicted,expected))
    if max<accc:
        max=accc
        print(accc)
        print(cnn)
        print(metrics.classification_report(expected, predicted, digits=5))
        print(metrics.confusion_matrix(expected, predicted))




#
# model=RandomForestClassifier(n_estimators=1000,n_jobs=-1)
# model.fit(X[:magin], Y[:magin])
# predicted = model.predict(X[magin:])
# print(metrics.classification_report(expected, predicted,digits=5))
# print(metrics.confusion_matrix(expected, predicted))

# model = MLPClassifier(activation='relu', alpha=1e-5,hidden_layer_sizes=(150,10),learning_rate='adaptive',max_iter=500,tol=0.0001,random_state=1)
# model.fit(X[:magin], Y[:magin])
# predicted = model.predict(X[magin:])
# print(metrics.classification_report(expected, predicted,digits=5))
# print(metrics.confusion_matrix(expected, predicted))


# if __name__=='__main__':
#     param_grid = {"C": [i*(2.3/100)+0.7 for i in range(100)],
#                   "gamma": [i*(1/100) for i in range(100)],
#                  }
#     model = SVC()
#     clf = RandomizedSearchCV(model, param_grid, scoring='accuracy', n_jobs=6, cv=3)
#     clf.fit(X[:10000], Y[:10000])
#     print(clf.best_score_)
#     print(clf.best_params_)


# predicted = model.predict(X[magin:])
# print(metrics.classification_report(expected, predicted,digits=5))
# print(metrics.confusion_matrix(expected, predicted))

# model=GaussianNB()
# model.fit(X[:magin], Y[:magin])
# predicted = model.predict(X[magin:])
# print(metrics.classification_report(expected, predicted,digits=5))
# print(metrics.confusion_matrix(expected, predicted))

