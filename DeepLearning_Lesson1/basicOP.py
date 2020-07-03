import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder



dataset = pd.read_csv("DeepLearning_Lesson1/breastcancer.csv")
#dataset.info()




x = dataset.iloc[:,2:31]
y = dataset.iloc[:,1]

encoder = LabelEncoder()
y = encoder.fit_transform(y)                               ## 0.8951 before scaling
                                                           ## 0.9720 after scaling x values



from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)



X_train, X_test, Y_train, Y_test = train_test_split(X_scaled_array, y,
                                                    test_size=0.25, random_state=87)




np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(30, input_dim=29, activation='relu')) # hidden layer acc 0.6875 w/ just 1
my_first_nn.add(Dense(30, input_dim=29, activation='relu')) # hidden layer
my_first_nn.add(Dense(30, input_dim=29, activation='relu')) # hidden layer acc 0.6979 w/ 3
my_first_nn.add(Dense(30, input_dim=29, activation='relu')) # hidden layer acc 0.7500 w/10
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))
