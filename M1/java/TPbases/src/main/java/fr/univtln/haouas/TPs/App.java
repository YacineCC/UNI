package fr.univtln.haouas.TPs;
import java.util.Calendar;
/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        System.out.println(Personne.getTotalDesSalaires());
        Personne p1 = PersonneBuilderFactory.createPersonneBuilderComplete("Pierre", "Truc", 1990, 2000).build();
        System.out.println(Personne.getTotalDesSalaires());
        Personne p2 = PersonneBuilderFactory.createPersonneBuilderwithSalaire("Paul", "Bidule", 5000).build();

        System.out.println(p1);
        p1.setAnneeNaissance(Calendar.getInstance().get(Calendar.YEAR) - 25);
        p1.setSalaire(2100);
        System.out.println(p1);
        System.out.println(p2);
        System.out.println("Comparer salaire p1 p2" + p1.comparerSalaire(p2));
        System.out.println("Comparer salaire p1 p2 (statique)" +Personne.comparerSalaire(p1, p2));
        System.out.println("p1 == p2 ? " + p1.equals(p2));
        p2.setAnneeNaissance(p1.getAnneeNaissance());
        p2.getCerveau().setNbNeurones(100);
        System.out.println(p2);
        System.out.println("p1 == p2 ? " + p1.equals(p2));
        System.out.println(p1.getAnneeNaissance());
        System.out.println(p2.getAnneeNaissance());

        Personne[] employes = new Personne[100];
        employes[0] = p1;
        employes[1] = p2;
        Entreprise e = new Entreprise(Entreprise.TypeEntreprise.PME, "MaBoite", employes);
        System.out.println("PME ? " + e.isPME());
        System.out.println("Grand groupe ? " +e.isGrandGroupe());
        System.out.println("Publique ? " + e.isPublic());
        e.afficherEmployes();
        e.miseEnForme();
        e.afficherEmployes();


    }
}
