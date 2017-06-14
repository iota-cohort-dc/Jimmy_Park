import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Dojo Mail';
  emails = [
    {email: ["Jimmy@email.com", "Lisa@email.com", "Tammy@email.com", "Rachael@email.com"]}, {importance: [true, true, false, false]},
    {subject:["Motorcycle", "Eating Out", "Vacations", "Family time"]},
    {content:["Smooth Roads", "Cheesecake Factory", "Some Sunny Beach", "White sandy beach"] }
  ]
}
