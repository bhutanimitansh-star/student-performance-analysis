import pandas as pd

df = pd.read_csv("data/students.csv")

# basic inspection
print("Shape (rows, columns):", df.shape) # prints the number of rows and columns
print("\nData Info:") 
print(df.info())

print("\nStatistical Summary:") # prints summary statistics for numerical columns
print(df.describe())

# Average scores
print("\nAverage Scores:") 
print("Math:", df["math score"].mean())
print("Reading:", df["reading score"].mean())
print("Writing:", df["writing score"].mean())


# Average scores by gender
print("\nAverage scores by gender:")
gender_avg = df.groupby("gender").mean()
print(gender_avg)


import matplotlib.pyplot as plt

gender_avg.plot(kind="bar")
plt.title("Average Scores by Gender") # sets the title of the plot
plt.ylabel("Score") # labels the y-axis
plt.xlabel("Gender") # labels the x-axis
plt.savefig("gender_scores.png") # saves the plot as an image file
plt.show()


print("\nConclusion:") # concludes the analysis
print("Female students have higher average scores in math, reading, and writing compared to male students in this dataset.") # summarizes the findings
