package fr.univtln.haouas.TPs;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");

        Homme homme = new Homme("Homme", "H001", 9, 100, 30);
        homme.crier();
        Aigle aigle = new Aigle("Aigle", "A001", 100, "brun", 10);
        aigle.crier();

        Lapin lapin = new Lapin("Lapin", "L001", 1, "32", 2);
        lapin.crier();

        Plante plante = new Plante("Plante", "Vert");
        plante.pousser();

        System.out.println("Homme: " + homme);
        System.out.println("Aigle: " + aigle);
        System.out.println("Lapin: " + lapin);
        System.out.println("Plante: " + plante);

        Animal[] animaux = {new Chien("Medor", "C001", 9, "rouge", 5),
                new Homme(),
            new Homme("Robert", "H002", 9, 200, 30),
            new Aigle("Aigle", "A002", 100, "brun", 10),
            new Lapin("Lapin", "L002", 1, "32", 2),
            new Chien("Rex", "C002", 9, "rouge", 5),
            new Chien("Rocky", "C003", 9, "bleu", 7)};//,
            //new Chien("Rex", "C004", 9, "rouge", 5)};
        for (Animal animal : animaux) {
            System.out.println(animal.getInfo());
        }

        Animal.afficherCriAnimaux(animaux);
        System.out.println("\nyoloooo\n");
        Animal.afficherDescriptionAnimaux();

        ICarnivore[] lesCarnivore = {new Chien("Medor", "C001", 9, "rouge", 5),
                new Aigle("Aigle", "A002", 100, "brun", 10),
                new Chien("Rex", "C002", 9, "rouge", 5),
                new Chien("Rocky", "C003", 9, "bleu", 7),
        new Homme("Robert", "H002", 9, 200, 30)};

        IHerbivore vachette = new Vache("Vachette", "V001", 9, "blanche", 5);
        IHerbivore[] lesHerbivore = {new Lapin("Lapin", "L002", 1, "32", 2),
                vachette,
                new Homme("Robert", "H002", 9, 200, 30)};

        Animal Lapinou = new Lapin("Lapinou", "L003", 1, "32", 2);

        for (ICarnivore carnivore : lesCarnivore) {
            carnivore.manger(Lapinou);
        }

        Plante plante1 = new Plante("Plante test", "Vert");
        for (IHerbivore herbivore : lesHerbivore) {
            herbivore.manger(plante1);
        }

        //vachette.moyenExpression(); // Error: method moyenExpression() is not found in interface IHerbivore

        Animal vachette2 = new Vache("Vachette2", "V002", 9, "blanche", 5);
        System.out.println(vachette2.moyenExpression());
}
}
