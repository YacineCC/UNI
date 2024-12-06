package fr.univtln.haouas.samples;
import java.util.Map;
import java.util.Queue;

public class Clinique {
    private Map<Tatouage, Animal> registre;
    private Queue<Animal> salleAttente;

    public void ajouterAnimal(Animal animal) {
        Tatouage tatouage = animal.getTatouage();
        if (registre.containsKey(tatouage)) {
            throw new IllegalArgumentException("L'animal est déjà enregistré");
        }
        registre.put(tatouage, animal);
    }

    public Animal chercherAnimal(Tatouage tatouage) {
        return registre.get(tatouage);
    }

    public void ajouterSalleAttente(Animal animal) {
        if (salleAttente.contains(animal)) {
            throw new IllegalArgumentException("L'animal est déjà en salle d'attente");
        }
        salleAttente.add(animal);
    }
}