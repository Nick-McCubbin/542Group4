import pandas as pd


#Splitting two of the four csv files, by the ";", for readability and extracting them into data0 and data1
data0 = pd.read_table("matchs-schudule.csv", delimiter = ";")

data1 = pd.read_table("Qatar2022-teams.csv", delimiter = ";")

#Splitting the rest of the csv files, instead by the ",", for readability and extracting them into data2 and data3
data2 = pd.read_table("fifa_ranking-2022-10-06.csv", delimiter = ",")

data3 = pd.read_table("historical_win-loose-draw_ratios_qatar2022_teams.csv", delimiter = ",")

zero_and_one = data0.merge(data1.rename(columns={'Team':'country1'}),how='outer')

two_and_three = data2.merge(data3.rename(columns={'country1':'country_full'}),how='inner')

everything = zero_and_one.merge(two_and_three.rename(columns = {'country_full': 'country1'}), how = 'inner')