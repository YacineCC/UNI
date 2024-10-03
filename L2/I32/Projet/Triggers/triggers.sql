-- Fonction pour retirer de l'argent au joueur
-- Paramètres: L'id du joueur et le montant à retirer.
CREATE OR REPLACE FUNCTION retireArgent(INTEGER, INTEGER)
AS $$
    BEGIN
        UPDATE Joueur
        SET argent = argent - $2
        WHERE idJoueur = $1;
    END;
$$ LANGUAGE PLPGSQL;


-- Fonction pour récupérer l'argent du joueur
-- Paramètre: L'id du joueur.
CREATE OR REPLACE FUNCTION getArgentJoueur(INTEGER)
RETURNS INTEGER
AS $$
    DECLARE argentJoueur INTEGER := 0;
    BEGIN 
        SELECT argent
        FROM Joueur
        WHERE Joueur.idJoueur = new.idJoueur
        INTO argentJoueur;

        RETURN argentJoueur;
    END;
$$ LANGUAGE PLPGSQL;



-- Fonction pour ajouter de l'argent au joueur
-- Paramètres: id du joueur, argent à ajouter
CREATE OR REPLACE FUNCTION giveArgentJoueur(INTEGER, INTEGER)
AS $$
    BEGIN 
        UPDATE Joueur
        SET argent = argent + $2
        WHERE idJoueur = $1;
    END;
$$ LANGUAGE PLPGSQL;


-- Fonction pour ajouter de l'xp au joueur
-- Paramètres: id du joueur, xp à ajouter
CREATE OR REPLACE FUNCTION giveXpJoueur(INTEGER, INTEGER)
AS $$
    BEGIN 
        UPDATE Joueur
        SET experience = experience + $2    -- Besoin de vérifier si dépasse 250 000 ?
        WHERE idJoueur = $1;
    END;
$$ LANGUAGE PLPGSQL;



-- Fonction pour ajouter les crimes commis au cours des missions.
-- appelée seulement si mission complétée.
-- Paramètres: l'id du jouer, l'id de la mission
CREATE OR REPLACE FUNCTION ajoutCrimesMission(INTEGER, INTEGER)
AS $$
    -- Demander au prof comment faire car plusieurs crimes peuvent être commis




-- Trigger achat arme
CREATE TRIGGER checkAchatArme
    BEFORE INSERTION ON JoueurPossedeArme
    FOR EACH ROW
    EXECUTE PROCEDURE checkAchatArme();


CREATE OR REPLACE FUNCTION checkAchatArme()
RETURNS TRIGGER
AS $$
    DECLARE 
        argent_joueur INTEGER := getArgentJoueur(new.idJoueur);
        prix INTEGER := new.prixArme;
    BEGIN
        IF (argent_joueur >= prix) THEN     -- Besoin de vérifier ou domaine suffisant ?
            retireArgent(new.idJoueur, prix)
            RETURN new;
        ENDIF;

        RAISE INFO 'Pas assez pour acheter, il manque % €', (prix - argent_joueur);
        RETURN NULL;
    END;
$$ LANGUAGE PLPGSQL;



-- Trigger achat propriété
CREATE TRIGGER checkAchatPropriete
    BEFORE INSERTION ON JoueurPossedePropriete
    FOR EACH ROW
    EXECUTE PROCEDURE checkAchatPropriete();


CREATE OR REPLACE FUNCTION checkAchatPropriete()
RETURNS TRIGGER
AS $$
    DECLARE 
        argent_joueur INTEGER := getArgentJoueur(new.idJoueur);
        prix INTEGER := new.prixPropriete;
    BEGIN
        IF (argent_joueur >= prix) THEN 
            retireArgent(new.idJoueur, prix)
            RETURN new;
        ENDIF;

        RAISE INFO 'Pas assez pour acheter, il manque % €', (prix - argent_joueur);
        RETURN NULL;
    END;
$$ LANGUAGE PLPGSQL;


-- Trigger achat véhicule
CREATE TRIGGER checkAchatVehicule
    BEFORE INSERTION ON JoueurPossedeVehicule
    FOR EACH ROW
    EXECUTE PROCEDURE checkAchatVehicule();


