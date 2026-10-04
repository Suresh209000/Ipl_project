import matplotlib.pyplot as plt 
import seaborn as sns
df = sns.load_dataset('tips')
print(df)
sns.displot(df['total_bill'],bins = 5,kde = True)

plt.show()