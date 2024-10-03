-- Domaines
CREATE DOMAIN tMissions AS VARCHAR(30)
CHECK (VALUE IN ('Braquage', 'Courses', 'Vol de voiture', 'Combats', 'Scénario'));

CREATE DOMAIN tPropriete AS VARCHAR(30)
CHECK (VALUE IN ('Appartement', 'Maison', 'Business'));

CREATE DOMAIN tBusiness AS VARCHAR(30)
CHECK (VALUE IN ('Fabrique faux billets', 'Fabrique de drogue', 'entrepot trafic'));

CREATE DOMAIN tVehicule AS VARCHAR(30)
CHECK (VALUE IN ('Avion', 'Voiture', 'Bateau', 'Helicoptere', 'Velo', 'Moto'));

CREATE DOMAIN tVoiture AS VARCHAR(30)
CHECK (VALUE IN ('Hypercars', 'Sportives', 'Tout-Terrain', 'SUV', 'Vintage', 'Muscle-Car', 'Van'));

CREATE DOMAIN tMoteur AS VARCHAR(30)
CHECK (VALUE IN ('Réaction', 'Hélices', 'Turbine'));

CREATE DOMAIN gMusique AS VARCHAR(30)
CHECK (VALUE IN ('Pop', 'RnB', 'Rock', 'Rap', 'Country', 'Jazz', 'Classique', 'Electro'));

CREATE DOMAIN tVetement AS VARCHAR(30)
CHECK (VALUE IN ('Sportif', 'Mode', 'Formel', 'Costume', 'Streetwear', 'Special'));



-- Contient toutes les commandes créant les tables

-- Les entités
CREATE TABLE Commanditaire
(
    idCommanditaire INTEGER PRIMARY KEY,
    nomCommanditaire VARCHAR(20) NOT NULL,
    adrCommanditaire VARCHAR(30) -- Peut être null -> si commandité par tel par exemple.
);

CREATE TABLE Mission
(
    idMission INTEGER PRIMARY KEY,
    intituleMission VARCHAR(30) NOT NULL,
    typeMission tMissions NOT NULL,
    recompenseArgent INTEGER,
    recompenseXP INTEGER,
    xpRequisPourMission INTEGER,
    idCommanditaire INTEGER REFERENCES Commanditaire,

    CONSTRAINT recompenses_positives
    CHECK (recompenseArgent >= 0 AND recompenseXP >= 0)
);

CREATE TABLE Propriete
(
    idPropriete INTEGER PRIMARY KEY,
    typePropriete tPropriete NOT NULL,
    adrPropriete VARCHAR(30) NOT NULL,
    prixPropriete INTEGER NOT NULL,
    intitulePropriete VARCHAR(30) NOT NULL,

    CONSTRAINT prixPropriete
    CHECK (prixPropriete >= 0)
);

CREATE TABLE Business
(
    idPropriete INTEGER REFERENCES Propriete,
    revenuPassif INTEGER NOT NULL,
    typeBusiness tBusiness NOT NULL,

    CONSTRAINT revenuPassif
    CHECK (revenuPassif >= 0)
);

CREATE TABLE Appartement
(
    idPropriete INTEGER REFERENCES Propriete,
    etageAppart INTEGER NOT NULL,

    CONSTRAINT etageAppart
    CHECK (etageAppart >= 0)
);

CREATE TABLE Maison
(
    idPropriete INTEGER REFERENCES Propriete,
    aPiscine BOOLEAN,
    aJardin BOOLEAN
);

CREATE TABLE Crime
(
    idCrime INTEGER PRIMARY KEY,
    intituleCrime VARCHAR(20),
    incrDegMechancete INTEGER NOT NULL,

    CONSTRAINT incrementMechancete
    CHECK (incrDegMechancete >= 0)
);

CREATE TABLE Arme
(
    idArme INTEGER PRIMARY KEY,
    intituleArme VARCHAR(20) NOT NULL,
    degatArme INTEGER NOT NULL,
    prixArme INTEGER NOT NULL,

    CONSTRAINT degat_et_prix
    CHECK (prixArme >= 0 AND degatArme >= 0)
);

