# Dictionnaire de données

* Statut
  - [ ] à rédiger
  - [x] en cours de rédaction
  - [ ] relecture
  - [ ] finaliser
  - [ ] révision
  

| Champ | Désignation | Type/Taille | Contrainte | Règle de calcul | Clé étrangère | Commentaire |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| id | Identifiant | serial |  | NOT NULL |  | Identifiant non signifiant |
| code_officiel | Numéro de SIRET ou RNA de la structure | varchar(14) |  |  |  |  |
| type_code_officiel | Type de code (Siret ou RNA) | varchar(5) |  |  |  |  |
| nom | Nom de la structure | varchar(255) |  |  |  |  |
| categorie | Catégorie de la structure | varchar(255) |  |  |  |  |
| typologie | Typologie de la structure | varchar(255) |  |  |  |  |
| adresse | Adresse de la structure | varchar(255) |  |  |  |  |
| code_postal | Code postal de la structure | varchar(5) |  |  |  | Issu de la table de correspondance code postaux - code INSEE |
| numcom | Code INSEE de la structure | varchar(5) |  |  |  | Issu de la table des communes |
| nomcom | Nom de la commune | varchar(255) |  |  |  | Issu de la table des communes |
| url_web | Site internet de la structure | text |  |  |  |  |
| facebook | Page facebook de la structure | text |  |  |  |  |
| twitter | Page twitter de la structure | text |  |  |  |  |
| instagram | Page instagram de la structure | text |  |  |  |  |
| ct_nom | Nom du référent | varchar(150) |  |  |  |  |
| ct_prenom | Prénom du référent | varchar(100) |  |  |  |  |
| ct_courriel | Courriel du référent | varchar(200) |  |  |  |  |
| ct_tel_fixe | Numéro de téléphone fixe du référent | varchar(14) |  |  |  |  |
| ct_tel_mobile | Numéro de téléphone mobile du référent | varchar(14) |  |  |  |  |
| x_wgs84 | Longitude cordonnée géographique (X) en WGS84 | numeric(2,7) |  |  |  |  |
| y_wgs84 | Latitude cordonnée géographique (Y) en WGS84 | numeric(1,9) |  |  |  |  |
| geom | Cordonnée géographique en lambert93 (Point) | geom |  |  |  |  |
| date_sai | Date d'import/saisie de la donnée | datetime |  | NOT NULL | now() |  |
|  |  |  |  |  |  |  |
