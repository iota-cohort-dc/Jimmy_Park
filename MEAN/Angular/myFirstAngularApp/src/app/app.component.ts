import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title: string = 'This is Jimmys Angular!'; // this will get sent to the front end in the app.component.html
  x: number = 1000;
  y: number = 9899;
  mystr: string = "This is my test for angular";
  name = 'Bill Gates'
  today = new Date();
  user = {
    first_name: 'Darth',
    last_name: 'Vadar'
  }

  myBoolean = true;
  myArray = [2,4,7,3,673,,33,754,45,5678,22];
  color = 'red';





}
