# World Cup Data Mining Project - BZAN 542
This repo is our world cup data mining project by using R for text classification, a common natural language processing (NLP) problem. The project was built for a group project in BZAN 542 - Data Mining Methods for Business Applications at the University of Tennessee in Spring 2022. It is being posted here as a reference and hopefully a springboard for future extensions and refinements.

# Overview
The main data set we used is from the FIFA database. It contains every match between international teams from 1992 to March of 2022. There are 433 games recorded in this dataset and 36 different variables recorded. We also incorporated 4 other datasets for some of our modeling techniques that included the schedules and the groups of each World Cup since 1992, team ranks, and player ratings.
The objective of our predictive model is to predict the outcome of the group stages of the world cup. While the data was mostly ready, it still required some cleaning for use in our model. This included changing data types to meet the information in the tables. We also created features:
•	Is the game a World Cup game? (Yes/No)
•	One feature used for predictions was the win or loss of any world cup game. We predicted on the average rank of the game played which was the 2022 FIFA world cup rankings of both teams divided by 2. 
•	A rank difference variable that was the difference between the home teams rank and the away teams’ rank. 
•	The difference in rating of the top three players of the home team minus the top-three players of the away team for offense, defense, midfield, and the highest rated goalkeeper that each team had.
We trained different types of models including 
•	Logistic regression initially that predicted 67% accuracy on the training and holdout data. This was the highest performing model. 
•	We used a decision tree also which predicted to 66% accuracy. This model was slightly less accurate. 
•	A random forest and a gradient boosted model. The accuracy of these models was significantly lower. 
•	Naïve Bayes. This model had very low accuracy.
Since the accuracy of the logistic regression was the highest, we decided to use this as the predictive model for the outcome of the World Cup matches. We combined four different data sets that included all international matches since 1992 as well as the schedule and the groups of the World Cup.  The other data sets included the ranks of the World Cup for the ratings of the corresponding positions. We averaged the ratings from the last five years. The reason that we did this is because players from five years ago are most likely not on the team anymore. We wanted to have an accurate representation of the current team since the games dated back to 1992. The predictors used in this model were:
•	Average rank of each team
•	Average player-score of the top 3 offenders on each team
•	Average player-score of the top 3 defenders on each team
•	Average player-score of the top 3 midfielders on each team
•	Average player-score of the top rated goalkeeper on each team
The outcomes of the group stages that the logistic regression model is show in a table below. A W or L in the Win_or_loss column indicates a win or a loss for the home team in that matchup. These predictions showed a 67% accuracy on the holdout data, which gives us confidence that the model can predict real world outcomes reasonably well for international matches.



![image](https://user-images.githubusercontent.com/112140301/208023913-d99b9ef8-bf1a-4eb3-921c-4478fc0c7747.png)

