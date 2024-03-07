import pandas as pd
import numpy as np

# Load the CSV containing image names and entropy scores
df = pd.read_csv('image_entropy_scores.csv')

# Sort the DataFrame by entropy scores
df_sorted = df.sort_values(by='Entropy')

# Divide the DataFrame into 5 equal parts (quintiles) and label each quintile
quintiles = np.array_split(df_sorted, 5)
for i, quintile in enumerate(quintiles):
    quintile['Quintile'] = f'Quintile {i+1}'

# Select 10 random images from each quintile and keep the quintile label
selected_images_with_labels = pd.concat([q.sample(n=10) for q in quintiles])

# Now you have 50 images selected, 10 from each quintile of entropy scores, with labels
# You might want to save this selection to a new CSV
selected_images_with_labels.to_csv('selected_images_with_labels.csv', index=False)
