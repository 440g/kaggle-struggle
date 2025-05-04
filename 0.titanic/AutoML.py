import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score

pd = pd.read_csv('dataset/train_modified.csv')

y = pd["Survived"]
X = pd.drop(["Survived"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


automl = AutoML(
    mode="Compete",
    explain_level=1
)

automl.fit(X_train, y_train) 
preds = automl.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))

automl.report()

leaderboard = automl.get_leaderboard()
print(leaderboard[["model_type", "metric_value", "train_time"]])
