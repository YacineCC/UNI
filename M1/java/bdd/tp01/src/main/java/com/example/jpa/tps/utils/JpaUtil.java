package com.example.jpa.tps.utils;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

public class JpaUtil {
    private static final EntityManagerFactory emf =
            Persistence.createEntityManagerFactory("tpJakartaUnit");

    public static EntityManagerFactory getEntityManagerFactory() {
        return emf;
    }
    public static void close() {
        emf.close();
    }
}
