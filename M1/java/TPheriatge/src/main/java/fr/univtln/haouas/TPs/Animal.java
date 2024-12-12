package fr.univtln.haouas.TPs;
/**
 * @author Haouas Yacine.
 */


/**
 * Une classe abstraite Animal qui contient les attributs nom et id communs
 * à tous les animaux et une méthode abstraite crier. Animal ne peut donc pas être instanciée.
 */
public abstract class Animal {
    private String nom;
    private String id;
    private int age;
    private static final int NB_MAX_ANIMAUX = 30;
    private static int nbAnimaux = 0;
    private static final Animal[] animaux = new Animal[NB_MAX_ANIMAUX];


    /**
     * Constructeur de la classe Animal
     * @param nom nom de l'animal.
     * @param id identifiant unique de l'animal.
     * @param age âge de l'animal.
     */
    public Animal(String nom, String id, int age) {
        if (nbAnimaux >= NB_MAX_ANIMAUX)
            throw new IllegalArgumentException("Nombre maximal d'animaux atteint");
        this.nom = nom;
        this.id = id;
        this.age = age;
        this.animaux[this.nbAnimaux] = this;
        this.nbAnimaux++;

    }


    public Animal(){
      super();
    if (nbAnimaux >= NB_MAX_ANIMAUX)
        throw new IllegalArgumentException("Nombre maximal d'animaux atteint");
      this.animaux[this.nbAnimaux] = this;
      this.nbAnimaux++;
    }

    /**
     * Méthode qui retourne le nom de l'animal.
     * @return le nom de l'animal.
     */
    public String getNom() {
        return nom;
    }
    /**
     * Méthode abstraite crier qui doit être implémentée par les classes filles.
     * Cette méthode est abstraite, car chaque animal crie d'une manière différente.
     */
    public abstract void  crier();

    /**
     * Méthode toString qui retourne une chaîne de caractères contenant les informations de l'animal.
     * @return une chaîne de caractères contenant les informations de l'animal
     */

    public String getInfo(){
        if (nom == null && age == 0)
            return "Je suis un animal ";
        else
            return "Je suis un animal âgé de " + age + " an(s)";
    }

    public abstract String moyenExpression();


    public abstract void crier(String espece);

    @Override
    public String toString(){
        return "Animal : nom " + nom + " id " + id;
    }

    public static void afficherCriAnimaux(Animal[] animaux){
        for (Animal animal : animaux) {
            System.out.println(animal.moyenExpression());
        }
    }

    public static void afficherDescriptionAnimaux(){
        for (Animal animal : animaux) {
            if (animal == null)
                continue;
            System.out.println(animal.getInfo() + animal.moyenExpression());
        }
    }

}
