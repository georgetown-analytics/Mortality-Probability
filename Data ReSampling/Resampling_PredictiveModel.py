# Importing the libraries
import plotly
%matplotlib inline
import numpy as np
import pandas as pd
from ipywidgets import widgets
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.metrics import auc
from IPython.html.widgets import *
import statsmodels.formula.api as sm
from sklearn.metrics import roc_curve
from sklearn.decomposition import PCA
from imblearn.combine import SMOTEENN
from imblearn.pipeline import Pipeline
from imblearn.combine import SMOTETomek
from imblearn.over_sampling import SMOTE
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split as tts
from imblearn.metrics import sensitivity_specificity_support

# Importing the dataset
dataset = pd.read_csv('6c_Updated_Data.csv')
X = dataset.drop(['Record','IndDea','Age','Age_Cat35','HispOr','Educ_CollgCompl','NotInPoverty','Res_Pacific'], axis=1)
y = dataset.loc[:, 'IndDea']
IndDea = dataset.IndDea.value_counts()
print('Survived:', IndDea[0])
print('Died:', IndDea[1])
print('Proportion:', round(IndDea[0] / IndDea[1], 2), ': 1')
my_colors = 'gbykmc'
IndDea.plot(kind='bar', title='Class Counts', color=my_colors)

# Splitting the dataset into the Training set and Test set prior to fitting / resampling
X_train, X_test, y_train, y_test = tts(X, y, test_size = 0.2, random_state = 0)

# Identify statistically significant variables 
regressor_OLS = sm.OLS(endog = y_train, exog = X_train).fit()
regressor_OLS.summary()

#Logistic Regression
logreg = LogisticRegression(C=1)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print(cm)
def plot_confusion(cm):
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.binary)
    plt.title('Confusion matrix')
    plt.set_cmap('Reds')
    plt.colorbar()
    target_names = ['survived', 'died']
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=60)
    plt.yticks(tick_marks, target_names)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()    
plot_confusion(cm)
print(cm.astype(np.float64) / cm.sum(axis=1, keepdims=1))
print(sensitivity_specificity_support(y_test, y_pred, average='weighted')) #Sensitivity (ratio TP / (TP + FN) - quantifies the ability to avoid false negatives)
print(recall_score(y_test, y_pred)) #The recall is intuitively the ability of the classifier to find all the positive samples

# Random Forest Classifier
clf_rf = RandomForestClassifier(n_estimators=25, random_state=12)
clf_rf.fit(X_train, y_train)
y_pred_rf = clf_rf.predict(X_test)
accuracy_score(y_test, y_pred_rf)
cm = confusion_matrix(y_test, y_pred_rf)
print(cm)
def plot_confusion(cm):
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.binary)
    plt.title('Confusion matrix')
    plt.set_cmap('Reds')
    plt.colorbar()
    target_names = ['survived', 'died']
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=60)
    plt.yticks(tick_marks, target_names)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()    
plot_confusion(cm)
print(cm.astype(np.float64) / cm.sum(axis=1, keepdims=1))
print(sensitivity_specificity_support(y_test, y_pred_rf, average='weighted'))
print(recall_score(y_test, y_pred_rf))

# Pipeline
pca = PCA()
smt = SMOTE(random_state=42)
knn = KNN()
pipeline = Pipeline([('smt', smt), ('pca', pca), ('knn', knn)])
pipeline.fit(X_train, y_train) 
y_pred_ppl = pipeline.predict(X_test)
accuracy_score(y_test, y_pred_ppl)
cm = confusion_matrix(y_test, y_pred_ppl)
print(cm)
def plot_confusion(cm):
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.binary)
    plt.title('Confusion matrix')
    plt.set_cmap('Reds')
    plt.colorbar()
    target_names = ['survived', 'died']
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=60)
    plt.yticks(tick_marks, target_names)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()    
plot_confusion(cm)
print(cm.astype(np.float64) / cm.sum(axis=1, keepdims=1))
print(sensitivity_specificity_support(y_test, y_pred_ppl, average='weighted'))
print(recall_score(y_test, y_pred_ppl))

# Principal Component Analysis (PCA) + Logistic Regression ----- DOES NOT RECOGNIZE Class IndDea=1
pca = PCA(n_components=2)
pca.fit(X_train)
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
logisticRegr = LogisticRegression(solver = 'lbfgs')
logisticRegr.fit(X_train_pca, y_train)
y_pred_pca = logisticRegr.predict(X_test_pca)
def plot_2d_space(X_test_pca, y_pred_pca, label='Classes'):   
    colors = ['#1F77B4', '#FF7F0E']
    markers = ['o', 's']
    for l, c, m in zip(np.unique(y_pred_pca), colors, markers):
        plt.scatter(
            X_test_pca[y_pred_pca==l, 0],
            X_test_pca[y_pred_pca==l, 1],
            c=c, label=l, marker=m
        )
    plt.title(label)
    plt.legend(loc='upper right')
    plt.show()
