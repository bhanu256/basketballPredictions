from os import path
from numpy import save
from numpy import load

from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model import LogisticRegression 

import numpy as np
import pandas as pd 

class Regression:

    def __init__(self):
        self.data = self.prepareData()

    #Endpoint functions
    def predict(self, homeTeam, awayTeam):
        try:
            x_axis, y_axis = self.gatherData(homeTeam, awayTeam)
            x_train, x_test, y_train, y_test = train_test_split(x_axis, y_axis, test_size = 0.3, random_state = 0)
            x_train, x_test = self.scaling(x_train, x_test)
            prob = self.model(x_train, y_train, x_test)

            return prob.tolist()
        except Exception as exp:
            return exp

    def uniqueTeams(self):
        return self.data.Team.unique().tolist()

    def teamData(self, teamName, oppName):
        details = self.calculation('', teamName, oppName)
        return details
        
    def oppTeamData(self, teamName, oppName):
        details = self.calculation("Opp.", teamName, oppName)
        return details

    #Support functions
    def fileExists(self, name):
        if path.exists(name):
            return True
        else:
            return False

    def prepareData(self):
        data = pd.read_csv("nbaStats.csv")

        wins = []
        for i in data['WINorLOSS']:
            if i == "W":
                wins.append(1)
            else:
                wins.append(0)

        data['wins'] = wins

        return data
        
    def gatherData(self, homeTeam, awayTeam):
        data = self.data[(self.data['Team'] == homeTeam) & (self.data['Opponent'] == awayTeam)]

        features_to_drop = ['Unnamed: 0','Team', 'Home', 'Game' , 'Date', 'Opponent', 'WINorLOSS', 'OpponentPoints',
                        'Opp.FieldGoals', 'Opp.3PointShotsAttempted', 'Opp.3PointShots', 'Opp.FreeThrows', 
                        'Opp.FreeThrowsAttempted', 'Opp.FreeThrows.', 'Opp.OffRebounds', 'Opp.TotalRebounds', 
                        'Opp.Assists', 'Opp.Steals', 'Opp.Blocks', 'Opp.Turnovers', 'Opp.TotalFouls',
                        'Opp.FieldGoalsAttempted', 'Opp.FieldGoals.', 'Opp.3PointShots.', 'wins']

        y_axis = data['wins']
        x_axis = data.drop(features_to_drop, axis=1)
        x_axis = SimpleImputer().fit_transform(x_axis)

        return x_axis, y_axis

    def scaling(self, x_train, x_test):
        sc_x = StandardScaler() 
        x_train = sc_x.fit_transform(x_train)  
        x_test = sc_x.transform(x_test) 

        return x_train, x_test

    def model(self, x_train, y_train, x_test):
        classifier = LogisticRegression(random_state = 0) 
        classifier.fit(x_train, y_train) 
        y_pred = classifier.predict_proba(x_test)

        return y_pred[0]

    def calculation(self, adds, homeTeam, awayTeam):
        attributes = ['FieldGoals', 'FreeThrows', 'OffRebounds',
         'TotalRebounds', 'Assists', 'Blocks', 'Turnovers']

        details = {}
        data = self.data[(self.data['Team'] == homeTeam) & (self.data['Opponent'] == awayTeam)]

        for attr in attributes:
            details[attr] = round(data[adds + attr].mean(), 2)

        return details

# obj = Regression()
# print(obj.predict("ATL", "TOR"))