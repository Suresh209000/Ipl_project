import matplotlib.pyplot as plt 
import seaborn as sns
df = sns.load_dataset('tips')

print(df)
sns.rugplot(df['total_bill'])
plt.show()