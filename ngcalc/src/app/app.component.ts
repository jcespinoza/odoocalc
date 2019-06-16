import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

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
    console.log("Calling service again");
    this.http.post("http://localhost:8069/odoocalc/calculate",
          {
            input: "5+92+7"
          },
          {
            headers: new HttpHeaders({
              'Content-Type':  'application/json',
            }),
            responseType: 'json'
          }
        )
        .subscribe(result => {
          console.log("Here's the response: " + JSON.stringify(result));
        }, error => {
          console.log("Well, that didn't work");
        });
        console.log("Call was made. Wait a bit...");
  }
}
