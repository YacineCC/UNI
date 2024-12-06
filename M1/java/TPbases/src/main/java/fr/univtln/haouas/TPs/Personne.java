package fr.univtln.haouas.TPs;

public class Personne {
    private final String prenom;
    private final String nom;
    private int age = -1;
    private int salaire = -1;

    public Personne(Builder builder) {
        this.prenom = builder.prenom;
        this.nom = builder.nom;
        this.age = builder.age;
        this.salaire = builder.salaire;
    }

    public String getPrenom() {
        return prenom;
    }

    public String getNom() {
        return nom;
    }

    public int getAge() {
        return age;
    }

    public int getSalaire() {
        return salaire;
    }


    public void setAge(int age) {
        this.age = age;
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
                ", age=" + age +
                ", salaire=" + salaire +
                '}';
    }

    public static class Builder {
        private final String prenom;
        private final String nom;
        private int age = -1;
        private int salaire = -1;

        public Builder(String prenom, String nom) {
            this.prenom = prenom;
            this.nom = nom;
        }

        public Builder age(int age) {
            this.age = age;
            return this;
        }

        public Builder salaire(int salaire) {
            this.salaire = salaire;
            return this;
        }

        public Personne build() {
            return new Personne(this);
        }

    }
}
