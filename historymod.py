from enum import Enum
import re
from typing import List
import torch
import string
import statistics
import pickle
from medspacy.sentence_splitting import PyRuSHSentencizer
import medspacy
from medspacy.preprocess import PreprocessingRule, Preprocessor
from medspacy.ner import TargetRule
from medspacy.context import ConTextRule
from medspacy.section_detection import Sectionizer
from medspacy.postprocess import PostprocessingRule, PostprocessingPattern, Postprocessor
from medspacy.postprocess import postprocessing_functions
from medspacy.visualization import visualize_ent, visualize_dep
from medspacy.ner import TargetRule
from medspacy.visualization import visualize_ent
from medspacy.section_detection import SectionRule
import spacy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import dill as pickle
from string import digits
import json

op = pd.DataFrame(docop._.context_graph.edges)
pp = pd.DataFrame(doc._.context_graph.edges)
if len(pp) > 0:
  pp.columns=['column1', 'column2']
  pp['column1'] = pp['column1'].astype(str)
  pp['column2'] = pp['column2'].astype(str)
  selected_rowshist = pp.loc[pp['column2'].str.contains("HISTORICAL")]
  selected_rowshist['column1'] = selected_rowshist['column1'].astype(str)
  hist = list(selected_rowshist['column1'])
  selected_rowsneg = pp.loc[pp['column2'].str.contains("ACTIVE")]
  selected_rowsneg['column1'] = selected_rowsneg['column1'].astype(str)
  act = list(selected_rowshist['column1'])
  #hist



  flag=0
  for i in hist:
      for j in Abdominal_Pain:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistAbdominal_Pain = 1
  else:
      yhistAbdominal_Pain = 0


  flag=0
  for i in hist:
      for j in Cellulitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistcellulitis = 1
  else:
      yhistcellulitis = 0


  flag=0
  for i in hist:
      for j in Burns:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistburn = 1
  else:
      yhistburn = 0

  flag=0
  for i in hist:
      for j in Afib:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistAfib = 1
  else:
      yhistAfib = 0



  flag=0
  for i in hist:
      for j in DM:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistDiabetes = 1
  else:
      yhistDiabetes = 0

  flag=0
  for i in hist:
      for j in ACS:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistACS = 1
  else:
      yhistACS = 0

  flag=0
  for i in hist:
      for j in AAA:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistAAA = 1
  else:
      yhistAAA = 0

  flag=0
  for i in hist:
      for j in Tachycardia:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistTachycardia = 1
  else:
      yhistTachycardia = 0

  flag=0
  for i in hist:
      for j in Bradycardia:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistBradycardia = 1
  else:
      yhistBradycardia = 0

  flag=0
  for i in hist:
      for j in CHF:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistCHF = 1
  else:
      yhistCHF = 0

  flag=0
  for i in hist:
      for j in HTN_Emergency:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistHTN_Emergency = 1
  else:
      yhistHTN_Emergency = 0

  flag=0
  for i in hist:
      for j in HypotensionShock:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistHypotensionShock = 1
  else:
      yhistHypotensionShock = 0

  flag=0
  for i in hist:
      for j in Cardiac_arrest:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistCardiac_arrest = 1
  else:
      yhistCardiac_arrest = 0

  flag=0
  for i in hist:
      for j in Airway_Obstruction:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistAirway_Obstruction = 1
  else:
      yhistAirway_Obstruction = 0

  flag=0
  for i in hist:
      for j in Pneumonia:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistPneumonia = 1
  else:
      yhistPneumonia = 0

  flag=0
  for i in hist:
      for j in COPD:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistCOPD = 1
  else:
      yhistCOPD = 0

  flag=0
  for i in hist:
      for j in Pneumothorax:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistPneumothorax = 1
  else:
      yhistPneumothorax = 0

  flag=0
  for i in hist:
      for j in Respiratory_Failure:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistRespiratory_Failure = 1
  else:
      yhistRespiratory_Failure = 0

  flag=0
  for i in hist:
      for j in GI_Bleed:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistGI_Bleed = 1
  else:
      yhistGI_Bleed = 0

  flag=0
  for i in hist:
      for j in ALF:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistALF = 1
  else:
      yhistALF = 0

  flag=0
  for i in hist:
      for j in Pancreatitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistPancreatitis = 1
  else:
      yhistPancreatitis = 0

  flag=0
  for i in hist:
      for j in Colitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistColitis = 1
  else:
      yhistColitis = 0

  flag=0
  for i in hist:
      for j in Gastroenteritis:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistGastroenteritis = 1
  else:
      yhistGastroenteritis = 0

  flag=0
  for i in hist:
      for j in Meningitis_encephalitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistmeningitis_encephalitis = 1
  else:
      yhistmeningitis_encephalitis = 0

  flag=0
  for i in hist:
      for j in Bacteremia:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistBacteremia = 1
  else:
      yhistBacteremia = 0

  flag=0
  for i in hist:
      for j in Endocarditis:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistEndocarditis = 1
  else:
      yhistEndocarditis = 0

  flag=0
  for i in hist:
      for j in UTI:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistUTI = 1
  else:
      yhistUTI = 0

  flag=0
  for i in hist:
      for j in Vented:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistvented = 1
  else:
      yhistvented = 0

  flag=0
  for i in hist:
      for j in Afib:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistafib = 1
  else:
      yhistafib = 0

  flag=0
  for i in hist:
      for j in DM:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistDM = 1
  else:
      yhistDM = 0

  flag=0
  for i in hist:
      for j in DKA:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistDKA = 1
  else:
      yhistDKA = 0

  flag=0
  for i in hist:
      for j in PE:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistPE = 1
  else:
      yhistPE = 0

  flag=0
  for i in hist:
      for j in ICH:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistICH = 1
  else:
      yhistICH = 0

  flag=0
  for i in hist:
      for j in SDH:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistSDH = 1
  else:
      yhistSDH = 0

  flag=0
  for i in hist:
      for j in SAH:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistSAH = 1
  else:
      yhistSAH = 0

  flag=0
  for i in hist:
      for j in Seizures:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistSeizure = 1
  else:    yhistSeizure = 0

  flag=0
  for i in hist:
      for j in ESRD:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistESRD = 1
  else:
      yhistESRD = 0

  flag=0
  for i in hist:
      for j in CKD:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistCKD = 1
  else:
      yhistCKD = 0

  flag=0
  for i in hist:
      for j in AKI:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistAKI = 1
  else:
      yhistAKI = 0

  flag=0
  for i in hist:
      for j in HTN:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistHTN = 1
  else:
      yhistHTN = 0

  flag=0
  for i in hist:
      for j in Asthma:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistAsthma = 1
  else:
      yhistAsthma = 0

  flag=0
  for i in hist:
      for j in EtOH_WD:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistEtOH_WD = 1
  else:
      yhistEtOH_WD = 0

  flag=0
  for i in hist:
      for j in CAD:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistCAD = 1
  else:
      yhistCAD = 0

  flag=0
  for i in hist:
      for j in OSA:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistOSA = 1
  else:
      yhistOSA = 0

  flag=0
  for i in hist:
      for j in Hypothyroid:
          if i==j:
              flag=1
              break
  if flag==1:
      yhisthypothyroid = 1
  else:
      yhisthypothyroid = 0

  flag=0
  for i in hist:
      for j in Hyperthyroid:
          if i==j:
              flag=1
              break
  if flag==1:
      yhisthyperthyroid = 1
  else:
      yhisthyperthyroid = 0

  flag=0
  for i in hist:
      for j in AI:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistAI = 1
  else:
      yhistAI = 0

  flag=0
  for i in hist:
      for j in Cushing:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistCushing = 1
  else:
      yhistCushing = 0

  flag=0
  for i in hist:
      for j in CVA:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistCVA = 1
  else:
      yhistCVA  = 0

  flag=0
  for i in hist:
      for j in Delirium:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistDelirium = 1
  else:
      yhistDelirium = 0

  flag=0
  for i in hist:
      for j in DLD:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistDLD = 1
  else:
      yhistDLD = 0

  flag=0
  for i in hist:
      for j in Lupus:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistLupus = 1
  else:
      yhistLupus = 0

  flag=0
  for i in hist:
      for j in Scleroderma:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistScleroderma = 1
  else:
      yhistScleroderma = 0

  flag=0
  for i in hist:
      for j in Pericardial_Effusion:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistPericardial_Effusion = 1
  else:
      yhistPericardial_Effusion = 0

  flag=0
  for i in hist:
      for j in Cholecystitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistCholecystitis = 1
  else:
      yhistCholecystitis = 0

  flag=0
  for i in hist:
      for j in ARDS:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistARDS = 1
  else:
      yhistARDS = 0

  flag=0
  for i in hist:
      for j in Cellulitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistCellulitis = 1
  else:
      yhistCellulitis = 0

  flag=0
  for i in hist:
      for j in TBI:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistTBI = 1
  else:
      yhistTBI = 0

  flag=0
  for i in hist:
      for j in Burns:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistBurn = 1
  else:
      yhistBurn = 0

  flag=0
  for i in hist:
      for j in PAD:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistPAD = 1
  else:
      yhistPAD = 0

  flag=0
  for i in hist:
      for j in Brain_Tumor:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistBrain_Tumor = 1
  else:
      yhistBrain_Tumor = 0

  flag=0
  for i in hist:
      for j in GERD:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistGERD = 1
  else:
      yhistGERD = 0

  flag=0
  for i in hist:
      for j in AAA:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistpreopAAA = 1
  else:
      yhistpreopAAA = 0

  flag=0
  for i in hist:
      for j in trach:
          if i==j:
              flag=1
              break
  if flag==1:
      yhisttrach = 1
  else:
      yhisttrach = 0

  flag=0
  for i in hist:
      for j in Pleural_effusion:
          if i==j:
              flag=1
              break
  if flag==1:
      yhistpleural_effusion = 1
  else:
      yhistpleural_effusion = 0


  flag=0
  for i in act:
      for j in Abdominal_Pain:
          if i==j:
              flag=1
              break
  if flag==1:
      yactAbdominal_Pain = 1
  else:
      yactAbdominal_Pain = 0


  flag=0
  for i in act:
      for j in Cellulitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yactcellulitis = 1
  else:
      yactcellulitis = 0


  flag=0
  for i in act:
      for j in Burns:
          if i==j:
              flag=1
              break
  if flag==1:
      yactburn = 1
  else:
      yactburn = 0

  flag=0
  for i in act:
      for j in Afib:
          if i==j:
              flag=1
              break
  if flag==1:
      yactAfib = 1
  else:
      yactAfib = 0



  flag=0
  for i in act:
      for j in DM:
          if i==j:
              flag=1
              break
  if flag==1:
      yactDiabetes = 1
  else:
      yactDiabetes = 0

  flag=0
  for i in act:
      for j in ACS:
          if i==j:
              flag=1
              break
  if flag==1:
      yactACS = 1
  else:
      yactACS = 0

  flag=0
  for i in act:
      for j in AAA:
          if i==j:
              flag=1
              break
  if flag==1:
      yactAAA = 1
  else:
      yactAAA = 0

  flag=0
  for i in act:
      for j in Tachycardia:
          if i==j:
              flag=1
              break
  if flag==1:
      yactTachycardia = 1
  else:
      yactTachycardia = 0

  flag=0
  for i in act:
      for j in Bradycardia:
          if i==j:
              flag=1
              break
  if flag==1:
      yactBradycardia = 1
  else:
      yactBradycardia = 0

  flag=0
  for i in act:
      for j in CHF:
          if i==j:
              flag=1
              break
  if flag==1:
      yactCHF = 1
  else:
      yactCHF = 0

  flag=0
  for i in act:
      for j in HTN_Emergency:
          if i==j:
              flag=1
              break
  if flag==1:
      yactHTN_Emergency = 1
  else:
      yactHTN_Emergency = 0

  flag=0
  for i in act:
      for j in HypotensionShock:
          if i==j:
              flag=1
              break
  if flag==1:
      yactHypotensionShock = 1
  else:
      yactHypotensionShock = 0

  flag=0
  for i in act:
      for j in Cardiac_arrest:
          if i==j:
              flag=1
              break
  if flag==1:
      yactCardiac_arrest = 1
  else:
      yactCardiac_arrest = 0

  flag=0
  for i in act:
      for j in Airway_Obstruction:
          if i==j:
              flag=1
              break
  if flag==1:
      yactAirway_Obstruction = 1
  else:
      yactAirway_Obstruction = 0

  flag=0
  for i in act:
      for j in Pneumonia:
          if i==j:
              flag=1
              break
  if flag==1:
      yactPneumonia = 1
  else:
      yactPneumonia = 0

  flag=0
  for i in act:
      for j in COPD:
          if i==j:
              flag=1
              break
  if flag==1:
      yactCOPD = 1
  else:
      yactCOPD = 0

  flag=0
  for i in act:
      for j in Pneumothorax:
          if i==j:
              flag=1
              break
  if flag==1:
      yactPneumothorax = 1
  else:
      yactPneumothorax = 0

  flag=0
  for i in act:
      for j in Respiratory_Failure:
          if i==j:
              flag=1
              break
  if flag==1:
      yactRespiratory_Failure = 1
  else:
      yactRespiratory_Failure = 0

  flag=0
  for i in act:
      for j in GI_Bleed:
          if i==j:
              flag=1
              break
  if flag==1:
      yactGI_Bleed = 1
  else:
      yactGI_Bleed = 0

  flag=0
  for i in act:
      for j in ALF:
          if i==j:
              flag=1
              break
  if flag==1:
      yactALF = 1
  else:
      yactALF = 0

  flag=0
  for i in act:
      for j in Pancreatitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yactPancreatitis = 1
  else:
      yactPancreatitis = 0

  flag=0
  for i in act:
      for j in Colitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yactColitis = 1
  else:
      yactColitis = 0

  flag=0
  for i in act:
      for j in Gastroenteritis:
          if i==j:
              flag=1
              break
  if flag==1:
      yactGastroenteritis = 1
  else:
      yactGastroenteritis = 0

  flag=0
  for i in act:
      for j in Meningitis_encephalitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yactmeningitis_encephalitis = 1
  else:
      yactmeningitis_encephalitis = 0

  flag=0
  for i in act:
      for j in Bacteremia:
          if i==j:
              flag=1
              break
  if flag==1:
      yactBacteremia = 1
  else:
      yactBacteremia = 0

  flag=0
  for i in act:
      for j in Endocarditis:
          if i==j:
              flag=1
              break
  if flag==1:
      yactEndocarditis = 1
  else:
      yactEndocarditis = 0

  flag=0
  for i in act:
      for j in UTI:
          if i==j:
              flag=1
              break
  if flag==1:
      yactUTI = 1
  else:
      yactUTI = 0

  flag=0
  for i in act:
      for j in Vented:
          if i==j:
              flag=1
              break
  if flag==1:
      yactvented = 1
  else:
      yactvented = 0

  flag=0
  for i in act:
      for j in Afib:
          if i==j:
              flag=1
              break
  if flag==1:
      yactafib = 1
  else:
      yactafib = 0

  flag=0
  for i in act:
      for j in DM:
          if i==j:
              flag=1
              break
  if flag==1:
      yactDM = 1
  else:
      yactDM = 0

  flag=0
  for i in act:
      for j in DKA:
          if i==j:
              flag=1
              break
  if flag==1:
      yactDKA = 1
  else:
      yactDKA = 0

  flag=0
  for i in act:
      for j in PE:
          if i==j:
              flag=1
              break
  if flag==1:
      yactPE = 1
  else:
      yactPE = 0

  flag=0
  for i in act:
      for j in ICH:
          if i==j:
              flag=1
              break
  if flag==1:
      yactICH = 1
  else:
      yactICH = 0

  flag=0
  for i in act:
      for j in SDH:
          if i==j:
              flag=1
              break
  if flag==1:
      yactSDH = 1
  else:
      yactSDH = 0

  flag=0
  for i in act:
      for j in SAH:
          if i==j:
              flag=1
              break
  if flag==1:
      yactSAH = 1
  else:
      yactSAH = 0

  flag=0
  for i in act:
      for j in Seizures:
          if i==j:
              flag=1
              break
  if flag==1:
      yactSeizure = 1
  else:    yactSeizure = 0

  flag=0
  for i in act:
      for j in ESRD:
          if i==j:
              flag=1
              break
  if flag==1:
      yactESRD = 1
  else:
      yactESRD = 0

  flag=0
  for i in act:
      for j in CKD:
          if i==j:
              flag=1
              break
  if flag==1:
      yactCKD = 1
  else:
      yactCKD = 0

  flag=0
  for i in act:
      for j in AKI:
          if i==j:
              flag=1
              break
  if flag==1:
      yactAKI = 1
  else:
      yactAKI = 0

  flag=0
  for i in act:
      for j in HTN:
          if i==j:
              flag=1
              break
  if flag==1:
      yactHTN = 1
  else:
      yactHTN = 0

  flag=0
  for i in act:
      for j in Asthma:
          if i==j:
              flag=1
              break
  if flag==1:
      yactAsthma = 1
  else:
      yactAsthma = 0

  flag=0
  for i in act:
      for j in EtOH_WD:
          if i==j:
              flag=1
              break
  if flag==1:
      yactEtOH_WD = 1
  else:
      yactEtOH_WD = 0

  flag=0
  for i in act:
      for j in CAD:
          if i==j:
              flag=1
              break
  if flag==1:
      yactCAD = 1
  else:
      yactCAD = 0

  flag=0
  for i in act:
      for j in OSA:
          if i==j:
              flag=1
              break
  if flag==1:
      yactOSA = 1
  else:
      yactOSA = 0

  flag=0
  for i in act:
      for j in Hypothyroid:
          if i==j:
              flag=1
              break
  if flag==1:
      yacthypothyroid = 1
  else:
      yacthypothyroid = 0

  flag=0
  for i in act:
      for j in Hyperthyroid:
          if i==j:
              flag=1
              break
  if flag==1:
      yacthyperthyroid = 1
  else:
      yacthyperthyroid = 0

  flag=0
  for i in act:
      for j in AI:
          if i==j:
              flag=1
              break
  if flag==1:
      yactAI = 1
  else:
      yactAI = 0

  flag=0
  for i in act:
      for j in Cushing:
          if i==j:
              flag=1
              break
  if flag==1:
      yactCushing = 1
  else:
      yactCushing = 0

  flag=0
  for i in act:
      for j in CVA:
          if i==j:
              flag=1
              break
  if flag==1:
      yactCVA = 1
  else:
      yactCVA  = 0

  flag=0
  for i in act:
      for j in Delirium:
          if i==j:
              flag=1
              break
  if flag==1:
      yactDelirium = 1
  else:
      yactDelirium = 0

  flag=0
  for i in act:
      for j in DLD:
          if i==j:
              flag=1
              break
  if flag==1:
      yactDLD = 1
  else:
      yactDLD = 0

  flag=0
  for i in act:
      for j in Lupus:
          if i==j:
              flag=1
              break
  if flag==1:
      yactLupus = 1
  else:
      yactLupus = 0

  flag=0
  for i in act:
      for j in Scleroderma:
          if i==j:
              flag=1
              break
  if flag==1:
      yactScleroderma = 1
  else:
      yactScleroderma = 0

  flag=0
  for i in act:
      for j in Pericardial_Effusion:
          if i==j:
              flag=1
              break
  if flag==1:
      yactPericardial_Effusion = 1
  else:
      yactPericardial_Effusion = 0

  flag=0
  for i in act:
      for j in Cholecystitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yactCholecystitis = 1
  else:
      yactCholecystitis = 0

  flag=0
  for i in act:
      for j in ARDS:
          if i==j:
              flag=1
              break
  if flag==1:
      yactARDS = 1
  else:
      yactARDS = 0

  flag=0
  for i in act:
      for j in Cellulitis:
          if i==j:
              flag=1
              break
  if flag==1:
      yactCellulitis = 1
  else:
      yactCellulitis = 0

  flag=0
  for i in act:
      for j in TBI:
          if i==j:
              flag=1
              break
  if flag==1:
      yactTBI = 1
  else:
      yactTBI = 0

  flag=0
  for i in act:
      for j in Burns:
          if i==j:
              flag=1
              break
  if flag==1:
      yactBurn = 1
  else:
      yactBurn = 0

  flag=0
  for i in act:
      for j in PAD:
          if i==j:
              flag=1
              break
  if flag==1:
      yactPAD = 1
  else:
      yactPAD = 0

  flag=0
  for i in act:
      for j in Brain_Tumor:
          if i==j:
              flag=1
              break
  if flag==1:
      yactBrain_Tumor = 1
  else:
      yactBrain_Tumor = 0

  flag=0
  for i in act:
      for j in GERD:
          if i==j:
              flag=1
              break
  if flag==1:
      yactGERD = 1
  else:
      yactGERD = 0

  flag=0
  for i in act:
      for j in AAA:
          if i==j:
              flag=1
              break
  if flag==1:
      yactpreopAAA = 1
  else:
      yactpreopAAA = 0

  flag=0
  for i in act:
      for j in trach:
          if i==j:
              flag=1
              break
  if flag==1:
      yacttrach = 1
  else:
      yacttrach = 0

  flag=0
  for i in act:
      for j in Pleural_effusion:
          if i==j:
              flag=1
              break
  if flag==1:
      yactpleural_effusion = 1
  else:
      yactpleural_effusion = 0
