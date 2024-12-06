package fr.univtln.haouas.samples;

public class Oiseau extends Animal{
    private String nom;
    public void crier(){System.out.println("je vooooole");}

    public Oiseau(String nom) {
        super(nom);
    }
}
