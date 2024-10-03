DROP TABLE IF EXISTS Reservation;
DROP TABLE IF EXISTS Client;
DROP TABLE IF EXISTS Spectacle;

CREATE TABLE Spectacle
	(nomS VARCHAR(15) NOT NULL PRIMARY KEY,
	Nbplaces INTEGER NOT NULL,
	NbplacesLibres INTEGER NOT NULL,
	tarif DECIMAL(10,2) NOT NULL
	);

CREATE TABLE Client
	(nomC VARCHAR(10) NOT NULL PRIMARY KEY,
	Solde integer NOT NULL
	);

CREATE TABLE Reservation
	(nomC VARCHAR(10) NOT NULL references Client,
	nomS VARCHAR(15) NOT NULL references Spectacle,
	NbplacesReservees INT NOT NULL,
	PRIMARY KEY (nomC, nomS)
	);




DELETE FROM Reservation;
DELETE FROM Client;
DELETE FROM Spectacle;

INSERT INTO Client VALUES ('Quentin', 50);
INSERT INTO Client VALUES ('Neven', 50);
INSERT INTO Spectacle VALUES ('Happy Potter', 250, 250, 20);

