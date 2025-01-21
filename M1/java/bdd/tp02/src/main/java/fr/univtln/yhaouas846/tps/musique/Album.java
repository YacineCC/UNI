package fr.univtln.yhaouas846.tps.musique;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

@Entity @Getter @Setter
public class Album {
    @Id @GeneratedValue
    private Long id;
    private String title;
    private LocalDate releaseDate;

    @ManyToOne
    private Artist artist;
}