CREATE OR REPLACE FUNCTION checkAchatVehicule()
RETURNS TRIGGER
AS $$
    DECLARE 
        argent_joueur INTEGER := getArgentJoueur(new.idJoueur);
        prix INTEGER := new.prixVehicule;
    BEGIN
        IF (argent_joueur >= prix) THEN 
            retireArgent(new.idJoueur, prix)
            RETURN new;
        ENDIF;

        RAISE INFO 'Pas assez pour acheter, il manque % €', (prix - argent_joueur);
        RETURN NULL;
    END;
$$ LANGUAGE PLPGSQL;



-- Trigger achat vêtement
CREATE TRIGGER checkAchatVetement
    BEFORE INSERTION ON JoueurPossedeVetement
    FOR EACH ROW
    EXECUTE PROCEDURE checkAchatVetement();


CREATE OR REPLACE FUNCTION checkAchatVetement()
RETURNS TRIGGER
AS $$
    DECLARE 
        argent_joueur INTEGER := getArgentJoueur(new.idJoueur);
        prix INTEGER := new.prixVetement;
    BEGIN
        IF (argent_joueur >= prix) THEN 
            retireArgent(new.idJoueur, prix)
            RETURN new;
        ENDIF;

        RAISE INFO 'Pas assez pour acheter, il manque % €', (prix - argent_joueur);
        RETURN NULL;
    END;
$$ LANGUAGE PLPGSQL;


-- Trigger pré-mission
CREATE TRIGGER checkReqMission
    BEFORE INSERTION ON JoueurRealiseMission
    FOR EACH ROW
    EXECUTE PROCEDURE checkReqMission();


CREATE OR REPLACE FUNCTION checkReqMission()
RETURNS TRIGGER
AS $$
    DECLARE 
        idMission INTEGER := new.idMission;
        idJoueur INTEGER := new.idJoueur;
        idVehicule INTEGER := SELECT idVehicule 
                              FROM Mission, MissionNecessiteVehicule 
                              WHERE Mission.idMission = MissionNecessiteVehicule.idMission;

        jouerPossedeV BOOLEAN := (SELECT idVehicule
                                FROM MissionNecessiteVehicule, JoueurPossedeVehicule
                                WHERE MissionNecessiteVehicule.idMission = idMission 
                                AND JoueurPossedeVehicule.idJoueur = idJoueur
                                AND MissionNecessiteVehicule.idVehicule = JoueurPossedeVehicule.idVehicule) != NULL;

        jouerPossedeA BOOLEAN := (SELECT idArme
                                FROM MissionNecessiteArme
                                WHERE MissionNecessiteArme.idMission = idMission)
                                IN
                                (SELECT idArme
                                FROM JoueurPossedeArme
                                WHERE JoueurPossedeArme.idJoueur = idJoueur);
        
        jouerPossedeP BOOLEAN := (SELECT idPropriete
                                FROM MissionNecessitePropriete, JoueurPossedePropriete
                                WHERE MissionNecessitePropriete.idMission = idMission 
                                AND JoueurPossedePropriete.idJoueur = idJoueur
                                AND MissionNecessitePropriete.idPropriete = JoueurPossedePropriete.idPropriete) != NULL;

    BEGIN 
        -- On vérifie que le joueur possède tout ce qui est demandé
        IF (jouerPossedeV AND jouerPossedeA AND jouerPossedeP) THEN RETURN new;
        ENDIF;

        RAISE INFO 'Le joueur ne remplit pas les prérequis';
        RETURN NULL;
    END;
$$ LANGUAGE PLPGSQL;



-- Trigger post-mission
CREATE TRIGGER missionReussie
    AFTER INSERTION ON JoueurRealiseMission
    FOR EACH ROW
    EXECUTE PROCEDURE missionReussie();



CREATE OR REPLACE FUNCTION missionReussie()
RETURNS TRIGGER
AS $$
    DECLARE
        recompArgent INTEGER := (SELECT recompenseArgent
                                 FROM Mission
                                 WHERE Mission.idMission = new.idMission);
        recompXp INTEGER := (SELECT recompenseXP
                             FROM Mission
                             WHERE Mission.idMission = new.idMission);
    BEGIN
        giveArgentJoueur(new.idJoueur, recompArgent);
        giveXpJoueur(new.idJoueur, recompXp);

        -- todo: Mettre à jour les crimes commis par le joueur
    END;
$$ LANGUAGE PLPGSQL;

