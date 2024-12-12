package fr.univtln.haouas.TPs;

public class Plante {
    private String nom;
    private String couleur;

    public Plante(String nom, String couleur) {
        this.nom = nom;
        this.couleur = couleur;
    }

    public void pousser() {
        System.out.println("La plante pousse");
    }

    @Override
    public String toString() {
        return "Plante{" +
                "nom='" + nom + '\'' +
                ", couleur='" + couleur + '\'' +
                '}';
    }

    public String getNom() {
        return nom;
    }

}
