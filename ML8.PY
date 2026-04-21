import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([
    [1000, 2],
    [1500, 3],
    [2000, 4]
])

y = np.array([300000, 400000, 500000])

# Model
model = LinearRegression()
model.fit(X, y)

# User input
size = float(input("Enter house size (sqft): "))
bedrooms = int(input("Enter number of bedrooms: "))

new_data = np.array([[size, bedrooms]])

predicted_price = model.predict(new_data)

print(f"Predicted price: Rs {predicted_price[0]:.2f}")