
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\varsh\Downloads\New folder\Flight_details.2.xlsx")

average_prices = df.groupby(['indiGo', 'Month'])['Price'].mean().unstack()

plt.figure(figsize=(12, 8))
sns.heatmap(average_prices, annot=True, fmt=".2f", cmap='YlGnBu', linewidths=.5)
plt.title('Average Flight Prices by Month and Airline')
plt.xlabel('Month')
plt.ylabel('indiGo')
plt.show()