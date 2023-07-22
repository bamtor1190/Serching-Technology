import math
import matplotlib.pyplot as plt
import keras
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# csvファイル参照
file = pd.read_csv("csv/samsung.csv")

# 訓練用データ、テスト用データの準備
training_data = file.iloc[:1500, 1:2]
test_data = file.iloc[1500:, 1:2]

# 0, 1範囲に正規化
mmsc = MinMaxScaler(feature_range = (0, 1))
scaled_training_data = mmsc.fit_transform(training_data)

X_train = []
Y_train = []
X_test = []

# 時計列データ
for i in range(60, 1500):
    X_train.append(scaled_training_data[i-60:i, 0])
    Y_train.append(scaled_training_data[i, 0])
    
X_train = np.array(X_train)
Y_train = np.array(Y_train)

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
# (640, 60, 1)

# LSTM
model = Sequential()

model.add(LSTM(units = 20, return_sequences = True, input_shape = (X_train.shape[1], 1)))

model.add(LSTM(units = 20, return_sequences = True))
model.add(Dropout(0.2))

model.add(LSTM(units = 20, return_sequences = True))
model.add(Dropout(0.2))

model.add(LSTM(units = 20))

model.add(Dense(units = 1))

model.compile(optimizer = 'adam', loss = 'mean_squared_error')

model.fit(X_train, Y_train, epochs = 100, batch_size = 32)


total_dataset = pd.concat((training_data, test_data), axis = 0)

inputs = total_dataset[:len(total_dataset) - len(test_data) - 60].values
inputs = inputs.reshape(-1, 1)
inputs = mmsc.transform(inputs)
# (640, 1)

for i in range(60, 1017):
    X_test.append(inputs[i-60:i, 0])

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# 推定された値
predicted_stock_price = model.predict(X_test)
predicted_stock_price = mmsc.inverse_transform(predicted_stock_price)

# 推定結果をplot
plt.plot(file.loc[1500:, '日付け'],test_data.values, color = 'red', label = 'Real Samsung Stock Price')
plt.plot(file.loc[1500:, '日付け'],predicted_stock_price, color = 'blue', label = 'Predicted Samsung Stock Price')

plt.xticks(np.arange(0,957,150))

plt.title('Samsung Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Samsung Stock Price')
plt.legend()
plt.show()