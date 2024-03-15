/**
 * Interface pour les critiques
 * @export CritiqueInterface
 * @interface CritiqueInterface
 * @description Cette interface définit la structure des critiques.
 */
export interface CritiqueInterface {
  id: number | null;
  attraction_id: number | null;
  attraction_nom: string | null;
  nom: string;
  prenom: string;
  texte: string;
  note: number;
}
