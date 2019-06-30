from sklearn import tree
from sklearn.metrics import accuracy_score
import pandas as pd

filepath = "dataset.csv"
sep = ","
delimiter = None

df = pd.read_csv(filepath, sep=sep, delimiter=delimiter)

x = df[["sbp", "tobacco", "ldl", "adiposity", "chd",
       "typea", "alcohol", "age"]]
y = df["famhist"]

clf = tree.DecisionTreeClassifier()
clf.fit(x,y)

y_pred = clf.predict(x)
print("Akurasi", accuracy_score(y, y_pred))
# show columns
print("Hasil prediksi", clf.predict([[138,3,4,25,52,25,17.42,0]]))
