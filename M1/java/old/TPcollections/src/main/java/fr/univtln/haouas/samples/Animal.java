package fr.univtln.haouas.samples;

import java.time.LocalDate;
import java.util.Iterator;
import java.util.Set;

public class Animal implements Comparable<Animal> {
    private String nom;
    private int age;
    private String espece;
    private double poids ;
    private LocalDate dernierExamen = LocalDate.now();
    private Tatouage tatouage;

    public String getNom() {
        return nom;
    }
    public int getAge() {
        return age;
    }
    public String getEspece() {
        return espece;
    }
    public double getPoids() {
        return poids;
    }
    public LocalDate getDernierExamen() {
        return dernierExamen;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public void setEspece(String espece) {
        this.espece = espece;
    }
    public void setPoids(double poids) {
        this.poids = poids;
    }
    public void setDernierExamen(LocalDate dernierExamen) {
        this.dernierExamen = dernierExamen;
    }

    public Animal(String nom, int age, String espece, double poids) {
        this.nom = nom;
        this.age = age;
        this.espece = espece;
        this.poids = poids;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Animal animal = (Animal) o;
        return this.nom.equals(animal.nom);
    }

    @Override
    public String toString() {
        return "{Nom: "+this.nom+", age: "+this.age+", espece: "+this.espece+", poids: "+this.poids+"}";
    }

    @Override
    public int hashCode() {
        return this.nom.hashCode();
    }

    @Override
    public int compareTo(Animal o) {
        return o.nom.compareTo(this.nom);
    }



    public static void parcoursIterator(Set<Animal> animaux){
            Iterator<Animal> itAnimaux = animaux.iterator();
            while(itAnimaux.hasNext()){
                Animal animal = itAnimaux.next();
                System.out.println(animal);
            }
    }
    
    public static void parcoursForEach(Set<Animal> animaux){
        for (Animal animal : animaux) {
            System.out.println(animal);
        }
    }

}
