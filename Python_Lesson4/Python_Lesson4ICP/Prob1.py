import pandas as pd

df = pd.read_csv('Python_Lesson4/Python_Lesson4/train.csv')

print(df[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)) 

# there is a high correlation between female and whether they survived or not so yes, I think this dataclea should be used.

