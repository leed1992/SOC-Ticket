import pandas as pd
import re

# Load files
book_df = pd.read_excel("book4.xlsx")
client_df = pd.read_csv("Client apps_2025-09-01T11_11_16.371Z.csv")

# Normalize function: lowercase, remove digits, punctuation, and extra spaces
def normalize(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # remove everything except letters and spaces
    return text.strip()

# Apply normalization
book_df['Normalized_App'] = book_df['Practice Approved App'].apply(normalize)
client_df['Normalized_Name'] = client_df['Name'].apply(normalize)

# Match logic
matches = []
for approved_app in book_df['Normalized_App']:
    matched_rows = client_df[client_df['Normalized_Name'].str.contains(approved_app)]
    for _, row in matched_rows.iterrows():
        matches.append({
            'Approved App': approved_app,
            'Matched Name': row['Name']
        })

# Convert to DataFrame and display
matched_df = pd.DataFrame(matches)
print(matched_df)