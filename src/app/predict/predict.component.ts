import { Component, OnInit } from '@angular/core';
import { PredictionServiceService } from '../services/prediction-service.service';

import { Model } from './model';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent implements OnInit {

  teamData = {};
  oppTeamData = {};
  allTeamNames = [];

  statement: string;
  success = false;

  constructor(
    private service: PredictionServiceService
  ) { }

  ngOnInit(): void {
    this.service.teams().subscribe(
      (names) => {
        this.allTeamNames = Object.values(names)
      }
    )
  }

  getPredictionResults(teamName: string,oppTeamName: string){
    this.service.predict(teamName, oppTeamName).subscribe(
      (data) => {
        this.teamData = data['teamDetails']
        this.oppTeamData = data['oppTeamDetails']
        console.log(typeof(this.teamData), this.oppTeamData)
        this.prepareStatement(data['probabilities'], teamName, oppTeamName)
        this.success = true;
      },
      (error) => {
        this.statement = "No result found. Try with another teams!!"
        this.success = false;
      }
    );
  }

  prepareStatement(probabilities, teamName, oppTeamName){
    if(Number(probabilities[0]).toFixed(2) > Number(probabilities[1]).toFixed(2)){
      this.statement = "Team "+ teamName + " has about " + (Number(probabilities[0]) * 100).toFixed(2)+ " chance of winning";
    }
    else{
      this.statement = "Team "+ oppTeamName + " has about " + (Number(probabilities[1])*100).toFixed(2) + " chance of winning";
    }
  }

}
