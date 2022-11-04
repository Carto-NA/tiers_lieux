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

