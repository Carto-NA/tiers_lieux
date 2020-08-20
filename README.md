Les tiers-lieux
====

Contenu de la base de données :
Cette base de données a été constituée par la coopérative des Tiers-lieux en partenariat avec le service **Délégation Numérique** de la région Nouvelle-Aquitaine.

Elle contient à l’heure actuelle **200** tiers lieux et vise pour chaque tiers lieu à informer sur :
* la localisation (adresse, géolocalisation…) ;
* le site internet ;
* la page facebook ;
* le twitter ;

des compléments d’informations sur la situation géographique : dans une métropole ? dans quelle zone d’emploi et quelles caractéristiques pour la zone d’emploi ?
L’objectif de la publication de cette base de données est de permettre sa libre réutilisation mais également son amélioration afin d’avoir une vision nationale plus claire et plus fine des tiers lieux en France.

Si vous souhaitez avoir plus d’informations sur la base de données ou sur la Mission Coworking, contactez : remy.seillier@cget.gouv.fr


Provenance des données :
La Coopérative Tiers-Lieux en Nouvelle-Aquitaine

Thème :
* Économie
* Emploi
* Innovation

Mots-clés :
Coworking, Emploi, Polarité, Tiers-Lieux, Zone d'emploi


Dictionnaire de données
| Champ | Désignation | Type | Taille | Contrainte | Règle de calcul | Clé étrangère | Commentaire |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| id | Identifiant non signifiant | Type | Taille | Contrainte | Règle de calcul | Clé étrangère | Commentaire |
| siret | Numéro de SIRET de la structure |  |  |  |  |  |  |
| nom | Nom de la structure |  |  |  |  |  |  |
| categorie | Catégorie de la structure |  |  |  |  |  |  |
| typologie | Typologie de la structure |  |  |  |  |  |  |
| adresse | Adresse de la structure |  |  |  |  |  |  |
| code_postal | Code postal de la structure |  |  |  |  |  |  |
| numcom | Code INSEE de la structure |  |  |  |  |  |  |
| nomcom | Nom de la commune |  |  |  |  |  |  |
| url_web | Site internet de la structure |  |  |  |  |  |  |
| facebook | Page facebook de la structure |  |  |  |  |  |  |
| twitter | Page twitter de la structure |  |  |  |  |  |  |
| instagram | Page instagram de la structure |  |  |  |  |  |  |
| referent_nom | Nom du référent |  |  |  |  |  |  |
| refernet_prenom | Prénom du référent |  |  |  |  |  |  |
| referent_courriel | Courriel du référent |  |  |  |  |  |  |
| referent_tel | Numéro de téléphone du référent |  |  |  |  |  |  |
| x_wgs84 |  |  |  |  |  |  |  |
| y_wgs84 |  |  |  |  |  |  |  |
| geom | Cordonnée géographique en lambert93 (Point) | geom |  |  |  |  |  |
| date_sai | Date d'import/saisie de la donnée | datetime |  | NOT NULL | now() |  |  |
|  |  |  |  |  |  |  |  |
 
 



## Réutilisation
Ce jeu de données est publiée par la région Nouvelle-Aquitaine et la Coppérative Tiers-lieux via la plateforme PIGMA. Il est diffusé sous licence Ouverte 2.0 (voir le fichier LICENCE.md).


## Mises à jour
Les mises à jour sont effectuées à partir du fichier communiqué par la Coopérative des tiers lieux précédemment et en reprennent, en les modifiant le cas échéant, les données qui y figurent déjà.

## En savoir plus
*La coopérative des tiers-lieux (https://coop.tierslieux.net/)
*Les aides Nouvelle-Aquitaine (https://les-aides.nouvelle-aquitaine.fr/amenagement-du-territoire/tiers-lieux-2019-2021)
