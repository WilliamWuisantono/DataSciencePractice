# Cereal Data Analysis and Machine Learning Project
 
### Project Overview
This project utilizes the [Kaggle Cereal Dataset](https://www.kaggle.com/datasets/crawford/80-cereals) to explore the nutritional attributes of cereals in the United States. The goal is to preprocess and analyze the data, create multiple data visualizations, and apply machine learning techniques to classify cereals based on their rating.
 
---
 
### Team Members
- William
- Silas
- Jiwon
- Alonso
 
---
 ### Repository Structure
 
- **Data_Preprocessing.py**  
  This script handles the initial data cleaning and preprocessing. Major steps include:
  - Filling any missing values with the median for numerical columns.
  - Mapping manufacturer codes (`mfr`) to full company names for clarity.
  - Converting `mfr` and `type` columns to categorical types.
  - Creating a binary target variable `high_rating` based on whether a cereal’s rating is above 50.
 
- **MachineLearning.py**  
  This script trains a logistic regression model to classify cereals as "highly rated" or not. Steps include:
  - Feature scaling with `StandardScaler`.
  - Splitting data into training and testing sets.
  - Train a logistic regression model and make predictions.
  - Evaluating the model using accuracy score, confusion matrix, and cross-validation.
 
- **DataVisuals.py**  
  This script generates visual insights into the data:
  - Top 7 cereals by sugar content (bar plot).
  - Manufacturer distribution (pie chart).
  - Calories vs. rating by cereal type (scatter plot).
