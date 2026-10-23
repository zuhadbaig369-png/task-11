import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Penguins Data.csv")

columns = ["Culmen Length (mm)", "Culmen Depth (mm)",
           "Flipper Length (mm)", "Body Mass (g)"]

for column in columns:
    plt.hist(df[column].dropna(), bins=20, edgecolor="black")
    plt.title(column)
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()