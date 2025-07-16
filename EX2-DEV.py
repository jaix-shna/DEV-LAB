import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import string

# Load dataset (ensure correct path and encoding)
df = pd.read_csv(r"C:\Users\Jayaprakash\Downloads\archive\spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']  # Rename columns for clarity

# Dataset overview
print("First 5 rows:\n", df.head())
print("\nInfo:\n")
print(df.info())
print("\nDescribe:\n")
print(df.describe())
print("\nMissing values:\n", df.isnull().sum())
print("\nLabel distribution:\n", df['label'].value_counts())

# Plot spam vs ham count
sns.countplot(data=df, x='label')
plt.title('Spam vs Ham Message Count')
plt.xlabel('Label')
plt.ylabel('Count')
plt.show()

# Message length analysis
df['length'] = df['message'].apply(len)
print("\nLength stats:\n", df['length'].describe())

# Histogram of message lengths
plt.figure(figsize=(10,5))
df[df['label'] == 'ham']['length'].plot.hist(bins=20, label='Ham', alpha=0.7)
df[df['label'] == 'spam']['length'].plot.hist(bins=20, label='Spam', alpha=0.7, color='red')
plt.legend()
plt.title('Message Length Distribution')
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.show()

# Word clouds (remove punctuation and combine text)
spam_text = ' '.join(df[df['label'] == 'spam']['message']).translate(str.maketrans('', '', string.punctuation))
ham_text = ' '.join(df[df['label'] == 'ham']['message']).translate(str.maketrans('', '', string.punctuation))

# Spam Word Cloud
spam_wc = WordCloud(width=600, height=400, background_color='black').generate(spam_text)
plt.figure(figsize=(10,6))
plt.imshow(spam_wc, interpolation='bilinear')
plt.axis('off')
plt.title('Spam Word Cloud')
plt.show()

# Ham Word Cloud
ham_wc = WordCloud(width=600, height=400, background_color='white').generate(ham_text)
plt.figure(figsize=(10,6))
plt.imshow(ham_wc, interpolation='bilinear')
plt.axis('off')
plt.title('Ham Word Cloud')
plt.show()

# Boxplot of message length by label
plt.figure(figsize=(6,4))
sns.boxplot(x='label', y='length', data=df)
plt.title('Message Length by Label')
plt.show()

# Statistical insights
avg_ham = df[df['label'] == 'ham']['length'].mean()
avg_spam = df[df['label'] == 'spam']['length'].mean()
print(f"\n✅ Average Ham Message Length: {avg_ham:.2f} characters")
print(f"✅ Average Spam Message Length: {avg_spam:.2f} characters")
print("\nEDA Completed Successfully ✅")
