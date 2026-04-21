import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Create dataset
data = {
    'Age': [25, None, 28, 35],
    'Gender': ['Female', 'Male', 'Male', 'Female'],
    'Income': [50000, 60000, 45000, None]
}

df = pd.DataFrame(data)

# Handling missing values
imputer = SimpleImputer(strategy='mean')
df[['Age', 'Income']] = imputer.fit_transform(df[['Age', 'Income']])

print("Data after handling missing values:")
print(df)

# Encoding categorical data
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(df[['Gender']]).toarray()

encoded_df = pd.DataFrame(
    encoded_data,
    columns=encoder.get_feature_names_out(['Gender'])
)

print("\nData after categorical encoding:")
print(encoded_df)

# Feature Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['Age', 'Income']])

scaled_df = pd.DataFrame(scaled_data, columns=['Scaled Age', 'Scaled Income'])

print("\nData after feature scaling:")
print(scaled_df)
