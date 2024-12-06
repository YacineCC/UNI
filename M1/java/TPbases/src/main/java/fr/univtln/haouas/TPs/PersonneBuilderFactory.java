package fr.univtln.haouas.TPs;

public class PersonneBuilderFactory {
    public static Personne.PersonneBuilder createPersonneBuilderBasic(String prenom, String nom) {
        return new Personne.PersonneBuilder(prenom, nom);
    }

    public static Personne.PersonneBuilder createPersonneBuilderwithAnneeNaissance(String prenom, String nom, int anneeNaissance) {
        return new Personne.PersonneBuilder(prenom, nom).withAge(anneeNaissance);
    }

    public static Personne.PersonneBuilder createPersonneBuilderwithSalaire(String prenom, String nom, int salaire) {
        return new Personne.PersonneBuilder(prenom, nom).withSalaire(salaire);
    }

    public static Personne.PersonneBuilder createPersonneBuilderComplete(String prenom, String nom, int anneeNaissance, int salaire) {
        return new Personne.PersonneBuilder(prenom, nom).withAge(anneeNaissance).withSalaire(salaire);
    }
}
