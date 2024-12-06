package fr.univtln.haouas.TPs;
import java.util.Calendar;


public class Personne {
    private final String prenom;
    private final String nom;
    private int anneeNaissance;
    private int salaire;
    private static int totalDesSalaires = 0;
    private final Cerveau cerveau;

    private Personne(PersonneBuilder builder) {
        this.prenom = builder.prenom;
        this.nom = builder.nom;
        this.anneeNaissance = builder.anneeNaissance;
        this.salaire = builder.salaire;
        totalDesSalaires += this.salaire;
        this.cerveau = new Cerveau();
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

    public int comparerSalaire(Personne p) {
        if (this.salaire > p.salaire) {
            return 1;
        } else if (this.salaire < p.salaire) {
            return -1;
        } else {
            return 0;
        }
    }

    public static int comparerSalaire(Personne p1, Personne p2) {
        return p1.salaire - p2.salaire;
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

    public static int getTotalDesSalaires() {
        return totalDesSalaires;
    }

    @Override
    public String toString() {
        return "Personne{" +
                "prenom='" + prenom + '\'' +
                ", nom='" + nom + '\'' +
                ", age=" + getAge() +
                ", salaire=" + salaire +
                ", cerveau=" + cerveau +
                '}';
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (obj.getClass() != this.getClass()) {
            return false;
        }
        Personne p = (Personne) obj;
        return this.anneeNaissance == p.anneeNaissance;
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

    public class Cerveau {
        private int nbNeurones;

        public Cerveau() {
            this.nbNeurones = 0;
        }

        public int getNbNeurones() {
            return nbNeurones;
        }

        public void setNbNeurones(int nbNeurones) {
            this.nbNeurones = nbNeurones;
        }

        @Override
        public String toString() {
            return "Cerveau{" +
                    "nbNeurones=" + nbNeurones +
                    '}';
        }


    }
    public Cerveau getCerveau() {
        return cerveau;
    }
}
