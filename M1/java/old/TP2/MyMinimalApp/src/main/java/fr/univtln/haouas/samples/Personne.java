package fr.univtln.haouas.samples;


import java.util.Calendar;

//Builder Pattern
public class Personne {
    private final String nom;
    private final String prenom;
    private int age;
    private int salaire;
    private int annee_naissance;

    public static class Builder {
        //Paramètres requis.
        private final String nom;
        private final String prenom;


        //Paramètre optionnels.
        private int age             = -1;
        private int salaire         = -1;
        private int annee_naissance = -1;

        public Builder(String nom, String prenom) {
            this.nom    = nom;
            this.prenom = prenom;
        }

        public Builder salaire(int val)
            {salaire = val; return this;}
        public Builder annee_naissance(int val)
            {annee_naissance = val; age = java.util.Calendar.getInstance().get(Calendar.YEAR) - annee_naissance; return this;}

        public Personne build() {
            return new Personne(this);
        }
    }

    public Personne(Builder builder) {
        nom     = builder.nom;
        prenom  = builder.prenom;
        age     = builder.age;
        salaire = builder.salaire;
        annee_naissance = builder.annee_naissance;
    }


    public String getNom() {
        return nom;
    }
    public String getPrenom() {
        return prenom;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public int getSalaire() {
        return salaire;
    }

    public void setSalaire(int salaire) {
        if(salaire > 0) {
            this.salaire = salaire;
        }
    }


}
