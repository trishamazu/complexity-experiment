import pandas as pd
from scipy.stats import entropy

# Assume 'normalized_image_scores.csv' has been previously created and contains the normalized scores
# Load the normalized CSV file
normalized_df = pd.read_csv('normalized_image_scores.csv')

# Calculate the entropy for each row (image) and append as a new column
normalized_df['Entropy'] = normalized_df.iloc[:, 1:].apply(lambda x: entropy(x), axis=1)

# Create a new DataFrame with just the image name and the entropy
# Assuming the first column contains the image names
entropy_df = normalized_df[['image_name', 'Entropy']]  # Adjust 'image name' if the actual column name differs

# Save this new DataFrame to a CSV file
entropy_df.to_csv('image_entropy_scores.csv', index=False)
