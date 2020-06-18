import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.svm import SVC, LinearSVC


df = pd.read_csv("Python_Lesson4/Python_Lesson4/glass.csv")
X = df.drop("Type", axis =1)
y = df["Type"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state = 0)


#LinearSVC
LinearSVC = SVC(kernel ='linear')
Y_pred = LinearSVC.fit(X_train, y_train).predict(X_test)
acc_LinearSVC = round(LinearSVC.score(X_train, y_train) * 100, 2)
print("Linear SVC accuracy is:", acc_LinearSVC)

#Classification Report
print(classification_report(y_test, Y_pred))