import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.svm import SVC, LinearSVC



df = pd.read_csv("Python_Lesson4/Python_Lesson4/glass.csv")
X = df.drop("Type", axis =1)
y = df["Type"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state = 0)

#GNB
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
acc_gnb = round(gnb.score(X_train, y_train) * 100, 2)
print("Naïve Bayes accuracy is:", acc_gnb)

#Classification Report
print(classification_report(y_test, y_pred))