--
-- Insertion des données dans les tables qui n'ont pas de clés 
-- étrangères
--

--
-- Insertion des données dans les tables `Matieres` et 'Classes'
-- Dans ce cas, on N'est PAS obligé d'écrire le nom des champs
-- car on va tous les renseigner dans le VALUES
--
INSERT INTO Matieres
VALUES ('INFO', 'Informatique', 12);

INSERT INTO Matieres
VALUES ('ECO-DROIT', 'Economie-Droit', 5);

INSERT INTO Matieres
VALUES ('MATH', 'Mathematique', 1);

-- On peut aussi saisir plusieurs enregistrements avec une seule requête
INSERT INTO Classes
VALUES ('SIO1', 'BTS Service Informatique et aux Organisations 1'),
    ('TRH1', 'Terminale STMG Spécialité Ressources Humaines 1'),
    ('TSIG', 'Terminale STMG Spécialité Informatique');

--
-- Insertion des données dans les tables `Profs`, 'Trimestres'
-- Dans ce cas, on EST obligé d'écrire le nom des champs
-- car on ne va pas tous les renseigner dans le VALUES
-- car la clé primaire est un AUTO_INCREMENT
--
INSERT INTO Profs (NomP, PrenomP)
VALUES ('STROZZI', 'Alexa');

INSERT INTO Profs (NomP, PrenomP)
VALUES ('LEVY', 'SYLVIE');

INSERT INTO Profs (NomP, PrenomP)
VALUES ('LEROUX', 'Valentin');

-- On n'est pas obligé de mettre tous les champs 
INSERT INTO Profs (NomP)
VALUES ('TESSIER');

-- On peut aussi saisir plusieurs enregistrements avec une seule requête
INSERT INTO Trimestres (LibelleTrimestre)
VALUES ('Trimestre 1'),
    ('Trimestre 2'),
    ('Trimestre 3');


-- 
-- Insertion des données dans les tables qui ont des clés étrangères 
-- faisant références à des clés primaires dont les valeurs existent
-- 

INSERT INTO Eleves (Nom, Prenom, Adresse, CodePostal, Ville, CodeClasse, Sexe, DateNaissance)
VALUES ('AHBIBI', 'Sami', '110 rue des fleurs', '84000', 'Avignon', 'TSIG', 'G', '2001-04-13');

INSERT INTO Eleves (Nom, Prenom, Adresse, CodePostal, Ville, CodeClasse, Sexe, DateNaissance)
VALUES ('ZARQANE', 'Nordine', '14 rue carre', '84140', 'Montfavet', 'TSIG', 'G', '2001-02-01');

INSERT INTO Eleves (Nom, Prenom, Adresse, CodePostal, Ville, CodeClasse, Sexe, DateNaissance)
VALUES ('BENALI', 'Myriam', '5 bis chemin du fer a cheval', '84000', 'Avignon', 'TRH1', 'F', '2001-05-15');

INSERT INTO Eleves (Nom, Prenom, Adresse, CodePostal, Ville, CodeClasse, Sexe, DateNaissance)
VALUES ('LOGEZ', 'Louis', '10 rue de la baie', '98800', 'Nouméa', 'SIO1', 'M', '2007-05-22');

INSERT INTO Devoirs (NomDevoir, DateDevoir, TotalPoints, CoefDevoir, NumTrimestre, NumProf, CodeMatiere, CodeClasse)
VALUES ('DS7', '2021-03-15', 18, 1, 2, 1, 'INFO', 'SIO1');

INSERT INTO Devoirs (NomDevoir, DateDevoir, TotalPoints, CoefDevoir, NumTrimestre, NumProf, CodeMatiere, CodeClasse)
VALUES ('DS8', '2021-02-10', 32, 1, 2, 1, 'INFO', 'SIO1');

INSERT INTO Devoirs (NomDevoir, DateDevoir, TotalPoints, CoefDevoir, NumTrimestre, NumProf, CodeMatiere, CodeClasse)
VALUES ('CT3', '2021-02-10', 20, 2, 1, 3, 'MATH', 'TSIG');

-- 
-- Insertion des données dans les dernières tables
--
INSERT INTO AvoirNotes
VALUES (1, 1, 10);

INSERT INTO AvoirNotes
VALUES (2, 1, 12);

INSERT INTO AvoirNotes
VALUES (1, 2, 15);

INSERT INTO AvoirNotes
VALUES (2, 2, 17);

INSERT INTO AvoirNotes
VALUES (1, 3, 6);

INSERT INTO AvoirNotes
VALUES (2, 3, 8.5);

--
-- Regarder le contenu de toutes les table APRES avoir
-- inséré toutes les données
--
SELECT * FROM Trimestres;
SELECT * FROM Profs;
SELECT * FROM Matieres;
SELECT * FROM Classes;
SELECT * FROM Eleves;
SELECT * FROM Devoirs;
SELECT * FROM AvoirNotes;
--Exercice 1
SELECT * FROM Profs;

--Exercice 2
SELECT Nom,Prenom FROM Eleves;

--Exercice 3
SELECT Nom,Prenom,Sexe,DateNaissance
FROM Eleves
WHERE CodeClasse = "TSIG"
