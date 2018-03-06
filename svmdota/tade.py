from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.cross_validation import cross_val_score, ShuffleSplit
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import sys
import pandas as pd
from sklearn.neural_network import MLPClassifier
import xgboost as xgb

# matches = pd.read_csv('matches_dota.csv.bz2', compression = 'bz2')
# matches = matches.drop_duplicates()
# # print(matches.head())
# np.set_printoptions(threshold=np.NaN)
# normal_skill = matches[matches['skill'] == 1]
# # print(normal_skill)
# rad_heroes = ['r1_hero_id', 'r2_hero_id', 'r3_hero_id', 'r4_hero_id', 'r5_hero_id']
# dire_heroes = ['d1_hero_id', 'd2_hero_id', 'd3_hero_id', 'd4_hero_id', 'd5_hero_id']
# X_normal = np.zeros([normal_skill.shape[0], 226])
# X_normal[np.tile(np.arange(normal_skill.shape[0]),[5,1]).T.ravel(),
#             normal_skill[rad_heroes].as_matrix().ravel() - 1] = 1.0
# X_normal[np.tile(np.arange(normal_skill.shape[0]),[5,1]).T.ravel(),
#             normal_skill[dire_heroes].as_matrix().ravel() + 112] = 1.0
# y_normal = normal_skill['radiant_win'].as_matrix()



import cache
# X=X_normal[:30000]
# y=y_normal[:30000]
# X=cache.chulitadeshuju(X)
X=np.load('X_whole.npy')
y=np.load('Y_whole.npy')
X=cache.chulitadeshuju(X)
for i in range(len(y)):
    y[i]=max(0,y[i])
np.set_printoptions(threshold=np.NaN)
# print(X[100:105])
# print(y[100:105])

cv = ShuffleSplit(n=X.shape[0], n_iter=5, random_state=123, test_size=0.15)
for sc in ('f1', 'accuracy', 'precision', 'recall'):
    score = cross_val_score(
        LogisticRegression(),
        X, y,
        cv=cv,
        scoring=sc
    )
    print(sc, score.mean())

ind = np.argsort(np.random.rand(len(X)))
tr_ind = ind[:int(len(ind) * 85 / 100)]
test_ind = ind[int(len(ind) * 85 / 100):]
dtrain = xgb.DMatrix(X[tr_ind, :], label = y[tr_ind])
dtest = xgb.DMatrix(X[test_ind, :], label = y[test_ind])
param = {'bst:max_depth':6, 'bst:eta':0.4, 'silent':1, 'objective':'binary:logistic' }
param['nthread'] = 4
param['eval_metric'] = ['auc', 'logloss']
evallist  = [(dtest,'eval'), (dtrain,'train')]
num_round = 200
bst = xgb.train( param, dtrain, num_round, evallist, verbose_eval = 10 )



# cv = ShuffleSplit(n=X.shape[0], n_iter=5, random_state=123, test_size=0.15)
# for sc in ('f1', 'accuracy', 'precision', 'recall'):
#     score = cross_val_score(
#         RandomForestClassifier(n_estimators=250, n_jobs=-1),
#         X, y,
#         cv=cv,
#         scoring=sc
#     )
#     print(sc, score.mean())
#     sys.stdout.flush()

    # f1
    # 0.663536428096
    # accuracy
    # 0.617111111111
    # precision
    # 0.627062518644
    # recall
    # 0.708983756967


    # roc_auc
    # 0.686079766909
    # log_loss - 0.636024839982