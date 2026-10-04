import matplotlib.pyplot as plt
import seaborn as sns
flights = sns.load_dataset('flights')
# print(flights)
tips = sns.load_dataset('tips')
# print(tips)
tipscoo = tips[['total_bill','tip','size']]
# print(tipscoo)
print(tipscoo.corr())
sns.clustermap(tipscoo.corr()                     )
plt.show()