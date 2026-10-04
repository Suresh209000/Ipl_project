import matplotlib.pyplot as plt 
import seaborn as sns
df = sns.load_dataset('tips')
print(df)
plt.subplot(1,2,1)
sns.histplot(df['total_bill'],bins = 5,kde = True)
plt.subplot(1,2,2)
sns.histplot(df['tip'],bins = 5,kde = True)
plt.show()