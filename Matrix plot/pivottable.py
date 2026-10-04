import matplotlib.pyplot as plt
import seaborn as sns
flights = sns.load_dataset('flights')
pvtflights = flights.pivot_table(values = 'passengers',index = 'month', columns='year')
print(pvtflights)
sns.heatmap(pvtflights)
plt.show() 