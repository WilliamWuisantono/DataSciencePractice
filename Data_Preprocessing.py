import pandas as pd

def preprocess_data():
    df = pd.read_csv('cereal.csv')

    # Cleaning the Data if the dataset has any missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # 1. Data preprocessing for data analysis and visuals
    # Modify the manufacturer dataset for clarity
    manufacturer_mapping = {
            'A': 'American Home Food Products',
            'G': 'General Mills',
            'K': 'Kelloggs',
            'N': 'Nabisco',
            'P': 'Post',
            'Q': 'Quaker Oats',
            'R': 'Ralston Purina'
        }
    df['mfr'] = df['mfr'].map(manufacturer_mapping)

    # 2. Converting 'mfr' and 'type' from objects to category
    df['mfr'] = df['mfr'].astype('category')
    df['type'] = df['type'].astype('category')

    # 3. Create a binary target variable 'high_rating' based on the rating column
    df['high_rating'] = df['rating'].apply(lambda x: 1 if x > 50 else 0)

    return(df)