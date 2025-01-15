# This code is used to convert .data file to .csv files
import pandas as pd

# File paths
input_file = '/Users/z5601757/Documents/AriaResearch/Project/Dataset/heartDisease/reprocessed.hungarian.data'  # Replace with the path to your .data file
output_file = '/Users/z5601757/Documents/AriaResearch/Project/Dataset/new.csv'  # Replace with your desired .csv file path

# Step 1: Load the .data file
# Assuming the .data file is comma-separated
df = pd.read_csv(input_file, header=None)   # Use `header=None` if there's no header row

# Step 2: Add column names (optional)
# Replace ['col1', 'col2', ...] with appropriate column names
# df.columns = ['col1', 'col2', 'col3', 'col4']

# Step 3: Save as .csv
df.to_csv(output_file, index=False)
print(f"File converted and saved to {output_file}")
print(df.head(10))
