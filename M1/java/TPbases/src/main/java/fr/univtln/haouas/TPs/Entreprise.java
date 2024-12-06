package fr.univtln.haouas.TPs;

public class Entreprise {
    private static final int MAX_EMPLOYEES = 100;
    private String nom;
    private Personne[] employees = new Personne[MAX_EMPLOYEES];
    private TypeEntreprise type;

    public enum TypeEntreprise {
        PUBLIQUE, PME, GRAND_GROUPE
    }

    public Entreprise(TypeEntreprise type, String nom, Personne[] employees) {
        this.type = type;
        this.nom = nom;
        this.employees = employees;
    }

    public boolean isPublic() {
        return type == TypeEntreprise.PUBLIQUE;
    }

    public boolean isPME() {
        return type == TypeEntreprise.PME;
    }

    public boolean isGrandGroupe() {
        return type == TypeEntreprise.GRAND_GROUPE;
    }

    public boolean addEmployee(Personne p) {
        for (int i = 0; i < MAX_EMPLOYEES; i++) {
            if (employees[i] == null) {
                employees[i] = p;
                return true;
            }
        }
        return false;
    }

    public void afficherEmployes() {
        for(Personne e:employees) {
            if (e != null) {
                System.out.println(e);
            }
        }
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public TypeEntreprise getType() {
        return type;
    }

    public void setType(TypeEntreprise type) {
        this.type = type;
    }

    public Personne[] getEmployees() {
        return employees;
    }

    public void miseEnForme() {
        for(Personne e:employees) {
            if (e != null)
                System.out.println(e.getNom().toUpperCase());
        }
    }

}
