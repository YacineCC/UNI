package fr.univtln.haouas.TPs;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        Personne p1 = new Personne("Pierre", "Truc", 30, 2000);
        System.out.println(p1);
        p1.setAge(31);
        p1.setSalaire(2100);
        System.out.println(p1);
    }
}
