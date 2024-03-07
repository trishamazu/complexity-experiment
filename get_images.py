import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('/home/wallacelab/complexity-experiment/hebart49_scaled_embedding_data.csv')  # Update this path to your CSV file location

# Normalize the scores so each row (for each image) sums to 1 (excluding the image name column)
df.iloc[:, 1:] = df.iloc[:, 1:].div(df.iloc[:, 1:].sum(axis=1), axis=0)

# Save the normalized DataFrame to a new CSV file
df.to_csv('normalized_image_scores.csv', index=False)

# This creates a new CSV file named 'normalized_image_scores.csv' in the current directory
