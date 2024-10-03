from __future__ import annotations

class Materiaux:
    """ Le materiau d'un objet représente ses coefficients ambiant, diffus,
    spéculaire, sa puissance spéculaire. Si l'objet est réfléchissant son
    coef_r sera > 0, si il est transparent son indice de réfraction est > 0."""

    def __init__(self, ambiant : float, diffus : float, speculaire : float, n : int, coef_r : float, transparence : bool, indice_refraction : float=0) -> None:
        self.ambiant = ambiant
        self.diffus = diffus
        self.speculaire = speculaire
        self.n = n
        self.coef_r = coef_r
        self.transparence = transparence
        self.indice_refraction = indice_refraction
        
    def __str__(self) -> str:
        return f'ambiant : {self.ambiant}\n diffus : {self.diffus}\n speculaire : {self.speculaire}\n n : {self.n}\n coef_r : {self.coef_r}\n transparence : {self.transparence}'
    

    def __repr__(self) -> str:
        return str(self)


"""Quelques Variables globales utiles pour le main. Représention simplifié de 
matériaux courant."""
VERRE = Materiaux(ambiant=0.3, diffus=0.5, speculaire=0.7, n=100, coef_r=0, transparence=True, indice_refraction=5)
MAT = Materiaux(ambiant=0.2, diffus=0.5, speculaire=0.5, n=30, coef_r=0, transparence=False)
BRILLANT = Materiaux(ambiant=0.3, diffus=0.7, speculaire=0.7, n=100, coef_r=0.65, transparence=False)
MIRROIR = Materiaux(ambiant=0.3, diffus=0.5, speculaire=0.7, n=100, coef_r=1, transparence=False)