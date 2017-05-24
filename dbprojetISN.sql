BEGIN TRANSACTION;
CREATE TABLE "blog_login" ("id" integer NOT NULL PRIMARY KEY, "nom" varchar(42) NOT NULL, "adresse" varchar(42) NOT NULL, "mail" varchar(42) NOT NULL, "tel" integer NOT NULL, "motdpass" varchar(42) NOT NULL, "pseudo" varchar(42) NOT NULL);
INSERT INTO `blog_login` (id,nom,adresse,mail,tel,motdpass,pseudo) VALUES (1,'amy','any','amy@gmail.com',2324242,'amy','amy'),
 (2,'ancia','Talata','ancia@gmail.com',4754786097,'ancia','ancia'),
 (3,'ancia','Talata','ancia@gmail.com',45272163217,'ancia','ancia'),
 (4,'ancia','Talata','ancia@gmail.com',45272163217,'ancia','ancia'),
 (5,'paul','Larobia','paul@gmail.com',45272163217,'paul','paul'),
 (6,'gerard','Analakely','gerard@gmail.com',23124234235454,'gerard','gerard'),
 (7,'gerard','Analakely','gerard@gmail.com',23124234235454,'gerard','gerard'),
 (8,'rock','Ambohibe','rock@gmail.com',121212,'rock','rock'),
 (9,'lucas','Alasora','lucas@gmail.com',12121,'lucas','lucas'),
 (10,'torre','Amboara','torre@egd.com',12312412,'torre','torre'),
 (11,'gerard','Anjeva','gerard@gmail.com',23124124124,'gerard','gerard'),
 (12,'gerard','Anjeva','gerard@gmail.com',23124124124,'gerard','gerard'),
 (13,'abc','Amboci','abc@gmail.com',122324,'abc','abc'),
 (14,'ancia','Alasora','ancia@gmail.com',345517155,'abc','amy'),
 (15,'ancia','Alasora','ancia@gmail.com',345517155,'abc','amy'),
 (16,'ancia','bloc 34 porte 3','ancia@gmail.com',348517196,'aze','ancia'),
 (17,'allo','Amboci','ancia@egd.com',348517133,'allo','allo'),
 (18,'allo','Amboci','ancia@egd.com',348517133,'allo','allo'),
 (19,'truc','Alasora','ralimanana1809@gmail.com',348517196,'rqVKFhmf&DGtIf:x%LNpy6/l','truc'),
 (20,'taste','Amboci','tanguyvanier@egd.mg',348517122,'5Bx&e~YgAiN-&Vf/otC~D4eC','taste'),
 (21,'user1','Amboara','ralimanan1809@gmail.com',348517222,'1Kwhzd0i~?ge4HF2D!DC3GXu','user1'),
 (22,'user2','Aty','ralimanana1809@gmail.com',348517111,'w&oGEXUcrQxzPi9%BSnj6%HF','user2'),
 (23,'ERRE','bloc 34 porte 3','ancia@gmail.com',348517196,'!b.yHb?eRX6fx-!Pe4:w','FDFD'),
 (24,'gerard','Alasora','tanguy.vanier@leve.egd.mg',348517122,'lG8Q+Qg2yA86pp//4jY0','paul'),
 (25,'gerard','Alasora','tanguy.vanier@eleve.egd.mg',348517122,'U/Ap9/?Xogt5I%:9qsWu','paul1');
