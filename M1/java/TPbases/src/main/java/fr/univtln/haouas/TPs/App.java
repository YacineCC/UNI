package fr.univtln.haouas.TPs;
import java.util.Calendar;
/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");

        Personne p1 = PersonneBuilderFactory.createPersonneBuilderComplete("Pierre", "Truc", 1990, 2000).build();
        Personne p2 = PersonneBuilderFactory.createPersonneBuilderBasic("Paul", "Bidule").build();

        System.out.println(p1);
        p1.setAnneeNaissance(Calendar.getInstance().get(Calendar.YEAR) - 25);
        p1.setSalaire(2100);
        System.out.println(p1);
        System.out.println(p2);
    }
}
