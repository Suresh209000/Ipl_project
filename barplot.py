import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
df = sns.load_dataset('tips')
print(df)
sns.barplot(x = df['sex'],y = df['tip'],estimator=np.sum)
plt.show()