CREATE TABLE "blog_document" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "docfile" varchar(100) NOT NULL);
INSERT INTO `blog_document` (id,docfile) VALUES (1,'MaBiblio/4.jpg'),
 (2,'MaBiblio/3.jpg'),
 (3,'MaBiblio/5.jpg'),
 (4,'MaBiblio/0.jpg'),
 (5,'MaBiblio/1.jpg'),
 (6,'MaBiblio/IMG_2203.JPG'),
 (7,'MaBiblio/2.jpg'),
 (8,'MaBiblio/2_cA17URf.jpg'),
 (9,'MaBiblio/0_SHYDvY7.jpg'),
 (10,'MaBiblio/3_OcSCqNH.jpg'),
 (11,'MaBiblio/3_cgoMsrq.jpg'),
 (12,'MaBiblio/IMG_2224.JPG'),
 (13,'MaBiblio/IMG_2224_1hRTmT0.JPG'),
 (14,'MaBiblio/IMG_2224_BkIk6G4.JPG'),
 (15,'MaBiblio/IMG_2224_bkrqTuL.JPG'),
 (16,'MaBiblio/IMG_2225.JPG'),
 (17,'MaBiblio/IMG_2225_Ocup4pV.JPG'),
 (18,'MaBiblio/IMG_2225_mytgeOI.JPG'),
 (19,'MaBiblio/IMG_2224_Celq1Ec.JPG'),
 (20,'MaBiblio/IMG_2224_98Medtw.JPG'),
 (21,'MaBiblio/IMG_2224_Tz3OKeP.JPG'),
 (22,'MaBiblio/IMG_2224_BmCzYJq.JPG'),
 (23,'MaBiblio/IMG_2224_OB6KXv3.JPG'),
 (24,'MaBiblio/IMG_2224_qa5LikZ.JPG'),
 (25,'MaBiblio/IMG_2224.JPG');
CREATE TABLE "blog_article" ("id" integer NOT NULL PRIMARY KEY, "libelle" varchar(100) NOT NULL, "categorie" varchar(42) NOT NULL, "marque" varchar(42) NOT NULL, "couleur" varchar(42) NOT NULL, "etat" varchar(42) NOT NULL, "prix" integer NOT NULL, "description" text NULL, "date" datetime NOT NULL, "docfile" varchar(100) NOT NULL, "user_id" integer NOT NULL);
INSERT INTO `blog_article` (id,libelle,categorie,marque,couleur,etat,prix,description,date,docfile,user_id) VALUES (1,'ordi portable','ordinateur','acer','gris','neuf',1000,'blabla bla bla','2017-05-07 06:09:42.265815','Images/0.jpg',1),
 (2,'samsung android TC-X','téléphone','samsung','noir','neuf',100,'dsfezf blabla bla bla','2017-05-07 06:32:19.910196','Images/0.jpg',1),
 (6,'robe noire','9','channel','noir','5',1234,'classe et sexy','2017-05-12 09:26:22.081966','Images/0.jpg',1),
 (7,'portable samsung dual core','5','samsung','gris','5',2000,'bd fsd dfsd','2017-05-12 10:38:37.068953','Images/IMG_2232.JPG',1),
 (8,'portable samsung dual core','5','samsung','gris','5',2000,'bd fsd dfsd','2017-05-12 10:48:15.553636','Images/IMG_2232_bqP6w6k.JPG',1),
 (9,'téléphone portable','5','sony','noir','5',1223,'connexion 3G','2017-05-14 07:06:18.732914','Images/IMG_2232_5KloEkT.JPG',1),
 (10,'portable samsung dual core','5','samsung','gris','5',2000,'bd fsd dfsd','2017-05-14 07:51:34.998117','Images/IMG_2232_t9riGFW.JPG',1),
 (11,'rice cooker','Electroménager','vista','blanc','5',500,'efficace','2017-05-15 05:58:22.621865','Images/IMG_2227.JPG',1),
 (12,'robe bleue','Vêtement','channel','bleue','6',2424,'tsara tarehy','2017-05-19 18:52:17.642305','Images/IMG_2233.JPG',5),
 (13,'montre','Electroménager','dior','métal','8',19,'glamour','2017-05-21 05:23:18.234155','Images/IMG_2233_713Zrtk.JPG',21);
CREATE INDEX "django_session_de54fa62" ON "django_session" ("expire_date");
CREATE UNIQUE INDEX "django_content_type_app_label_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE INDEX "django_admin_log_e8701ad4" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_417f1b1c" ON "django_admin_log" ("content_type_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_e8701ad4" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_8373b171" ON "auth_user_user_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_e8701ad4" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_0e939a4f" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_417f1b1c" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_8373b171" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_group_permissions_0e939a4f" ON "auth_group_permissions" ("group_id");
COMMIT;
