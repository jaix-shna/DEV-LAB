# Part 1: NumPy Arrays
import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Array operations
print("Original Array:", arr1)
print("Array + 5:", arr1 + 5)
print("Sliced Array:", arr1[1:4])
print("Reshaped 2D Array:\n", arr2.reshape(3, 2))

# Part 2: Pandas DataFrame
import pandas as pd

# Creating DataFrame
data = {
    'Name': ['JEYAPRASATH', 'SURYA', 'AFZAL'],
    'Age': [19, 19,19 ],
    'Score': [90, 88, 88]
}
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nDataFrame Info:")
print(df.info())

print("\nStatistics:")
print(df.describe())

# Part 3: Matplotlib Plots
import matplotlib.pyplot as plt

# Line Plot
plt.figure()
plt.plot(df['Name'], df['Score'], marker='o', color='green')
plt.title('Scores of Students')
plt.xlabel('Name')
plt.ylabel('Score')
plt.grid(True)
plt.show()

# Bar Plot
plt.figure()
plt.bar(df['Name'], df['Age'], color='orange')
plt.title('Age of Students')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()

# Pie Chart
plt.figure()
plt.pie(df['Score'], labels=df['Name'], autopct='%1.1f%%', startangle=90)
plt.title('Score Distribution')
plt.show()
