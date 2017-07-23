import os
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.naive_bayes import GaussianNB,BernoulliNB
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

data_dir='output/'
data_file = [os.path.join(data_dir,'data_batch_%d.bin'%ii) for ii in [i for i in range(1,11)]]

data = np.concatenate([np.fromfile(open(file, "r"), dtype=np.uint8).reshape(5000,3073) for file in data_file],axis=0).astype('float64')
data_X = data[:,1:]
data_y = data[:,0]

train_X = data_X[:-5000,:]
train_y = data_y[:-5000]

test_X = data_X[-5000:,:]
test_y = data_y[-5000:]

clf = BernoulliNB()
clf.fit(train_X, train_y)
y_pred = clf.predict(test_X)
print("Classification Report:\n%s" % classification_report(test_y, y_pred))
f1_weighted = cross_val_score(clf, data_X, data_y, cv=10, scoring='f1_weighted')
accuracy = cross_val_score(clf, data_X, data_y, cv=10, scoring='accuracy')
precision_weighted = cross_val_score(clf, data_X, data_y, cv=10, scoring='precision_weighted')
recall_weighted = cross_val_score(clf, data_X, data_y, cv=10, scoring='recall_weighted')
print('f1_weighted: ',f1_weighted)
print('accuracy: ',accuracy)
print('precision_weighted: ',precision_weighted)
print('recall_weighted: ',recall_weighted)

clf = RandomForestClassifier(n_estimators=20)
clf.fit(train_X, train_y)
y_pred = clf.predict(test_X)
print("Classification Report:\n%s" % classification_report(test_y, y_pred))
f1_weighted = cross_val_score(clf, data_X, data_y, cv=10, scoring='f1_weighted')
accuracy = cross_val_score(clf, data_X, data_y, cv=10, scoring='accuracy')
precision_weighted = cross_val_score(clf, data_X, data_y, cv=10, scoring='precision_weighted')
recall_weighted = cross_val_score(clf, data_X, data_y, cv=10, scoring='recall_weighted')
print('f1_weighted: ',f1_weighted)
print('accuracy: ',accuracy)
print('precision_weighted: ',precision_weighted)
print('recall_weighted: ',recall_weighted)