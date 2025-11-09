# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# -------------------------------
# Task 1: NumPy array and mean
# -------------------------------
numbers = np.arange(1, 11)  # Create array from 1 to 10
mean_value = np.mean(numbers)
print("NumPy Array:", numbers)
print("Mean value:", mean_value)

# -------------------------------
# Task 2: Load a small dataset with pandas
# -------------------------------
# Create a small dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 22],
    'Salary': [50000, 60000, 70000, 80000, 45000]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("\nDataFrame:\n", df)

# Display summary statistics
print("\nSummary Statistics:\n", df.describe())

# -------------------------------
# Task 3: Fetch data from a public API
# -------------------------------
# Example API: JSON placeholder
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if response.status_code == 200:
    data = response.json()
    print("\nFetched API Data:", data)
    print("Title from API:", data['title'])
else:
    print("Failed to fetch data")

# -------------------------------
# Task 4: Simple line graph with matplotlib
# -------------------------------
# Example data
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

plt.plot(y)  # Plot y values against index
plt.title("Simple Line Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()
