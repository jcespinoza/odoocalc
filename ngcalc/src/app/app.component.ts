import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{

  title = 'ngcalc';

  constructor(private http: HttpClient){

  }

  ngOnInit(): void {
    this.http.get("http://localhost:8069/odoocalc/calculate?texty=54", )
        .subscribe(result => {
          console.log("Here's the response: " + JSON.stringify(result));
        }, error => {
          console.log("Well, that didn't work");
        })
  }
}
