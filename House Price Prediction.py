from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[500], [1000], [1500], [2000], [2500]])

y = np.array([20, 40, 60, 80, 100])

model = LinearRegression()
model.fit(x, y)


pred = model.predict([[1800]])

print("Predicted House Price:", pred[0], "Lakhs")