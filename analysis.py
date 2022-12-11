import pandas as pd
from sklearn import model_selection


#Splitting two of the four csv files, by the ";", for readability and extracting them into data0 and data1
data0 = pd.read_table("matchs-schudule.csv", delimiter = ";")

data1 = pd.read_table("Qatar2022-teams.csv", delimiter = ";")

#Splitting the rest of the csv files, instead by the ",", for readability and extracting them into data2 and data3
data2 = pd.read_table("fifa_ranking-2022-10-06.csv", delimiter = ",")

data3 = pd.read_table("historical_win-loose-draw_ratios_qatar2022_teams.csv", delimiter = ",")

zero_and_one = data0.merge(data1.rename(columns={'Team':'country1'}),how='outer')


two_and_three = data2.merge(data3.rename(columns={'country1':'country_full'}),how='inner')

everything = zero_and_one.merge(two_and_three.rename(columns = {'country_full': 'country1'}), how = 'inner')


everything.columns



# Import the necessary libraries

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


df = everything
# Clean and process the data
df = df.dropna()
df["date"] = pd.to_datetime(df["date"])
df["country1"] = df["country1"].astype("category").cat.codes
df["country2"] = df["country2"].astype("category").cat.codes
df["Group"] = df["Group"].astype("category").cat.codes
df["date"] = pd.to_numeric(df["date"])
# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[[ "date","country1", "country2", "Group","games"]], df["rank"], test_size=0.2)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)


