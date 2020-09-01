import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent implements OnInit {

  data = ["Name", "Avg_Points", "Avg_FreeThrows", "Avg_Goals", "Winning_probability"];

  constructor() { }

  ngOnInit(): void {
  }

}
