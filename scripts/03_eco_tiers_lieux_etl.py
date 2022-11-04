#-------------------------------------------------------------------------------
# Name:        03_eco_tiers_lieux_etl
# Purpose:     Script qui permet d'integrer les données dans la geodatabase ESRI
#
# Author:      vincentto
#
# Created:     04/11/2022
# Copyright:   (c) vincentto 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf-8

#---------------------------------#
# Import des librairies

import arcpy, datetime, os, pandas as pd, numpy as np
from arcpy import env

#---------------------------------#
# On définit l'espace de travail

# On demande de saisir l'environnement de travail (prod ou preprod)
environnement_travail = input("Saisir l'environnement de travail (prod ou preprod): ")

# On test et on déclare la variable
if environnement_travail == "preprod":
    conn = "conn_preprod/preprod_metier.sde"
elif environnement_travail == "prod":
    conn = "conn_prod/prod_metier.sde"
    
# Dossier du projet
projet = r"Modele_AdminDonnees/"

# Espace de travail
arcpy.env.workspace = r"i:/ArcGIS/Projects/" + projet + conn

################################################################################
## ETL - Données "tiers-lieux"
################################################################################

#####################################################
##Process: Création d'une classe d'entité de point à partir de XY
path_fileCSV = r"C:\tmp_jupyterNotebook\prj_tiers_lieux\api_gogocarto_tiers_lieux.csv"
colonne_x = "longitude"
colonne_y = "latitude"
#colonne_z = None

arcpy.management.XYTableToPoint(
    path_file, 
    r"\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_XYTableToPoint",
    colonne_x, 
    colonne_y, 
    None, 
    'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision'
)

#####################################################
##Process: On vide une table/classe d'entité

#
arcpy.TruncateTable_management(nomFC)

#####################################################
##Process: Ajout des données

#
arcpy.management.Append(
    r"'\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint'", 
    r"\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\conn_prod\prod_metier.sde\arcgis.metier.economie\arcgis.metier.eco_tiers_lieux", 
    "NO_TEST", 
    r'nom "Nom" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,nom,0,8000;typologie "Typologie" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,typologie,0,8000;service_annexe "Service annexe" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Services_annexes,0,8000;engagement_ecolo "Engagement écolo" true true false 3 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Engagement_écolo,0,8000;acces_fibre "Accès fibre" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Accès_fibre,0,8000;acces_pmr "Accès PMR" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Accès_PMR,0,8000;mode_gestion "Mode de gestion" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Mode_de_gestion,0,8000;num_rue "N° rue" true true false 50 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,N_,0,8000;rue "Rue" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,rue,0,8000;code_postal "Code postal" true true false 5 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,cp,-1,-1;commune "Commune" true true false 150 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Commune,0,8000;pers_referente "Personne référente" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Personne_référente,0,8000;telephone "Téléphone" true true false 17 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Tél,0,8000;courriel "Courriel" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Mail,0,8000;url_web "Site internet" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Web,0,8000;facebook "Facebook" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Facebook,0,8000;autre_res_social "Autre réseau social" true true false 255 Text 0 0,First,#,\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_mai2022_tony_XYTableToPoint,Autre_réseau_social,0,8000',
    '', 
    ''
)

#####################################################
##Process: Supprimer une table

# Suppression de la table temporaire
arcpy.Delete_management(r"\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\gdb_tiers_lieux.gdb\BDD_Tierslieux_XYTableToPoint")



################################################################################
## ETL - Données "tiers-lieux temps d'accès"
################################################################################

#####################################################
##Process: Copier une classe d'entité vers une classe d'entité

# Import de la classe d'entité de pre-pro à prod
arcpy.conversion.FeatureClassToFeatureClass(
    "arcgis.metier.eco_tiers_lieux_tps_acces", 
    r"\\fileruser2\Users\vincentto\Mes documents\ArcGIS\Projects\Modele_AdminDonnees\conn_prod\prod_metier.sde\arcgis.metier.economie", 
    "eco_tiers_lieux_tps_acces", 
    '', 
    'facilityid "FacilityID" true true false 4 Long 0 10,First,#,arcgis.metier.eco_tiers_lieux_tps_acces,facilityid,-1,-1;name "Name" true true false 254 Text 0 0,First,#,arcgis.metier.eco_tiers_lieux_tps_acces,name,0,254;frombreak "FromBreak" true true false 8 Double 8 38,First,#,arcgis.metier.eco_tiers_lieux_tps_acces,frombreak,-1,-1;tobreak "ToBreak" true true false 8 Double 8 38,First,#,arcgis.metier.eco_tiers_lieux_tps_acces,tobreak,-1,-1;st_area(shape) "st_area(shape)" false false true 0 Double 0 0,First,#,arcgis.metier.eco_tiers_lieux_tps_acces,st_area(shape),-1,-1;st_length(shape) "st_length(shape)" false false true 0 Double 0 0,First,#,arcgis.metier.eco_tiers_lieux_tps_acces,st_length(shape),-1,-1',
    ''
)
