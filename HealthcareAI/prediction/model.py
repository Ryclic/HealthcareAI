from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.metrics import precision_recall_curve
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from django.conf import settings
import pandas as pd
import numpy as np
import os

csv_path = os.path.join(settings.BASE_DIR, "prediction", "heart.csv")
data = pd.read_csv(csv_path)
data.head()

# converts our nominal values -> ordinal values
le = LabelEncoder()
df1 = data.copy(deep = True)
df1['Sex'] = le.fit_transform(df1['Sex'])
df1['ChestPainType'] = le.fit_transform(df1['ChestPainType'])
df1['RestingECG'] = le.fit_transform(df1['RestingECG'])
df1['ExerciseAngina'] = le.fit_transform(df1['ExerciseAngina'])
df1['ST_Slope'] = le.fit_transform(df1['ST_Slope'])

# from testing, these values are too statistically varied to be used - unnecessary for training
features = df1[df1.columns.drop(['HeartDisease','RestingBP','RestingECG'])].values
target = df1['HeartDisease'].values
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size = 0.20, random_state = 2)

def model(classifier):
    classifier.fit(x_train,y_train)
    # repeatedly input all training cases
    prediction = classifier.predict(x_test)
    cv = RepeatedStratifiedKFold(n_splits = 10,n_repeats = 3,random_state = 1)
    # print("Accuracy : ",'{0:.2%}'.format(accuracy_score(y_test,prediction)))

def predict(user_data):
    # more iterations to ensure convergence
    classifier_lr = LogisticRegression(solver="lbfgs", max_iter=1000)
    model(classifier_lr)
    # two ways of predicting, either give exact or get result
    predicted_class = classifier_lr.predict(user_data)
    predicted_proba = classifier_lr.predict_proba(user_data)

    if predicted_class == 1:
        predicted_class = True
    else:
        predicted_class = False

    return [predicted_class, predicted_proba]

#sample_data = np.array([[24, 1, 0, 198, 0, 140, 0, 0, 2]])
#result = predict(sample_data)
#print(result)

#print(f"Probability of no heart failure: {predicted_proba[0][0]}")
#print(f"Probability of heart failure: {predicted_proba[0][1]}")

#if predicted_class == 1:
#    print("Heart failure predicted.")
#else:
#    print("Heart failure not predicted.")
