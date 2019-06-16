import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import * as calc from './constants';
import { tap, map, catchError } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  
  shouldShowTextInput: boolean = true;
  shouldShowTouchInput: boolean = true;
  inputText: string = "";
  resultText: string;
  outputError: boolean = false;

  constructor(private http: HttpClient){

  }

  ngOnInit(): void {
    this.toggleInputMode();
  }

  toggleInputMode(){
    this.shouldShowTextInput = !this.shouldShowTextInput;
    this.shouldShowTouchInput = !this.shouldShowTextInput;
  }

  calcButtonClicked(event: MouseEvent){
    var buttonText = (event.srcElement as HTMLButtonElement).innerText;
    switch (buttonText) {
      case calc.CLEAR:
        this.handleClear();
        break;
      case calc.DELETE:
        this.handleDelete();
        break;
      case calc.PLUS: case calc.MINUS:
      case calc.DIVIDE: case calc.TIMES:
        this.handleOperation(buttonText);
        break;
      case "7": case "8": case "9":
      case "4": case "5": case "6":
      case "1": case "2": case "3":
                case "0":
        this.handleNumber(+buttonText);
        break;
      case calc.EQUALS:
        this.getResult();
        break;
      default:
        break;
    }
  }

  getResult() {
    this.performApiCall();
  }

  handleOperation(operation: string) {
    this.inputText += (event.srcElement as HTMLButtonElement).innerText;
  }

  handleNumber(number: number){
    this.inputText += (event.srcElement as HTMLButtonElement).innerText;
  }

  handleDelete(){
    this.inputText = this.inputText.length > 0
                     ? this.inputText.substr(0, this.inputText.length - 1)
                     : this.inputText;
  }

  handleClear(){
    this.inputText = ""
  }

  private performApiCall() {
    this.http.post("http://localhost:8069/odoocalc/calculate", { input: this.inputText }, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
      responseType: 'json'
    })
      .pipe( map((response:any) => {
        let { result } = response;
        if(!result) {
          throw new Error("Server is a bit sad and refused to do that :(");
        }
        if(!result.success) {
          throw new Error(result.errorMessage);
        }
        return result;
      })).subscribe(
        r => {
          console.log("Output: "+ r.output);
          this.resultText = r.output;
          this.outputError = false;
        },
        e=> {
          console.error(e);
          this.resultText = e;
          this.outputError = true;
      });
  }
}