CREATE TABLE Vehicule
(
    idVehicule INTEGER PRIMARY KEY,
    nomVehicule VARCHAR(20),
    prixVehicule INTEGER NOT NULL,
    typeVehicule tVehicule NOT NULL,
    marqueVehicule VARCHAR(20) NOT NULL,
    estBlinde BOOLEAN NOT NULL,
    estArme BOOLEAN NOT NULL,
    capaciteVehicule INTEGER NOT NULL,

    CONSTRAINT prixVehicule
    CHECK (prixVehicule >= 0),

    CONSTRAINT occupantVehicule
    CHECK (capaciteVehicule >= 1 AND capaciteVehicule <= 8)
);

CREATE TABLE Voiture
(
    idVehicule INTEGER REFERENCES Vehicule,
    typeVoiture tVoiture NOT NULL,
    estDecapotable BOOLEAN NOT NULL
);

CREATE TABLE VehiculeSpecial
(
    idVehicule INTEGER REFERENCES Vehicule,
    aBoost BOOLEAN NOT NULL,
    aJump BOOLEAN NOT NULL,
    aParachute BOOLEAN NOT NULL,
    estSousMarin BOOLEAN NOT NULL,
    peutVoler BOOLEAN NOT NULL
);

CREATE TABLE Avion
(
    idVehicule INTEGER REFERENCES Vehicule,
    altMax INTEGER NOT NULL,
    typeMoteur tMoteur NOT NULL,
    trainEstRetractable BOOLEAN NOT NULL,

    CONSTRAINT altitudeAvion
    CHECK (altMax < 100000) -- On ne peut pas aller dans l'espace
);

CREATE TABLE Couleur
(
    idCouleur INTEGER PRIMARY KEY,
    intituleCouleur VARCHAR(15),
    rouge INTEGER NOT NULL,
    vert INTEGER NOT NULL,
    bleu INTEGER NOT NULL,

    -- On vérifie que c'est bien du RGB256
    CONSTRAINT Couleur
    CHECK (rouge >= 0 AND rouge <= 255 AND vert >= 0 AND vert <= 255 AND bleu >= 0 AND bleu <= 255)
);

CREATE TABLE Joueur
(
    idJoueur INTEGER PRIMARY KEY,
    nomJoueur VARCHAR(25),
    hpMax FLOAT(2) NOT NULL,
    endurance FLOAT(2) NOT NULL,
    precision FLOAT(2) NOT NULL,
    force FLOAT(2) NOT NULL,
    discretion FLOAT(2) NOT NULL,
    pilotage FLOAT(2) NOT NULL,
    conduite FLOAT(2) NOT NULL,
    degMechancete INTEGER NOT NULL,
    argent INTEGER NOT NULL,
    experience INTEGER NOT NULL,

    -- On gère les coeff des statistiques
    CONSTRAINT hpMax
    CHECK (hpMax >= 1.0 AND hpMax <= 2.0),

    CONSTRAINT endurance
    CHECK (endurance >= 1.0 AND endurance <= 2.0),

    CONSTRAINT precision
    CHECK (precision >= 1.0 AND precision <= 2.0),


    CONSTRAINT force
    CHECK (force >= 1.0 AND force <= 2.0),

    CONSTRAINT discretion
    CHECK (discretion >= 1.0 AND discretion <= 2.0),

    CONSTRAINT pilotage
    CHECK (pilotage >= 1.0 AND pilotage <= 2.0),

    CONSTRAINT conduite
    CHECK (conduite >= 1.0 AND conduite <= 2.0),

    -- Max 250 000 xp
    CONSTRAINT experience
    CHECK (experience >= 0 AND experience <= 250000),

    CONSTRAINT argent
    CHECK (argent >= 0)     -- Pas de limite d'argent
);

CREATE TABLE Musique
(
    idMusique INTEGER PRIMARY KEY,
    nomMusique VARCHAR(20) NOT NULL,
    genreMusique gMusique NOT NULL,
    dureeMusique INTEGER NOT NULL,

    CONSTRAINT dureeMusique
    CHECK (dureeMusique >= 0)
);

CREATE TABLE Chanteur
(
    idChanteur INTEGER PRIMARY KEY,
    nomChanteur VARCHAR(20) NOT NULL
);

CREATE TABLE Station
(
    idStation INTEGER PRIMARY KEY, -- Prof veut pas de float / string en PK
    genreStation gMusique NOT NULL,
    freq FLOAT(2)
);

CREATE TABLE HostRadio
(
    idHost INTEGER PRIMARY KEY,
    nomHost VARCHAR(20)
);

