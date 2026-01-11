import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Plot style
sns.set(style="whitegrid")
# Load dataset (CSV file should be in same folder)
df = pd.read_csv("titanic.csv")

# Display first 5 rows
df.head()
# Dataset shape
print("Rows & Columns:", df.shape)

# Dataset info
df.info()

# Statistical summary
df.describe()
# Missing values count
df.isnull().sum()
# Fill missing Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing Embarked with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop Cabin column (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

# Recheck missing values
df.isnull().sum()
# Count duplicates
print("Duplicate rows:", df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)
# Convert categorical columns to category type
categorical_cols = ['Sex', 'Embarked', 'Pclass', 'Survived']
for col in categorical_cols:
    df[col] = df[col].astype('category')
plt.figure()
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()
plt.figure()
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()
plt.figure()
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()
plt.figure()
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.show()
# Convert categorical to numeric for correlation
df_corr = df.copy()
df_corr['Sex'] = df_corr['Sex'].map({'male': 0, 'female': 1})
df_corr['Embarked'] = df_corr['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

plt.figure(figsize=(10,6))
sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
print("Key Insights:")
print("- Females had a higher survival rate than males.")
print("- Passengers in 1st class survived more compared to 2nd and 3rd class.")
print("- Younger passengers had slightly higher survival chances.")
print("""
Conclusion:
The EDA helped identify important patterns and trends in the dataset.
Data cleaning, visualization, and statistical analysis provided valuable
insights into survival factors such as gender, class, and age.
""")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Plot style
sns.set(style="whitegrid")
# Load dataset (CSV file should be in same folder)
df = pd.read_csv("titanic.csv")

# Display first 5 rows
df.head()
# Dataset shape
print("Rows & Columns:", df.shape)

# Dataset info
df.info()

# Statistical summary
df.describe()
# Missing values count
df.isnull().sum()
# Fill missing Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing Embarked with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop Cabin column (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

# Recheck missing values
df.isnull().sum()
# Count duplicates
print("Duplicate rows:", df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)
# Convert categorical columns to category type
categorical_cols = ['Sex', 'Embarked', 'Pclass', 'Survived']
for col in categorical_cols:
    df[col] = df[col].astype('category')
plt.figure()
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()
plt.figure()
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()
plt.figure()
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()
plt.figure()
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.show()
# Convert categorical to numeric for correlation
df_corr = df.copy()
df_corr['Sex'] = df_corr['Sex'].map({'male': 0, 'female': 1})
df_corr['Embarked'] = df_corr['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

plt.figure(figsize=(10,6))
sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
print("Key Insights:")
print("- Females had a higher survival rate than males.")
print("- Passengers in 1st class survived more compared to 2nd and 3rd class.")
print("- Younger passengers had slightly higher survival chances.")
print("""
Conclusion:
The EDA helped identify important patterns and trends in the dataset.
Data cleaning, visualization, and statistical analysis provided valuable
insights into survival factors such as gender, class, and age.
""")
plt.show()

# ==============================
# FINAL INSIGHTS
# ==============================

print("\n========== KEY INSIGHTS ==========\n")
print("1. Female passengers had a significantly higher survival rate.")
print("2. Passengers in higher classes showed better survival chances.")
print("3. Fare amount positively influenced survival.")
print("4. Younger passengers had slightly higher survival probability.")
print("5. Overall survival rate was approximately 38%.")
