# Step 2: Python Code to Load and Explore the Data

import pandas as pd

# Define the file paths
csv_file_path = "C:\\ML_Projects\\sample_data.csv"
excel_file_path = "C:\\ML_Projects\\sample_data.xlsx"

# Load the CSV file
data_csv = pd.read_csv(csv_file_path)
print("CSV File Data:")
print(data_csv)

# Load the Excel file
data_excel = pd.read_excel(excel_file_path)
print("\nExcel File Data:")
print(data_excel)

# Basic Data Exploration
print("\nData Descriptions:")

print("CSV Data Description:")
print(data_csv.describe())

print("\nExcel Data Description:")
print(data_excel.describe())

# Displaying data types
print("\nData Types in CSV File:")
print(data_csv.dtypes)

print("\nData Types in Excel File:")
print(data_excel.dtypes)



CSV 
Name,Age,Score
Srikanth,28,85
Snigdha,22,78
Mary,31,92


excel

| Name    | Course | Sem |
| ------- | ------ | --- |
| Rajesh  | BCA    | 1   |
| Ramesh  | BCA    | 2   |
| Swati   | BCOM   | 1   |
| Florina | BCOM   | 3   |
| Pooja   | BBA    | 2   |
| Raghu   | BBA    | 4   |

