import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset.csv')

df = df.drop_duplicates(subset=['user_id'])
df['language'] = df['language'].astype(str).str.strip().str.lower()
df['location'] = df['location'].astype(str).str.strip().str.title()
df['account_created'] = pd.to_datetime(df['account_created'], errors='coerce')
df = df.dropna()

df.to_csv('cleaned_dataset.csv', index=False)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Follower Count
sns.histplot(df['follower_count'], bins=30, ax=axes[0], color='blue')
axes[0].set_title('Distribution of Follower Counts')

# 2. Locations (Fixed Future Warning)
top_locations = df['location'].value_counts().head(10)
sns.barplot(x=top_locations.values, y=top_locations.index, ax=axes[1], hue=top_locations.index, palette='viridis', legend=False)
axes[1].set_title('Top 10 User Locations')

# 3. Languages (Fixed Future Warning)
top_languages = df['language'].value_counts().head(10)
sns.barplot(x=top_languages.values, y=top_languages.index, ax=axes[2], hue=top_languages.index, palette='magma', legend=False)
axes[2].set_title('Top 10 Languages')

plt.tight_layout()

# Save as an image instead of trying to show it in the terminal
plt.savefig('eda_charts.png', bbox_inches='tight')
print("Cleaning complete. Cleaned dataset and 'eda_charts.png' saved successfully.")