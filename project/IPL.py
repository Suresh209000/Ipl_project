import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns

import pandas as pd

df = pd.read_csv(r"D:\Python Libraries\Seaborn\project\IPL.csv")

print(df.head())
df.info()

# 1. Which team wins the most matches

match_wins = df['match_winner'].value_counts()
sns.barplot(y = match_wins.index, x = match_wins.values,palette='viridis')
plt.title('Most match win by team')
plt.show()

#2. Toss Decision Trends

sns.countplot(x = df['toss_decision'],palette='rainbow')
plt.title('Toss decision Trends')
plt.show()

#3. Toss Vs Match winners

count = df[df['toss_winner']==df['match_winner']]['match_id'].count()
percentage = (count*100)/df.shape[0]
print(percentage.round(2))

# 4. How do teams win?(Runs vs Wickets)

sns.countplot(x = df['won_by'])
plt.show()

# Key player Performances

# 1. Most "Player od the match" awards

count = df['player_of_the_match'].value_counts().head(10)
sns.barplot(x = count.values,y = count.index,palette = 'rainbow')
plt.title('Most player of the match')
plt.xlabel('Match count')
plt.ylabel('Players Name')
plt.show()

# 2. Top 2 scorrer

high = df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False).head(2)
high.plot(kind = 'barh')
plt.title("Top 2 scorers")
plt.xlabel('Scores')
plt.ylabel('Players')
plt.show()     

#3. 10 best bowling figures
df['highest_wickets'] = df['best_bowling_figure'].apply(lambda x:x.split('--')[0])
df['highest_wickets'] = df['highest_wickets'].astype(int)
top_bowlers = df.groupby('best_bowling')['highest_wickets'].sum().sort_values(ascending=False).head(10)
print(top_bowlers)
# top_bowlers.plot(kind = 'barh')
sns.barplot(x = top_bowlers.values,y =top_bowlers.index,palette='rainbow')
plt.xlabel('Number of wickets')
plt.ylabel('Players name')
plt.title('Top 10 highest wicket takers')

plt.show()

#4. Most matches played by venue

venue_count = df['venue'].value_counts()
sns.barplot(x = venue_count.values,y = venue_count.index,palette='rainbow')
plt.show()