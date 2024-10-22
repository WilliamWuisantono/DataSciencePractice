import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("cereal.csv")

# Select the top 10 cereals by sugar content
top_sugar_cereals = df.nlargest(10, 'sugars')

# Set the style for the plot using seaborn
sns.set_style('whitegrid')

# Create a horizontal bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='sugars', y='name', data=top_sugar_cereals, palette='Oranges_r')

# Set plot labels and title
plt.xlabel('Sugar Content')
plt.ylabel('Cereal Name')
plt.title('Top 10 Cereals by Sugar Content')

# Show the plot
plt.show()