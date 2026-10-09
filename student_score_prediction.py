Student Score Prediction

My first Machine Learning project

import pandas as pd
from sklearn.linear_model import LinearRegression

Create a small dataset

data = {
"Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
"Scores": [20, 25, 40, 45, 60, 65, 75, 85]
}

Convert the data into a DataFrame

df = pd.DataFrame(data)

Select the input feature and target

X = df[["Hours_Studied"]]
y = df["Scores"]

Create and train the model

model = LinearRegression()
model.fit(X, y)

Predict the score for 9 hours of study

predicted_score = model.predict(pd.DataFrame({"Hours_Studied": [9]}))

print("Student Score Prediction")
print("Hours studied:", 9)
print("Predicted score:", round(predicted_score[0], 2))