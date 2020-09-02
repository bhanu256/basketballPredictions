from flask import Flask, jsonify
from regression import Regression
app = Flask(__name__)
obj = Regression()

@app.route('/')
def hello():
    return "Hello"

@app.route('/predict/<homeTeam>/<awayTeam>')
def predict(homeTeam, awayTeam):
    probabilities = obj.predict(homeTeam, awayTeam)
    return jsonify(probabilities)

@app.route('/teams')
def teamNames():
    namesList = obj.uniqueTeams()
    return jsonify(namesList)

if __name__ == "main":
    app.run()
