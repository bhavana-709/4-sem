import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("study_data.csv")

# -------- Scatter Plot --------
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.scatter(data['Study Hours'], data['Exam Score'])
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.grid(True)

# -------- Bar Chart --------
bins = [0, 2, 4, 6, 8, 10, 12]
labels = ['0-2', '2-4', '4-6', '6-8', '8-10', '10-12']

data['Study Hour Range'] = pd.cut(data['Study Hours'], bins=bins, labels=labels)

grouped_data = data.groupby('Study Hour Range')['Exam Score'].mean()

plt.subplot(1, 2, 2)
grouped_data.plot(kind='bar')
plt.title("Average Exam Score by Study Hour Range")
plt.xlabel("Study Hour Range")
plt.ylabel("Average Score")

plt.tight_layout()
plt.show()




CSV

Student_ID,Study Hours,Exam Score
1,5,82
2,3,60
3,2,48
4,1,35
5,4,70
6,6,66
7,9,95
8,7,88
9,8,78
10,6.5,90
11,4.5,76
12,10,98
13,12,99