plot_2d_space(X_test_pca, y_pred_pca, 'Imbalanced dataset (2 PCA components)')
accuracy_score(y_test, y_pred_pca)
cm = confusion_matrix(y_test, y_pred_pca)
print(cm)
def plot_confusion(cm):
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.binary)
    plt.title('Confusion matrix')
    plt.set_cmap('Reds')
    plt.colorbar()
    target_names = ['survived', 'died']
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=60)
    plt.yticks(tick_marks, target_names)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()    
plot_confusion(cm)
print(cm.astype(np.float64) / cm.sum(axis=1, keepdims=1))
print(sensitivity_specificity_support(y_test, y_pred_smt, average='weighted'))
print(recall_score(y_test, y_pred_smt))

# SMOTETomek (Over + Under Sampling) + Logistic Regression
print('Original dataset shape {}'.format(Counter(y_train)))
smt = SMOTETomek(ratio='auto')
X_train_smt, y_train_smt = smt.fit_sample(X_train, y_train)
print('Resampled dataset shape {}'.format(Counter(y_train_smt)))
logreg = LogisticRegression(C=1)
logreg.fit(X_train_smt, y_train_smt)
y_pred_smt = logreg.predict(X_test)
accuracy_score(y_test, y_pred_smt)
cm = confusion_matrix(y_test, y_pred_smt)
print(cm)
def plot_confusion(cm):
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.binary)
    plt.title('Confusion matrix')
    plt.set_cmap('Reds')
    plt.colorbar()
    target_names = ['survived', 'died']
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=60)
    plt.yticks(tick_marks, target_names)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()    
plot_confusion(cm)
print(cm.astype(np.float64) / cm.sum(axis=1, keepdims=1))
print(sensitivity_specificity_support(y_test, y_pred_smt, average='weighted'))
print(recall_score(y_test, y_pred_smt))
y_pred_smt_proba = logreg.predict_proba(X_test)
y_pred_smt_proba[:5]
def plot_roc_curve(y_test, y_pred_smt_proba):
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_smt_proba[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label='ROC curve (area = %0.3f)' % roc_auc)
    plt.plot([0, 1], [0, 1], 'k--')  # random predictions curve
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate or (1 - Specifity)')
    plt.ylabel('True Positive Rate or (Sensitivity)')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
plot_roc_curve(y_test, y_pred_smt_proba)

# SMOTEENN algorithm + Logistic Regression
sme = SMOTEENN(random_state=42)
X_train_sme, y_train_sme = sme.fit_sample(X_train, y_train)
#Saving resampled data to a csv file for later access
df_X = pd.DataFrame(X_train_sme)
df_X.to_csv("6c_ResampledData_X_train.csv", encoding='utf-8', index=False)
df_y = pd.DataFrame(y_train_sme)
df_y.to_csv("6c_ResampledData_y_train.csv", encoding='utf-8', index=False)
logreg = LogisticRegression(C=1)
logreg.fit(X_train_sme, y_train_sme)
y_pred_sme = logreg.predict(X_test)
accuracy_score(y_test, y_pred_sme)
cm = confusion_matrix(y_test, y_pred_sme)
print(cm)
def plot_confusion(cm):
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.binary)
    plt.title('Confusion matrix')
    plt.set_cmap('Reds')
    plt.colorbar()
    target_names = ['survived', 'died']
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=60)
    plt.yticks(tick_marks, target_names)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()    
plot_confusion(cm)
print(cm.astype(np.float64) / cm.sum(axis=1, keepdims=1))
print(sensitivity_specificity_support(y_test, y_pred_sme, average='weighted'))
print(recall_score(y_test, y_pred_sme))
y_pred_sme_proba = logreg.predict_proba(X_test)
y_pred_sme_proba[:5]
def plot_roc_curve(y_test, y_pred_sme_proba):
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_sme_proba[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label='ROC curve (area = %0.3f)' % roc_auc)
    plt.plot([0, 1], [0, 1], 'k--')  # random predictions curve
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate or (1 - Specifity)')
    plt.ylabel('True Positive Rate or (Sensitivity)')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
plot_roc_curve(y_test, y_pred_sme_proba)