else:
  yhistACS = 0
  yhistAAA = 0
  yhistAbdominal_Pain = 0
  yhistTachycardia = 0
  yhistBradycardia = 0
  yhistCHF = 0
  yhistHTN_Emergency = 0
  yhistHypotensionShock = 0
  yhistCardiac_arrest = 0
  yhistAirway_Obstruction = 0
  yhistPneumonia = 0
  yhistCOPD = 0
  yhistPneumothorax = 0
  yhistRespiratory_Failure = 0
  yhistGI_Bleed = 0
  yhistALF = 0
  yhistPancreatitis = 0
  yhistColitis = 0
  yhistGastroenteritis = 0
  yhistmeningitis_encephalitis = 0
  yhistBacteremia = 0
  yhistEndocarditis = 0
  yhistUTI = 0
  yhistvented = 0
  yhistafib = 0
  yhistDM = 0
  yhistDKA = 0
  yhistPE = 0
  yhistICH = 0
  yhistSDH = 0
  yhistSAH = 0
  yhistSeizure = 0
  yhistESRD = 0
  yhistCKD = 0
  yhistAKI = 0
  yhistHTN = 0
  yhistAsthma = 0
  yhistEtOH_WD = 0
  yhistCAD = 0
  yhistOSA = 0
  yhisthypothyroid = 0
  yhisthyperthyroid = 0
  yhistAI = 0
  yhistCushing = 0
  yhistCVA  = 0
  yhistDelirium = 0
  yhistDLD = 0
  yhistLupus = 0
  yhistScleroderma = 0
  yhistPericardial_Effusion = 0
  yhistCholecystitis = 0
  yhistARDS = 0
  yhistCellulitis = 0
  yhistTBI = 0
  yhistBurn = 0
  yhistPAD = 0
  yhistBrain_Tumor = 0
  yhistGERD = 0
  yhistpreopAAA = 0
  yhisttrach = 0
  yhistpleural_effusion = 0
  yactACS = 0
  yactAAA = 0
  yactAbdominal_Pain = 0
  yactTachycardia = 0
  yactBradycardia = 0
  yactCHF = 0
  yactHTN_Emergency = 0
  yactHypotensionShock = 0
  yactCardiac_arrest = 0
  yactAirway_Obstruction = 0
  yactPneumonia = 0
  yactCOPD = 0
  yactPneumothorax = 0
  yactRespiratory_Failure = 0
  yactGI_Bleed = 0
  yactALF = 0
  yactPancreatitis = 0
  yactColitis = 0
  yactGastroenteritis = 0
  yactmeningitis_encephalitis = 0
  yactBacteremia = 0
  yactEndocarditis = 0
  yactUTI = 0
  yactvented = 0
  yactafib = 0
  yactDM = 0
  yactDKA = 0
  yactPE = 0
  yactICH = 0
  yactSDH = 0
  yactSAH = 0
  yactSeizure = 0
  yactESRD = 0
  yactCKD = 0
  yactAKI = 0
  yactHTN = 0
  yactAsthma = 0
  yactEtOH_WD = 0
  yactCAD = 0
  yactOSA = 0
  yacthypothyroid = 0
  yacthyperthyroid = 0
  yactAI = 0
  yactCushing = 0
  yactCVA  = 0
  yactDelirium = 0
  yactDLD = 0
  yactLupus = 0
  yactScleroderma = 0
  yactPericardial_Effusion = 0
  yactCholecystitis = 0
  yactARDS = 0
  yactCellulitis = 0
  yactTBI = 0
  yactBurn = 0
  yactPAD = 0
  yactBrain_Tumor = 0
  yactGERD = 0
  yactpreopAAA = 0
  yacttrach = 0
  yactpleural_effusion = 0
