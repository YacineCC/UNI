package fr.univtln.haouas.TPs;
import java.util.Calendar;


public class Personne {
    private final String prenom;
    private final String nom;
    private int anneeNaissance;
    private int salaire;

    private Personne(PersonneBuilder builder) {
        this.prenom = builder.prenom;
        this.nom = builder.nom;
        this.anneeNaissance = builder.anneeNaissance;
        this.salaire = builder.salaire;
    }

    public String getPrenom() {
        return prenom;
    }

    public String getNom() {
        return nom;
    }

    public int getAge() {
        if (anneeNaissance == -1) {
            return -1;
        }
        else {
            return Calendar.getInstance().get(Calendar.YEAR) - anneeNaissance;
        }
    }

    public int getAnneeNaissance() {
        return anneeNaissance;
    }


    public int getSalaire() {
        return salaire;
    }


    public void setAnneeNaissance(int anneeNaissance) {
        this.anneeNaissance = anneeNaissance;
    }

    public void setSalaire(int salaire) {
        if (salaire < 0) {
            throw new IllegalArgumentException("Le salaire doit être positif");
        } else {
            this.salaire = salaire;
        }
    }

    @Override
    public String toString() {
        return "Personne{" +
                "prenom='" + prenom + '\'' +
                ", nom='" + nom + '\'' +
                ", age=" + getAge() +
                ", salaire=" + salaire +
                '}';
    }

    public static class PersonneBuilder {
        private final String prenom;
        private final String nom;
        private int anneeNaissance = -1;
        private int salaire = -1;

        public PersonneBuilder(String prenom, String nom) {
            this.prenom = prenom;
            this.nom = nom;
        }

        public PersonneBuilder withAge(int anneeNaissance) {
            this.anneeNaissance = anneeNaissance;
            return this;
        }

        public PersonneBuilder withSalaire(int salaire) {
            if (salaire < 0) {
                throw new IllegalArgumentException("Le salaire doit être positif");
            }
            else {
                this.salaire = salaire;
                return this;
            }

        }

        public Personne build() {
            return new Personne(this);
        }

    }
}
