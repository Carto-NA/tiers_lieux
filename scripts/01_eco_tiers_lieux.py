#-------------------------------------------------------------------------------
# Name:        01_eco_tiers_lieux
# Purpose:     Script qui permet de créer la structure dans la geodatabase ESRI
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

#---------------------------------#
# On définit les variables

## Creating a spatial reference object
spatial_ref = arcpy.SpatialReference(2154)
spatial_ref_4326 = arcpy.SpatialReference(4326)
txt_ref_4326 = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision'

# Spatial reference set to GCS_WGS_1984
#spatial_reference = arcpy.SpatialReference(4326)

# Table a utiliser
nomFC = "eco_tiers_lieux"

# On définit le chemin et le nom d'entité
fc = os.path.join(arcpy.env.workspace, nomFC)

################################################################################
## Création de la structure
################################################################################

###########################################
##Process: Création de la classe d entite

# On définit les variables
geometry_type = "POINT"
template = ""
has_m = "DISABLED"
has_z = "DISABLED"

# Création de la classe d entite
if arcpy.Exists("/economie" + nomFC):
  print "{} existe dans la geodatabase".format(nomFC)
else:
  # On creer la classe d entite
  arcpy.CreateFeatureclass_management(arcpy.env.workspace+"/economie", nomFC, geometry_type, template, has_m, has_z, spatial_ref)

  # Ajout des champs
  arcpy.AddField_management (nomFC, "nom", "TEXT", field_length=255, field_alias="Nom")
  arcpy.AddField_management (nomFC, "typologie", "TEXT", field_length=500, field_alias="Typologie")
  arcpy.AddField_management (nomFC, "service_annexe", "TEXT", field_length=9000, field_alias="Service annexe")
  arcpy.AddField_management (nomFC, "engagement_ecolo", "TEXT", field_length=3, field_alias="Engagement écolo")
  arcpy.AddField_management (nomFC, "acces_fibre", "TEXT", field_length=255, field_alias="Accès fibre")
  arcpy.AddField_management (nomFC, "acces_pmr", "TEXT", field_length=255, field_alias="Accès PMR")
  arcpy.AddField_management (nomFC, "mode_gestion", "TEXT", field_length=255, field_alias="Mode de gestion")
  arcpy.AddField_management (nomFC, "num_rue", "TEXT", field_length=50, field_alias="N° rue")
  arcpy.AddField_management (nomFC, "rue", "TEXT", field_length=255, field_alias="Rue")
  arcpy.AddField_management (nomFC, "code_postal", "TEXT", field_length=5, field_alias="Code postal")
  arcpy.AddField_management (nomFC, "Commune", "TEXT", field_length=150, field_alias="Commune")
  arcpy.AddField_management (nomFC, "pers_referente", "TEXT", field_length=255, field_alias="Personne référente")
  arcpy.AddField_management (nomFC, "telephone", "TEXT", field_length=17, field_alias="Téléphone")
  arcpy.AddField_management (nomFC, "courriel", "TEXT", field_length=255, field_alias="Courriel")
  arcpy.AddField_management (nomFC, "url_web", "TEXT", field_length=255, field_alias="Site internet")
  arcpy.AddField_management (nomFC, "facebook", "TEXT", field_length=255, field_alias="Facebook")
  arcpy.AddField_management (nomFC, "autre_res_social", "TEXT", field_length=255, field_alias="Autre réseau social")
  arcpy.AddField_management (nomFC, "affichage_carto", "TEXT", field_length=3, field_alias="Afficher sur la carte")
  arcpy.AddField_management (nomFC, "date_sai", "DATE")
  arcpy.AddField_management (nomFC, "date_maj", "DATE", field_alias="Date de mise à jour")
  arcpy.AddField_management (nomFC, "geometrie_pertinence", "TEXT", field_length=50, field_alias="Pertinence géométrie")
  arcpy.AddField_management (nomFC, "geometrie_type", "TEXT", field_length=100, field_alias="Source géometrie")
  
  ###########################################
  # Process: On affecte le domaine à un champ

  # Champ concerné par la liste de domaine
  tblField = "geometrie_pertinence"
  domaineName = "geometrie_pertinence"
  # On définit le chemin et le nom d'entité
  arcpy.AssignDomainToField_management(nomFC, tblField, domaineName)

  # Champ concerné par la liste de domaine
  tblField = "affichage_carto"
  domaineName = "lt_oui_non"
  # On définit le chemin et le nom d'entité
  arcpy.AssignDomainToField_management(nomFC, tblField, domaineName)
  
  # Champ concerné par la liste de domaine
  tblField = "geometrie_type"
  domaineName = "geometrie_type"
  # On définit le chemin et le nom d'entité
  arcpy.AssignDomainToField_management(nomTbl, tblField, domaineName)
