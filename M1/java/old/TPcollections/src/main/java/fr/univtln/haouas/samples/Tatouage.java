package fr.univtln.haouas.samples;

import java.util.Objects;

public final class Tatouage {
    private final String espece;
    private final int numero;

    public Tatouage(String espece, int numero) {
        this.espece = espece;
        this.numero = numero;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Tatouage tatouage = (Tatouage) o;
        return this.numero == tatouage.numero;
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(numero);
    }
}