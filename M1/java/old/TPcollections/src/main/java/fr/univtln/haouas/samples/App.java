package fr.univtln.haouas.samples;

import java.util.HashSet;
import java.util.TreeSet;
import java.util.Set;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        AnimalFactory factory = new AnimalFactory();
        Animal tiger = factory.createAnimal("Sagat", 33, "Tigre", 95);
        System.out.println(tiger);

        //Set<Animal> animaux = new HashSet<>();
        Set<Animal> animaux = new TreeSet<>();


        Animal lion1 = new Animal("Leo", 5, "Lion", 100);
        Animal lion2 = new Animal("Leo", 3, "Lion", 100);
        animaux.add(lion1);
        animaux.add(lion2);
        animaux.add(tiger);
        System.out.println(animaux);
        System.out.println(tiger == lion1);
        System.out.println(lion1.equals(lion2));
        //Animal.parcoursIterator(animaux);
        //Animal.parcoursForEach(animaux);

        Animal[] desAnimaux = new Animal[animaux.size()];
        animaux.toArray(desAnimaux);
        desAnimaux.append(lion2);
        


    }

}
