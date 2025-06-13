import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Titanic-Dataset.csv")

# ---- Data Preprocessing ----
#  Age Groups
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 30, 50, 80],
                        labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])

# ---- Basic Survival Stats ----
total = len(df)
survived = df['Survived'].sum()
not_survived = total - survived
survival_rate = round((survived / total) * 100, 2)

# ---- Grouped Survival Analysis ----
survival_by_sex = df.groupby('Sex')['Survived'].mean() * 100
survival_by_class = df.groupby('Pclass')['Survived'].mean() * 100
survival_by_embarked = df.groupby('Embarked')['Survived'].mean() * 100
survival_by_age_group = df.groupby('AgeGroup')['Survived'].mean() * 100

# ---- Plotting ----

plt.figure(figsize=(14, 10))

# 1. Survival by Sex
plt.subplot(2, 2, 1)
survival_by_sex.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Survival Rate by Sex')
plt.ylabel('Survival Rate (%)')
plt.xticks(rotation=0)

# 2. Survival by Class
plt.subplot(2, 2, 2)
survival_by_class.plot(kind='bar', color='lightgreen')
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate (%)')
plt.xticks(rotation=0)

# 3. Survival by Embarked Port
plt.subplot(2, 2, 3)
survival_by_embarked.plot(kind='bar', color='orange')
plt.title('Survival Rate by Port of Embarkation')
plt.ylabel('Survival Rate (%)')
plt.xticks(rotation=0)

# 4. Survival by Age Group
plt.subplot(2, 2, 4)
survival_by_age_group.plot(kind='bar', color='violet')
plt.title('Survival Rate by Age Group')
plt.ylabel('Survival Rate (%)')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
