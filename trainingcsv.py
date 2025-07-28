import pandas as pd

# Load fake and real datasets
df_fake = pd.read_csv("C:\\Users\\anand\\OneDrive\\Desktop\\Datasets\\FakeNews\\Fake.csv",encoding='ISO-8859-1')
df_real = pd.read_csv("C:\\Users\\anand\\OneDrive\\Desktop\\Datasets\\FakeNews\\True.csv",encoding='ISO-8859-1')

# Add label column
df_fake['label'] = 'FAKE'
df_real['label'] = 'REAL'

# Combine and shuffle
df = pd.concat([df_fake[['text', 'label']], df_real[['text', 'label']]], ignore_index=True)
df = df.sample(frac=1).reset_index(drop=True)

# Save merged file
df.to_csv("fake_and_real_news.csv", index=False)