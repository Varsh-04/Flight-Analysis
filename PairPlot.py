import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\varsh\Downloads\New folder\Flight_details.2.xlsx")

df['Duration'] = df['Duration_hours'] * 60 + df['Duration_min']

numeric_features = ['Price', 'Duration', 'Total_Stops']
sns.pairplot(df[numeric_features], diag_kind='kde', markers='o')

plt.suptitle('Pair Plot of Flight Features', y=1.02)
plt.show()