import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("cereal.csv")

# Sort the dataset by 'sugars' and select the top 10 cereals
top_sugar_cereals = df.sort_values('sugars', ascending=False).head(10)

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(top_sugar_cereals['name'], top_sugar_cereals['sugars'], color='orange')
plt.xlabel('Cereal Name')
plt.ylabel('Sugar Content')
plt.title('Top 10 Cereals by Sugar Content')
plt.xticks(rotation=45, ha='right')
plt.show()