import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
df = sns.load_dataset('tips')
print(df)
sns.swarmplot(x = df['day'],y = df['total_bill'],data = df)
plt.show()