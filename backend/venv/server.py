from flask import Flask, jsonify
from regression import Regression
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources = {
    r"/*": {
        "origins": "*"
    }
})
obj = Regression()

@app.route('/')
def hello():
    return "Hello"

@app.route('/predict/<homeTeam>/<awayTeam>')
def predict(homeTeam, awayTeam):
    probabilities = obj.predict(homeTeam, awayTeam)
    teamDetails = obj.teamData(homeTeam, awayTeam)
    oppTeamDetails = obj.oppTeamData(homeTeam, awayTeam)
    return jsonify({
            'probabilities': probabilities,
            'teamDetails': teamDetails,
            'oppTeamDetails': oppTeamDetails
        })

@app.route('/teams')
def teamNames():
    namesList = obj.uniqueTeams()
    return jsonify(namesList)

if __name__ == "main":
    app.run()
