import matplotlib.pyplot as plt 
import seaborn as sns
df = sns.load_dataset('tips')
print(df)
sns.countplot(x = df['sex'],hue = df['smoker'])
plt.show()