Les tiers-lieux
====

Contenu de la base de données :

Cette base de données a été constituée par la coopérative des Tiers-lieux en partenariat avec le service **Délégation Numérique** de la région Nouvelle-Aquitaine.

Elle contient à l’heure actuelle **200** tiers lieux et vise pour chaque tiers lieu à informer sur :
* la localisation (adresse, géolocalisation…)
* le contact
* le type de tiers-lieu
* la catégorie du tiers-lieu
* le site internet
* les réseaux sociaux


Provenance des données :
La Coopérative Tiers-Lieux en Nouvelle-Aquitaine

Thème :
* Économie
* Emploi
* Innovation

Mots-clés :
Coworking, Emploi, Polarité, Tiers-Lieux, Zone d'emploi


Dictionnaire de données
| Champ | Désignation | Type/Taille | Contrainte | Règle de calcul | Clé étrangère | Commentaire |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| id | Identifiant | serial |  | NOT NULL |  | Identifiant non signifiant |
| siret | Numéro de SIRET de la structure | varchar(14) |  |  |  |  |
| str_nom | Nom de la structure | varchar(255) |  |  |  |  |
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
| ct_courriel | Courriel du référent |  |  |  |  |  |
| ct_tel_fixe | Numéro de téléphone fixe du référent |  |  |  |  |  |
| ct_tel_mobile | Numéro de téléphone mobile du référent |  |  |  |  |  |
| x_wgs84 | Longitude cordonnée géographique (X) en WGS84 | numeric(2,7) |  |  |  |  |
| y_wgs84 | Latitude cordonnée géographique (Y) en WGS84 | numeric(1,9) |  |  |  |  |
| geom | Cordonnée géographique en lambert93 (Point) | geom |  |  |  |  |
| date_sai | Date d'import/saisie de la donnée | datetime |  | NOT NULL | now() |  |
|  |  |  |  |  |  |  |
 
 

Liste de valeurs :

Categorie :

| Libellé | Libellé long |
| :--: | :--: |
| NR | Non renseigné |
| Association | Association |
| SARL | Société à responsabilité limitée |
| SAS + Association | SAS + Association |
| GIP | Groupement d'intérêt public |
| EURL | Entreprise unipersonnelle à responsabilité limitée |
| SAS | société par actions simplifiée |
| SCI | Société civil immobilière |
| Université | Université |
| SA | Société anonyme |
| Association / SARL | Association / SARL |
| Association / collectivité | Association / collectivité |
| Association / université | Association / université |
| SCIC + Association | SCIC + Association |
| SPL | Société publique locale |
| EI | Entreprise individuel |


Typologie :

| Libellé | Libellé long |
| :--: | :--: |
| NR | Non renseigné |
| Coworking | Coworking |
| Fablab | Fablab |
| Coworking et fablab | Coworking et fablab |
| Atelier partagé | Atelier partagé |
| Fablab et atelier partagé | Fablab et atelier partagé |
| Coworking et atelier partagé | Coworking et atelier partagé |
| Coworking, fablab et atelier partagé | Coworking, fablab et atelier partagé |
| Fablab et atelier partagé | Fablab et atelier partagé |
| Hybride | Hybride |
| Terres agricoles |Terres agricoles |


## Réutilisation
Ce jeu de données est publiée par la région Nouvelle-Aquitaine et la Coppérative Tiers-lieux via la plateforme PIGMA. Il est diffusé sous licence Ouverte 2.0 (voir le fichier LICENCE.md).


## Mises à jour
Les mises à jour sont effectuées à partir du fichier communiqué par la Coopérative des tiers lieux précédemment et en reprennent, en les modifiant le cas échéant, les données qui y figurent déjà.

## En savoir plus
*La coopérative des tiers-lieux (https://coop.tierslieux.net/)
*Les aides Nouvelle-Aquitaine (https://les-aides.nouvelle-aquitaine.fr/amenagement-du-territoire/tiers-lieux-2019-2021)
