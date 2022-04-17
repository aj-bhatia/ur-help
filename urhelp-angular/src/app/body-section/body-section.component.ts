import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';

export interface customType{
}

@Component({
  selector: 'app-body-section',
  templateUrl: './body-section.component.html',
  styleUrls: ['./body-section.component.css']
})
export class BodySectionComponent implements OnInit { 

  checkoutForm = this.formBuilder.group({
    phone_number: ''
  });

  constructor(
    private formBuilder: FormBuilder,
  ) { }

  onEnable(): void {
    var x = this.checkoutForm.value['phone_number']
    console.warn('phone number has been registered', x) //send in phone number
    this.checkoutForm.reset();
    fetch('https://ScrapeUkraineNews.crazychicken442.repl.co/add?number='+x)
}

private handleError(error: any): Promise<any> {
  console.error('An error occurred', error);
  return Promise.reject(error.message || error);
}
   

  ngOnInit(): void {
  }

}
