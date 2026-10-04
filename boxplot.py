import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
df = sns.load_dataset('tips')
print(df)
sns.boxplot(x = df['tip'],y = df['day'],palette='rainbow')
plt.show()