DROP DATABASE pronotes;
CREATE DATABASE pronotes DEFAULT CHARACTER SET UTF8 COLLATE utf8_bin;
show DATABASES;
CREATE TABLE Profs (
    NumP int auto_increment NOT NULL,
    NomP Varchar(255),
    PrenomP Varchar(255),
    PRIMARY KEY (NumP),
);
CREATE TABLE Trimestres(
    NumT int auto_increment,
    LibelleTrimestre Varchar(255),
    PRIMARY KEY (NumT),
);

CREATE TABLE Matieres(
    CodeM int auto_increment NOT NULL,
    LibelleMat Varchar(255),
    CoefMatiere  Varchar(255),
    PRIMARY KEY (CodeM),
);
CREATE TABLE Classes(
    codeC int auto_increment NOT NULL,
    NomClasse Varchar( 255),
    PRIMARY KEY (CodeC),
);
CREATE TABLE Eleves(
    NumE int auto_increment NOT NULL,
    Nom Varchar (255),
    Prenom Varchar (255),
    Adresse Varchar (255),
    CodePostal Varchar (255),
    Ville Varchar (255),
    Sexe Varchar (255),
    DateNaissance Varchar (255),
    PRIMARY KEY (NumE), 
);
CREATE TABLE Devoirs(
    NumD int auto_increment NOT NULL,
    NomDevoirs Varchar (255),
    DateDevoirs Varchar (255),
    TotalPoints Varchar (255),
    CoefDevoirs Varchar (255),
    PRIMARY KEY (NumD),
);
CREATE TABLE Avoir (
    
);
INSERT INTO
