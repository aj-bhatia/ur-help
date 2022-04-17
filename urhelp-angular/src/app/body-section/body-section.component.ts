import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';

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
    private formBuilder: FormBuilder
  ) { }

  onEnable(): void{
    console.warn('phone number has been registered', this.checkoutForm.value)
    this.checkoutForm.reset();
  }

  ngOnInit(): void {
  }

}
