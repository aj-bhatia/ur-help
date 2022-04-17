import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BodySectionComponent } from './body-section/body-section.component';
import { EnableComponent } from './enable/enable.component';

@NgModule({
  declarations: [
    AppComponent,
    BodySectionComponent,
    EnableComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule
    // RouterModule.forRoot([
    //   {path: '', component: BodySectionComponent },
    //   {path: 'enable', component: EnableComponent}
    // ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
