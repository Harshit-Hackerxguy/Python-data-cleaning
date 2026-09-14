import pandas as pd

df = pd.read_csv('dataset.csv')

df = df.drop_duplicates(subset=['user_id'])
df['language'] = df['language'].astype(str).str.strip().str.lower()
df['location'] = df['location'].astype(str).str.strip().str.title()
df['account_created'] = pd.to_datetime(df['account_created'], errors='coerce')
df = df.dropna()

df.to_csv('cleaned_dataset.csv', index=False)
