import { Router, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { AdminComponent } from './admin/admin.component';
import { AuthService } from './Service/auth.service';
import { inject } from '@angular/core';
import { AccueilComponent } from './accueil/accueil.component';
import {ListeCritiquesComponent} from "./liste-critiques/liste-critiques.component";

export const utilisateurEstConnecte = () => {
  const authService = inject(AuthService);
  const router = inject(Router);

  if (authService.isLoggedIn) {
   
    return true;
  }

  return router.parseUrl('/login');
};

export const routes: Routes = [
    {
      path: 'login',
      component: LoginComponent,
    },
    {
      path: 'admin',
      component: AdminComponent,
      canActivate: [utilisateurEstConnecte]
    },
    {
      path: 'accueil',
      component: AccueilComponent,
    },
    {
      path: 'critiques',
      component: ListeCritiquesComponent,
    },
    {
      path: 'critiques/:id',
      component: ListeCritiquesComponent,
    },
    { path: '',   redirectTo: '/accueil', pathMatch: 'full' },
];
