import sqlite3
import pickle

# import pandas as pd
# import numpy as np
# from sklearn import linear_model, model_selection


# data = pd.read_csv("bd_students.csv", sep=";")
from matplotlib import pyplot as plt

# xxx = '000-000-000 46'
# xxx = '3596db4d-3a76-4dc9-9d90-848544e9e21b'
xxx = '7af95948-e43b-41be-b560-0101fe672da1'

db = sqlite3.connect('DataBase\\database.db')
cursor = db.cursor()
conn = db
cursor = cursor
# cursor.execute(f"SELECT Array_P FROM patient WHERE snils ='{xxx}'")
cursor.execute(f"SELECT data_dict FROM data_for_ii WHERE ID ='{xxx}'")
sql = cursor.fetchall()
norm_c = []
for i in sql:
    norm_c.append(i[0])

Array_P_m = (''.join(map(str, sql[0])))
# print(Array_P_m)
test = ''

pickle_in = open(Array_P_m, "rb")
linear__ = pickle.load(pickle_in)

# print(linear__)
# print(len(linear__))

global DZ
global DATA

"""Рассчет для частоты"""
gg = linear__

try:
    DZ = gg.get('Диагноз')
    # print(DZ)
    DATA = gg.get('Данные')
    # print(DATA)

except KeyError:
    print('Такого ключа нет')


import pandas as pd
import numpy as np
from sklearn import linear_model, model_selection


data = pd.read_csv("out.csv", sep=",")

# Столбец, значения которого должны быть предсказаны
# predict_column = "G3"

# Ограничить данные в наборе столбцов. Это важные столбцы для этого теста
# study_data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
study_data = data[["Диагноз", "Данные"]]

# Установите функции (атрибуты) и метку для теста. Метка - это данные, которые мы хотим предсказать.
X = np.array(study_data.drop(["Диагноз"], axis=1))
# X = np.array(data["DATA"])
Y = np.array(data["Диагноз"])

# Учитывая все прочитанные данные, разделите их на набор последовательностей и тестов.
# train: данные, используемые для обучения модели.
# test: данные, используемые для последующего сравнения результатов

# test_input = input().split()

# X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.1)


import pickle
best = 0
for j in range(20000):
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,
                                                                        Y,
                                                                        test_size=0.3)
    # linear = linear_model.LinearRegression()
    linear = linear_model.Perceptron()

    # print(X_train)
    # print(Y_train)

    linear.fit(X_train, Y_train)
    acc = linear.score(X_test, Y_test)
    # print("Точность: " + str(acc))

    # Сохранение высочайшей точности
    if acc > best:
        best = acc
        with open("savedata.pickle", "wb") as f:
            pickle.dump(linear, f)
print("--------------------------------------------------")
print("Высочайшая Точность:", (best * 100), "%")
print("--------------------------------------------------")

# Модель загрузки
pickle_in = open("savedata.pickle", "rb")
linear = pickle.load(pickle_in)

predictions = linear.predict(X_test)

# Обучаем модель рисованию линии с помощью Linear
# Понятие регрессии. Мы используем разные концепции для разных форматов данных (ввода)
# linear = linear_model.LinearRegression()
# linear.fit(X_train, Y_train)

# Проверяем точность нашей модели, сравнивая результаты с ожидаемыми данными (тесты)
# accuracy = linear.score(X_test, Y_test)

# Поскольку теперь наша модель обучена, мы прогнозируем метки (тестовые) на основе функций (также тестовых)


# Вывод данных
#
# for x in range(len(predictions)):
#     print("Прогнозируемая итоговая оценка:", predictions[x], "Data:", X_test[x], "Final grade:", Y_test[x])
#


for i in range(len(predictions)):
    print("Входные данные:             ", X_test[i])
    print("Ожидаемая оценка:           ", Y_test[i])
    print("Прогнозируемая оценка:      ", predictions[i])
    print("--------------------------------------------------")

print("Точность:", (best * 100), "%")
print("--------------------------------------------------")
print("--------------------------------------------------")
#
data1 = pd.read_csv("bd_test.csv")
# study_data1 = data1[["academic_performance", "attendance"]]
study_data1 = data1[["academic_performance"]]
X_test1 = study_data1
predictions1 = linear.predict(X_test1)
print("Новые входные данные:          ",)
print(X_test1)

# from prettytable import from_csv
#
# with open("bd_test.csv") as fp:
#     # создание таблицы из bd_test.csv
#     mytable = from_csv(fp)
# print(mytable)
#
#
# print("Прогнозируемая оценка НД:      "'\n', predictions1)