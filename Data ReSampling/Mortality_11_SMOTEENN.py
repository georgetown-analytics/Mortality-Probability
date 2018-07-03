# Importing the libraries
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.combine import SMOTEENN
from sklearn.metrics import confusion_matrix

# Importing the dataset
dataset = pd.read_csv('11_Updated_Data.csv')
X = dataset.drop(['Record','IndDea','Age','Age_Cat35','HispOr','Educ_CollgCompl','NotInPoverty','Res_Pacific'], axis=1)
y = dataset.loc[:, 'IndDea']

# Fixing class imbalance by applying SMOTEENN algorithm
X, y = make_classification(n_classes=2, class_sep=2,
weights=[0.1, 0.9], n_informative=32, n_redundant=0, flip_y=0,
n_features=32, n_clusters_per_class=1, n_samples=1008826, random_state=10)

sme = SMOTEENN(random_state=42)
X_res, y_res = sme.fit_sample(X, y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size = 0.2, random_state = 0)

# Identify statistically significant variables
import statsmodels.formula.api as sm
regressor_OLS = sm.OLS(endog = y_train, exog = X_train).fit()
regressor_OLS.summary()

# Fitting Logistic Regression Model to the training set
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1)
logreg.fit(X_train, y_train)

# Predicting the test set results
y_pred = logreg.predict(X_test)

# Calculating probability instead of binary outcome
y_pred_proba = logreg.predict_proba(X_test)
y_pred_proba[:5]

# PLotting ROC curve
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

def plot_roc_curve(y_test, y_pred_proba):
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label='ROC curve (area = %0.3f)' % roc_auc)
    plt.plot([0, 1], [0, 1], 'k--')  # random predictions curve
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate or (1 - Specifity)')
    plt.ylabel('True Positive Rate or (Sensitivity)')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    
plot_roc_curve(y_test, y_pred_proba)

# Calculating accuracy score for predicted results
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

# Creating confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

def plot_confusion(cm):
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.binary)
    plt.title('Confusion matrix')
    plt.set_cmap('Blues')
    plt.colorbar()

    target_names = ['survived', 'died']

    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=60)
    plt.yticks(tick_marks, target_names)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    
plot_confusion(cm)

print(cm.astype(np.float64) / cm.sum(axis=1))

# Calculating Sensitivity, Specificity and Support: we are interested in Sensitivity (ratio TP / (TP + FN). The specificity quantifies the ability to avoid false negatives).
from imblearn.metrics import sensitivity_specificity_support
sensitivity_specificity_support(y_test, y_pred, average='weighted')

# Calculating Recall Score (The recall is the ratio TP / (TP + FN) where TP is the number of true positives and FN the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples)
from sklearn.metrics import recall_score
print(recall_score(y_test, y_pred))

from sklearn.metrics import precision_score
print(precision_score(y_test, y_pred))