CREATE TABLE Vetement
(
    idVetement INTEGER PRIMARY KEY,
    typeVetement tVetement NOT NULL,
    intituleVetement VARCHAR(20) NOT NULL,
    prixVetement INTEGER NOT NULL,

    CONSTRAINT prixVetement
    CHECK (prixVetement >= 0)
);

CREATE TABLE BoutiqueVetement
(
    idBoutique INTEGER PRIMARY KEY,
    nomBoutique VARCHAR(20),
    adrBoutique VARCHAR(30)
);


-- Liens n:m
CREATE TABLE MissionNecessitePropriete
(
    idMission INTEGER REFERENCES Mission,
    idPropriete INTEGER REFERENCES Propriete,

    PRIMARY KEY(idMission, idPropriete)
);

CREATE TABLE MissionNecessiteVehicule
(
    idMission INTEGER REFERENCES Mission,
    idVehicule INTEGER REFERENCES Vehicule,

    PRIMARY KEY(idMission, idVehicule)
);

CREATE TABLE MissionFaitCommettreCrime
(
    idMission INTEGER REFERENCES Mission,
    idCrime INTEGER REFERENCES Crime,

    PRIMARY KEY(idMission, idCrime)
);

CREATE TABLE MissionNecessiteArme
(
    idMission INTEGER REFERENCES Mission,
    idArme INTEGER REFERENCES Arme,

    PRIMARY KEY(idMission, idArme)
);

CREATE TABLE JoueurRealiseMission
(
    idJoueur INTEGER REFERENCES Joueur,
    idMission INTEGER REFERENCES Mission,

    PRIMARY KEY(idJoueur, idMission)
);

CREATE TABLE JoueurCommetCrime
(
    idJoueur INTEGER REFERENCES Joueur,
    idCrime INTEGER REFERENCES Crime,
    dateCrime DATE NOT NULL,

    PRIMARY KEY(idJoueur, idCrime, dateCrime)
);

CREATE TABLE JoueurPossedeArme
(
    idJoueur INTEGER REFERENCES Joueur,
    idArme INTEGER REFERENCES Arme,

    PRIMARY KEY(idJoueur, idArme)
);

CREATE TABLE JoueurPossedePropriete
(
    idJoueur INTEGER REFERENCES Joueur,
    idPropriete INTEGER REFERENCES Propriete,

    PRIMARY KEY(idJoueur, idPropriete)
);

CREATE TABLE JoueurPossedeVehicule
(
    idJoueur INTEGER REFERENCES Joueur,
    idVehicule INTEGER REFERENCES Vehicule,
    dateAchatVehicule DATE NOT NULL,

    PRIMARY KEY(idJoueur, idVehicule, dateAchatVehicule)
);

CREATE TABLE VehiculeDeCouleur
(
    idVehicule INTEGER REFERENCES Vehicule,
    idCouleur INTEGER REFERENCES Couleur,

    PRIMARY KEY(idVehicule, idCouleur)
);

CREATE TABLE JoueurEcouteStation
(
    idJoueur INTEGER REFERENCES Joueur,
    idStation INTEGER REFERENCES Station,

    PRIMARY KEY(idJoueur, idStation)
);

CREATE TABLE StationDiffuseMusique
(
    idStation INTEGER REFERENCES Station,
    idMusique INTEGER REFERENCES Musique,

    PRIMARY KEY(idStation, idMusique)
);

CREATE TABLE MusiqueInterpreteeParChanteur
(
    idMusique INTEGER REFERENCES Musique,
    idChanteur INTEGER REFERENCES Chanteur,

    PRIMARY KEY(idMusique, idChanteur)
);

CREATE TABLE StationAnimeeParHost
(
    idStation INTEGER REFERENCES Station,
    idHost INTEGER REFERENCES HostRadio,

    PRIMARY KEY(idStation, idHost)
);

CREATE TABLE JoueurPossedeVetement
(
    idJoueur INTEGER REFERENCES Joueur,
    idVetement INTEGER REFERENCES Vetement,
    idCouleurVetement INTEGER REFERENCES Couleur,

    PRIMARY KEY(idJoueur, idVetement, idCouleurVetement)
);

CREATE TABLE VetementVenduChezBoutique
(
    idVetement INTEGER REFERENCES Vetement,
    idBoutique INTEGER REFERENCES BoutiqueVetement,

    PRIMARY KEY(idVetement, idBoutique)
);
