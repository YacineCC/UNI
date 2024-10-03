DROP TABLE IF EXISTS Employe;
DROP TABLE IF EXISTS Departement;


CREATE TABLE Departement(
   DID char(2), PRIMARY KEY(DID),
   Libelle varchar(20)
   );

CREATE TABLE Employe(
        EID integer, PRIMARY KEY(EID),
        Nom varchar(20),
        DID char(2),
        CONSTRAINT fk_dept
            FOREIGN KEY(DID)
                REFERENCES Departement(DID)
        );




