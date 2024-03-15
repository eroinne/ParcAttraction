import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListeCritiquesComponent } from './liste-critiques.component';

describe('ListeCritiquesComponent', () => {
  let component: ListeCritiquesComponent;
  let fixture: ComponentFixture<ListeCritiquesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListeCritiquesComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ListeCritiquesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
