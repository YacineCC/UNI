package fr.univtln.haouas.samples;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        Personne p1 = new Personne.Builder("Truc", "Pierre").annee_naissance(1979).salaire(2000).build() ;


        System.out.println(p1.getNom());
        System.out.println(p1.getPrenom());
        System.out.println(p1.getAge());
        System.out.println(p1.getSalaire());


    }


}
