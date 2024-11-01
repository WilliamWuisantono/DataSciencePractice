import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import Data_Preprocessing

# Load the dataset
df = Data_Preprocessing.preprocess_data()

# Select the top 7 cereals by sugar content
top_sugar_cereals = df.nlargest(7, 'sugars')

# Set the style for the plot using seaborn
sns.set_style('whitegrid')

# Create a horizontal bar plot
plt.figure(figsize=(15, 6))
sns.barplot(x='sugars', y='name', data=top_sugar_cereals, palette='Oranges_r')

# Set plot labels and title
plt.xlabel('Sugar Content')
plt.ylabel('Cereal Name')
plt.title('Top 7 Cereals by Sugar Content')

# Show the plot
plt.show()

# Frequency of Manufacturer in Dataset
plt.figure(figsize=(10, 6))
df['mfr'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Manufacturer Distribution')
plt.ylabel('')
plt.show()

# Calories vs Rating Scatter Plot
plt.figure(figsize=(8, 6)) 
sns.scatterplot(data=df, x='calories', y='rating', hue='type', palette='viridis', s=100) 
plt.title("Calories vs. Rating of Cereals")
plt.xlabel("Calories") 
plt.ylabel("Rating") 
plt.legend(title="Type") 
plt.show()
