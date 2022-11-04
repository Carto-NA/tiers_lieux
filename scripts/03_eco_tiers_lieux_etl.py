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
