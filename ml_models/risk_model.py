# This is a basic example using logistic regression
from sklearn.linear_model import LogisticRegression
import numpy as np
import joblib

# Sample data: [mood, sleep, screen_time]
X = np.array([[8, 7, 3], [5, 5, 6], [3, 4, 8], [9, 8, 2], [4, 3, 9]])
y = np.array([0, 1, 2, 0, 2])  # 0=Low, 1=Medium, 2=High

model = LogisticRegression(solver='lbfgs')
model.fit(X, y)
joblib.dump(model, 'risk_model.pkl')
