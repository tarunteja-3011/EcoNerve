import pandas as pd

# Load the file
df = pd.read_csv("AshokVihar_Hourly.csv")

# 1. PRECISION TASK: Combine separate time columns into one DateTime column
# This function looks for the columns you found: 'year', 'month', 'day', 'hour'
df['Date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

# 2. Sort the data by time (Time-series continuity requirement)
df = df.sort_values('Date')

# 3. CLEANING TASK: Fill missing pollution values (like PM2.5 or PM10)
# This replaces empty cells with the value from the hour before
df_clean = df.ffill()

# 4. Save the new, precise file
df_clean.to_csv("Cleaned_AshokVihar.csv", index=False)

print("--- SUCCESS REPORT ---")
print(f"Columns combined into 'Date' successfully.")
print(f"Total rows processed: {len(df_clean)}")
print("File saved as: Cleaned_AshokVihar.csv")