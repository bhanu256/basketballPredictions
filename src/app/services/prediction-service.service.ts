import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PredictionServiceService {

  constructor(
    private http: HttpClient
  ) { }

  predict(teamName: string, oppTeamName: string){
    return this.http.get("http://127.0.0.1:5000/predict/"+teamName+"/"+oppTeamName)
  }

  teams(){
    return this.http.get("http://127.0.0.1:5000/teams")
  }
}
