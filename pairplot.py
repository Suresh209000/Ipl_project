import matplotlib.pyplot as plt 
import seaborn as sns
df = sns.load_dataset('tips')

print(df)
sns.pairplot(df,hue='size',palette='rainbow')
plt.show()