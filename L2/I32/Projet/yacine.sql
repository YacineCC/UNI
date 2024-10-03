
INSERT INTO Commanditaire (idCommanditaire, nomCommanditaire, adrCommanditaire) VALUES

	(1,'Lamar Davis','420 Groove Street Hood'),(2,'Lester Crest','4th Weaboo Road'),
	(3,'Walter','308 old Nero Arroyo Lane'),(4,'Simeon','6th Inglewood Corner'),
	(5,'Ron','Sandy Shores'),(6,'Le Z','69th Vespucci Beach'),
	(7,'Le R','7th Quigons Chinalake Hills'),(8,'Le D','Psycho Rigudius Hospital'),
	(9,'Le S','420 AngolaRoad'),(10,'Le V','11th Cyber Road'),
	(11,'LDZ',NULL);
	

INSERT INTO Mission (idMission, intituleMission, typeMission, recompenseArgent, recompenseXP, preRequisPourMission, idCommanditaire) VALUES

	(1, 'Un travail de titan', 'Scénario', 5000, 150, 10,2),
	(2, 'Vidange','Courses', 2500, 100, 0, 1),
	(3, 'Monnaie de sa pièce', 'Vol de voiture', 1500, 100, 10, 4),
	(4, 'Bagarre à mort', 'Combats', 1000, 50, 0, 6),
	(5, 'Légitime saisie', 'Vol de voiture', 7000, 500, 1000, 4),
	(6, 'A toute Berzingue', 'Courses', 5000, 300, 500, 1),
	(7, 'Rammenez la coupe à la maison', 'Scénario', 10000, 750, 1000, 7),
	(8, 'Street Fighter II', 'Combats', 3000, 500, 100, 6),
	(9, 'Oeuvre de charité', 'Vol de voiture', 12000, 1000, 7000, 4),
	(10, 'CT de C', 'Braquage', 50000, 5000, 20000, 8),
	(11, 'Yolo Space Hacker', 'Scénario', 17000, 2000, 10000, 10),
	(12, 'Drone Air Strike', 'Scénario', 15000, 2000, 10000, 9),
	(13, 'Narcos','Scénario', 20000, 3000, 20000, 3),
	(14, 'Amitiés anciennes', 'Scénario', 10000, 5000, 30000, 11),
	(15, 'Passage de frontières', 'Braquage', 100000, 7000, 50000,5),
	(16, 'Sauver Obama', 'Scénario', 40000, 7000, 50000, 7),
	(17, 'Le casse du siècle', 'Braquage', 500000, 15000, 100000, 2),
	(18, 'Ohio', 'Combats', 10000, 10000, 200000, 6); 
	

INSERT INTO Crimes (idCrime, intituleCrime, incDegMechancete) VALUES
	
	(1, 'Meurtre', 100), (2, 'Vol de voiture', 10), (3, 'Braquage', 50),
	(4, 'Vandalisme', 30), (5, 'Conduite dangereuse', 30), (6, 'Prise d otages', 70);
	

INSERT INTO Propriete (idPropriete, typePropriete, adrPropriete, prixPropriete, intitulePropriete) VALUES

	(1, 'Appartement', '1st Sugon avenue' , 500000, 'Eclipse Tower'),
	(2, 'Appartement', '8th Amorg road', 200000, 'Amorbius Building'),
	(3, 'Appartement', '5th Saxton Hale boulevard', 500000,'The australium'),
	(4, 'Maison', '10th Grand Line road', 3000000, 'The one piece'),
	(5, 'Maison', ' 2nd Albuquerque avenue', 1000000, 'The new mexico'),
	(6, 'Maison', '3rd dezo lane', 70000, 'The notzo villa'),
	(7, 'Business', 'Vinewood Boulevard', 500000, 'Imprimerie'),
	(8, 'Business', 'Sandy Shores' , 700000, 'Potager'),
	(9, 'Business', 'Arcadia bay' , 1000000, 'La poste');
	

INSERT INTO Appartement (idPropriete, etageAppart) VALUES
	
	(1, 2), (2, 1), (3, 0);
	

INSERT INTO Maison (idPropriete, aPiscine, AJardin) VALUES

	(4, 'TRUE', 'TRUE'), (5, 'False', 'TRUE'), (6, 'FALSE', 'FALSE');
	

INSERT INTO Business (idPropriete, revenuPassif, typeBusiness) VALUES

	(7, 1000, 'Fabrique faux billets'),
	(8, 5000, 'Fabrique de drogue'),
	(9, 7000, 'entrepot trafic');


