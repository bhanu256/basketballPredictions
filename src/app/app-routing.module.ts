import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { PredictComponent } from './predict/predict.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {path: "home", component: HomeComponent, data: {animation: "Home"}},
  {path: "predict", component: PredictComponent, data: {animation: "Predict"}}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
