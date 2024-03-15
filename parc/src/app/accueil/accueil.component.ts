import { Component } from '@angular/core';
import { AttractionService } from '../Service/attraction.service';
import { CommonModule } from '@angular/common';
import {Observable, of} from 'rxjs';
import { AttractionInterface } from '../Interface/attraction.interface';
import { MatCardModule } from '@angular/material/card';
import {MatDialog} from "@angular/material/dialog";
import {MatButton} from "@angular/material/button";
import {RouterLink} from "@angular/router";
import {MatLabel} from "@angular/material/form-field";
import {MatProgressSpinner} from "@angular/material/progress-spinner";

@Component({
  selector: 'app-accueil',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatButton, RouterLink, MatLabel, MatProgressSpinner],
  templateUrl: './accueil.component.html',
  styleUrl: './accueil.component.scss'
})
export class AccueilComponent {
  public loading: boolean = true; // Ajoutez cette ligne

  constructor(
    public attractionService: AttractionService,
    public dialog: MatDialog
  )
  {
    this.loadAttractions();
  }

  public attractions: Observable<AttractionInterface[]> = this.attractionService.getAllAttractionWithMoyenne();

  loadAttractions() {
    this.attractionService.getAllAttractionWithMoyenne().subscribe({
      next: (attractions) => {
        this.attractions = of(attractions); // Assurez-vous que 'attractions' est un Observable
        this.loading = false; // Masquez le spinner une fois les données chargées
      },
      error: () => {
        this.loading = false; // Masquez également le spinner en cas d'erreur
      }
    });
  }


  
}
