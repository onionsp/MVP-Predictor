import pandas as pd
from sklearn.linear_model import Ridge
data = pd.read_csv('/Users/jsc/Downloads/player_mvp_stats.csv')

# Data cleaning
del data["Unnamed: 0"]
pd.isnull(data).sum()
data = data.fillna(0)
data.columns

features = [ 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P',
       '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',
       'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Year',
       'W', 'L', 'W/L%', 'GB', 'PS/G',
       'PA/G', 'SRS']

train = data[data["Year"] < 2021]
test = data[data["Year"] == 2021]

# Creating basic Ridge regression model
reg = Ridge(alpha=0.1)
reg.fit(train[features], train["Share"])
predictions = reg.predict(test[features])
