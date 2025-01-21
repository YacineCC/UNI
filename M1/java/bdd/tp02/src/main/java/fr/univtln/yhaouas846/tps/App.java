package fr.univtln.yhaouas846.tps;

import fr.univtln.yhaouas846.tps.person.Person;
import fr.univtln.yhaouas846.tps.utils.JpaUtil;
import jakarta.persistence.EntityManager;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        EntityManager em = JpaUtil.getEntityManagerFactory().createEntityManager();

        // Persistance d'une entité
        em.getTransaction().begin();
        Person person = new Person("Alice", 25);
        em.persist(person);
        em.getTransaction().commit();

        // Lecture de l'entité persistée
        Person foundPerson = em.find(Person.class, person.getId());
        System.out.println("Person found: " + foundPerson.getName() + ", Age: " + foundPerson.getAge());

        em.close();
        JpaUtil.close();
    }
}
