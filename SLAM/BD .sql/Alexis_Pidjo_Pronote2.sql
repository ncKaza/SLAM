
INSERT INTO Classes (CodeC, NomClasse)
VALUES ("sio1","BTS Service Informatique aux Organisations 1");
VALUES ("sio1","BTS Service Informatique aux Organisations 2");
VALUES ("TSTMG5","TERMINALE Sciences et Technologies du Management et de la Gestion");

INSERT INTO Eleves (Nom , prenom, CodeClasse)
VALUES ("PIDJO","Alexis", "sio1");
VALUES ("PULEOTO","Noah", "sio1");
VALUES ("DEBRAILLES","Josias", "sio1");

INSERT INTO Profs (NomP , prenomP)
VALUES ("STROZZI","Alexa" );
VALUES ("RABIER","Benjamin" );
VALUES ("LEROUX","Valentin");

INSERT INTO Matieres (LibelleMat, CoefMatiere)
VALUES ("Mathématiques pour l'informatique","3" );
VALUES ("Culture économique, juridique et managériale pour l'informatique","3" );
VALUES ("Culture générale et expression","2" );

INSERT INTO Trimestres (LibelleTrimestre)
VALUES ("Trimestre1");
VALUES ("Trimestre2");
VALUES ("Trimestre3"); 

INSERT INTO Devoirs(NomDevoirs,DateDevoirs, TotalPoints, CoefDevoirs)
VALUES ("Devoirs de Mathematique","15/4" , "20" , "1")
VALUES ("Devoirs de Anglais", "14/5" , "15" , "1")
VALUES ("Devoirs de Français","20/4" , "20" , "2")




INSERT INTO ELEVES (Nom , prenom, CodeClasse)
VALUES ("DUNON","Gael", "TSTMG5");
VALUES ("POREMPOEA","Sicera", "TSTMG5");
VALUES ("MASEI","Oran", "TSTMG5");
