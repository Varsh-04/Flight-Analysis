import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\varsh\Downloads\New folder\Flight_details.2.xlsx")

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Total_Stops', y='Price', alpha=0.6, hue='indiGo', palette='viridis', size='Price', sizes=(20, 200))

plt.title('Flight Prices vs. Total Stops')
plt.xlabel('Total Stops')
plt.ylabel('Flight Price')
plt.xticks(rotation=0)  # Rotate x-axis labels if needed
plt.legend(title='Airline', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()