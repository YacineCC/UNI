package fr.univtln.haouas.samples;

public abstract class Animal {
    private String nom;
    private static Animal[] animaux = new Animal[10];
    private static int NB = 0;

    public Animal(String nom) {
        this.nom = nom;
        animaux[NB++] = this;
    }
    public abstract void crier();

    public static void faireCrier() {
        for(Animal a:animaux) a.crier();
    }

    public String getNom() {
        return nom;
    }

}
