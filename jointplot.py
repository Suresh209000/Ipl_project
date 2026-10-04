import matplotlib.pyplot as plt 
import seaborn as sns
df = sns.load_dataset('tips')

print(df)
sns.jointplot(x = 'total_bill',y = 'tip',data = df,kind = 'scatter')
plt.show()