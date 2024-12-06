package fr.univtln.haouas.samples;

public class AnimalFactory {

        public Animal createAnimal(String nom, int age, String espece, double poids) {
            return new Animal(nom, age, espece, poids);
        }
    }
