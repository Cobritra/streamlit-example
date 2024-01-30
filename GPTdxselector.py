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

docac = doc3._.section_bodies[0]
ell = []
for ent in doc3.ents:
  ell.append(ent._.target_rule.literal)
#ell_strings = [str(span) for span in ell]
#ell = ", ".join(ell_strings)

phlegmasia = 0
keyword = "phlegmasia"
for key in keyword:
  if key in ell:
    phlegmasia = 1
    break

acs = 0
keyword = ["acs", "heart attack", "myocardial infarction"]
for key in keyword:
  if key in ell:
    acs = 1
    break

aaa = 0
keyword = ["aaa", "abdominal aortic aneurysm", "triple a", "aortic aneurysm", "abd aorta enlarged", "enlarged aorta"]
for key in keyword:
  if key in ell:
    aaa = 1
    break

tachycardia = 0
keyword = ["tachycardia", "svt"]
for key in keyword:
  if key in ell:
    tachycardia = 1
    break

afib = 0
keyword = ["afib", "afib with rvr", "atrial flutter", "irregularly irregular"]
for key in keyword:
  if key in ell:
          afib = 1
          break

vtach = 0
keyword = ["vtach", "ventricular tachycardia"]
for key in keyword:
  if key in ell:
          vtach = 1
          break

heart_block = 0
keyword = "heart block"
for key in keyword:
  if key in ell:
          heart_block = 1
          break


wenckebach = 0
keyword = "wenckebach"
for key in keyword:
  if key in ell:
          wenckebach = 1
          break

chf = 0
keyword = ["chf", "congestive heart failure", "heart failure", "cardiac failure", "low ejection fraction", "low ef", "congestive heart"]
for key in keyword:
  if key in ell:
          chf = 1
          break


bradycardia = 0
keyword = ["bradycardia", "bradycardic", "junctional"]
for key in keyword:
  if key in ell:
          bradycardia = 1
          break


htn_emergency = 0
keyword = ["htn emergency", "malignant hypertension"]
for key in keyword:
  if key in ell:
          htn_emergency = 1
          break


hypotension = 0
keyword = ["hypotension"]
for key in keyword:
  if key in ell:
          hypotension = 1
          break

cardiac_arrest = 0
keyword = ["cardiac arrest"]
for key in keyword:
  if key in ell:
          cardiac_arrest = 1
          break

copd = 0
keyword = ["copd", "chronic obstructive lung disease", "chronic obstructive pulmonary disease"]
for key in keyword:
  if key in ell:
          copd = 1
          break


tb = 0
keyword = ["tb", "tuberculosis", "ntm", "tbm"]
for key in keyword:
  if key in ell:
          tb = 1
          break


airway_obstruction = 0
keyword = ["airway obstruction", "vocal chord edema", "airway narrowing"]
for key in keyword:
  if key in ell:
          airway_obstruction = 1
          break

vented = 0
keyword = ["vented", "on ventilator", "intubated", "intubation"]
for key in keyword:
  if key in ell:
          vented = 1
          break


pneumonia = 0
keyword = ["pneumonia", "lung infection", "pulmonary infection", "lung infiltrate", "pulmonary infiltrate", "pulmonary consolidation"]
for key in keyword:
  if key in ell:
    pneumonia = 1
    break

pe = 0
keyword = ["pulmonary perfusion defect", "pulmonary embolism", "pe", "pulmonary emboli", "pulmonary embolus"]
for key in keyword:
  if key in ell:
          pe = 1
          break

ptx = 0
keyword = ["collapsed lung", "air around lung", "ptx"]
for key in keyword:
  if key in ell:
    ptx = 1
    break

respiratory_failure = 0
keyword = ["respiratory failure", "intubated"]
for key in keyword:
  if key in ell:
          respiratory_failure = 1
          break

alf = 0
keyword = ["liver failure", "transaminitis"]
for key in keyword:
  if key in ell:
          alf = 1
          break

abdominal_pain = 0
keyword = ["left upper quadrant pain", "right upper quadrant pain", "right lower quadrant pain", "abdominal pain"]
for key in keyword:
  if key in ell:
          abdominal_pain = 1
          break


gi_bleed = 0
keyword = ["gi bleed", "gib", "hematchezia", "melena", "hematchezia", "vomiting blood", "brbpr", "blood per rectum"]
for key in keyword:
  if key in ell:
          gi_bleed = 1
          break


acute_pancreatitis = 0
keyword = ["inflamed pancreas", "elevated lipase", "pancreatic inflammation", "pancreatitis"]
for key in keyword:
  if key in ell:
          acute_pancreatitis = 1
          break

colitis = 0
keyword = ["colitis", "bowel infection", "gut inflammation", "bowel inflammation", "inflamed bowel"]
for key in keyword:
  if key in ell:
          colitis = 1
          break

bacteremia = 0
keyword = ["blood infection", "positive blood culture", "gram negatives in blood", "+ blood culture", "bacteremia"]
for key in keyword:
  if key in ell:
          bacteremia = 1
          break

gastroenteritis = 0
keyword = ["gastroenteritis"]
for key in keyword:
  if key in ell:
          gastroenteritis = 1
          break

meningitis_encephalitis = 0
keyword = ["meningitis", "nuchal rigidity", "nuchal rigidity", "cns infection", "encephalitis", "septic emboli"]
for key in keyword:
  if key in ell:
          meningitis_encephalitis = 1
          break


endocarditis = 0
keyword = ["endocarditis"]
for key in keyword:
  if key in ell:
          endocarditis = 1
          break

uti = 0
keyword = ["urinary tract infection", "positive urine", "uti"]
for key in keyword:
  if key in ell:
          uti = 1
          break

dm = 0
keyword = ["diabetes mellitus", "dmt2", "iddm2", "iddm", "dm2", "dm"]
for key in keyword:
  if key in ell:
          dm = 1
          break

dka = 0
keyword = ["dka", "diabetic ketoacidosis"]
for key in keyword:
  if key in ell:
          dka = 1
          break

ich = 0
keyword = ["ich", "intracranial hemorrhage"]
for key in keyword:
  if key in ell:
          ich = 1
          break

sdh = 0
keyword = ["sdh"]
for key in keyword:
  if key in ell:
          sdh = 1
          break

sah = 0
keyword = ["sah"]
for key in keyword:
  if key in ell:
          sah = 1
          break

seizure = 0
keyword = ["seizure", "seizures"]
for key in keyword:
  if key in ell:
          seizure = 1
          break

ckd = 0
keyword = ["ckd", "chronic kidney disease"]
for key in keyword:
  if key in ell:
          ckd = 1
          break

esrd = 0
keyword = ["end-stage renal disease", "end stage kidney disease", "esrd"]
for key in keyword:
  if key in ell:
          esrd = 1
          break

etoh_wd = 0
keyword = ["alcohol withdrawal"]
for key in keyword:
  if key in ell:
          etoh_wd = 1
          break

htn = 0
keyword = ["hypertension", "high blood pressure", "elevated blood pressure"]
for key in keyword:
  if key in ell:
          htn = 1
          break

asthma = 0
keyword = ["asthma"]
for key in keyword:
  if key in ell:
          asthma = 1
          break


cad = 0
keyword = ["cad", "coronary artery disease", "coronary obstruction"]
for key in keyword:
  if key in ell:
          cad = 1
          break

hypothyroidism = 0
keyword = ["hypothyroidism", "hypoactive thyroid", "myxedema coma"]
for key in keyword:
  if key in ell:
      hypothyroidism = 1
      break

hyperthyroidism = 0
keyword = ["hyperactive thyroid", "hyperthyroidism"]
for key in keyword:
  if key in ell:
          hyperthyroidism = 1
          break

cva = 0
keyword = ["cva", "ischemic stroke"]
for key in keyword:
  if key in ell:
          cva = 1
          break

osa = 0
keyword = ["osa", "obstructive sleep apnea", "sleep apnea"]
for key in keyword:
  if key in ell:
          osa = 1
          break

dld = 0
keyword = ["high cholesterol", "hyperlipidemia"]
for key in keyword:
  if key in ell:
          dld = 1
          break

delirium = 0
keyword = ["delirium"]
for key in keyword:
  if key in ell:
          delirium = 1
          break

ai = 0
keyword = ["adrenal insufficiency", "low cortisol", "hypocortisolemia"]
for key in keyword:
  if key in ell:
          ai = 1
          break

cushings = 0
keyword = ["cushings", "cushings disease", "hypercortisolemia", "high cortisol"]
for key in keyword:
  if key in ell:
          cushings = 1
          break

lupus = 0
keyword = ["lupus", "systemic lupus erythematosus", "lupus erythematosus", "lupus erythematosus", "systemic lupus"]
for key in keyword:
  if key in ell:
          lupus = 1
          break

scleroderma = 0
keyword = ["systemic sclerosis", "scleroderma"]
for key in keyword:
  if key in ell:
    scleroderma = 1
    break

hemopericardium = 0
keyword = ["hemopericardium"]
for key in keyword:
  if key in ell:
          hemopericardium = 1
          break

pneumopericardium = 0
keyword = ["pneumopericardium"]
for key in keyword:
  if key in ell:
          pneumopericardium = 1
          break

hemoperitoneum = 0
keyword = ["hemoperitoneum"]
for key in keyword:
  if key in ell:
        hemoperitoneum = 1
        break

pneumoperitoneum = 0
keyword = ["pneumoperitoneum"]
for key in keyword:
  if key in ell:
          pneumoperitoneum = 1
          break

pericardial_effusion = 0
keyword = ["pericardial effusion"]
for key in keyword:
  if key in ell:
          hemopericardium = 1
          break

cholecystitis = 0
keyword = ["cholecystitis"]
for key in keyword:
  if key in ell:
          cholecystitis = 1
          break

ards = 0
keyword = ["ards", "acute respiratory distress syndrome", "respiratory distress syndrome"]
for key in keyword:
  if key in ell:
          ards = 1
          break

cellulitis = 0
keyword = ["cellulitis", "skin infection"]
for key in keyword:
  if key in ell:
          cellulitis = 1
          break

tbi = 0
keyword = ["tbi", "traumatic brain injury", "brain injury"]
for key in keyword:
  if key in ell:
          tbi = 1
          break

cancer = 0
keyword = ["cancer"]
for key in keyword:
  if key in ell:
          cancer = 1
          break

burn = 0
keyword = ["burn", "thermal injury"]
for key in keyword:
  if key in ell:
          burn = 1
          break

cp = 0
keyword = ["cp"]
for key in keyword:
  if key in ell:
    cp = 1
    break

pvd = 0
keyword = ["pvd", "pad", "peripheral vascular disease"]
for key in keyword:
  if key in ell:
          pvd = 1
          break

brain_tumor = 0
keyword = ["brain tumor", "schwanomma", "gbm", "glioblastoma", "astrocytoma"]
for key in keyword:
  if key in ell:
          brain_tumor = 1
          break

gerd = 0
keyword = ["gerd", "gastroesophageal reflux disease", "gastroesophageal refluxes", "gastric reflux", "reflux disease"]
for key in keyword:
  if key in ell:
          gerd = 1
          break

alf = 0
keyword = ["alcoholic liver cirrhosis", "liver failure", "liver cirrhosis", "cirrhosis", "cirrhotic", "varices"]
for key in keyword:
  if key in ell:
          alf = 1
          break

pleural_effusion = 0
keyword = ["empyema", "hemothorax", "pleural effusion"]
for key in keyword:
  if key in ell:
          pleural_effusion = 1
          break


#NLTK Dx calculator
if (acs > .4):
    y_predACS = 1
else:
    y_predACS = 0

if (((aaa >.4 and yhistAAA <.4))):
    y_predAAA = 1
else:
    y_predAAA = 0

if (tachycardia >.4):
    y_predTachycardia = 1
else:
    y_predTachycardia = 0

if (bradycardia >.4):
    y_predBradycardia = 1
else:
    y_predBradycardia = 0

if ((yhistCHF > .4 or chf > .4)):
    y_predCHF = 1
else:
    y_predCHF = 0

if (htn_emergency > .4 or data['Systolic'][0] >= 195):
    y_predHTN_Emergency = 1
else:
    y_predHTN_Emergency = 0

if (hypotension >.4 or data['Systolic'][0] <= 80):
    y_predHypotensionShock = 1
else:
    y_predHypotensionShock = 0

if (cardiac_arrest >.4):
    y_predCardiac_arrest = 1
else:
    y_predCardiac_arrest = 0

if ((airway_obstruction > .4)) :
    y_predAirway_Obstruction = 1
else:
    y_predAirway_Obstruction = 0

if ((pneumonia > .4 and yhistPneumonia <.4)):
    y_predPneumonia = 1
else:
    y_predPneumonia = 0

if (copd > .4):
    y_predCOPD = 1
else:
    y_predCOPD = 0

if (ptx >.4):
    y_predPneumothorax = 1
else:
    y_predPneumothorax = 0

if (data['Vented'][0] > .4 or respiratory_failure > .4):
    y_predRespiratory_Failure = 1
else:
    y_predRespiratory_Failure = 0

if (gi_bleed >.4):
    y_predGI_Bleed = 1
else:
    y_predGI_Bleed = 0

if (alf >.4):
    y_predALF = 1
else:
    y_predALF = 0

if (acute_pancreatitis > .4):
    y_predacutePancreatitis = 1
else:
    y_predacutePancreatitis = 0

if ((colitis > .4 and yhistColitis <.4)):
    y_predColitis = 1
else:
    y_predColitis = 0

if (gastroenteritis > .4):
    y_predGastroenteritis = 1
else:
    y_predGastroenteritis = 0

if ((meningitis_encephalitis >.4 and yhistmeningitis_encephalitis <.4)):
    y_predmeningitis_encephalitis = 1
else:
    y_predmeningitis_encephalitis = 0

if ((bacteremia > .4 and yhistmeningitis_encephalitis <.4)):
    y_predBacteremia = 1
else:
    y_predBacteremia = 0

if ((endocarditis >.4 and yhistEndocarditis <.4)) :
    y_predEndocarditis = 1
else:
    y_predEndocarditis = 0

if ((uti >.4 and yhistUTI <.4)):
    y_predUTI = 1
else:
    y_predUTI = 0

if (data['Vented'][0] > .4 or vented > .4):
    y_predvented = 1
else:
    y_predvented = 0

if (afib > .4 or yhistafib > .4):
    y_predafib = 1
else:
    y_predafib = 0

if ((dm > .4 or yhistDM >.4)):
    y_predDM = 1
else:
    y_predDM = 0

if (dka > .4 and data['AG'][0] > 15 and (dm > .4 or yhistDM >.4)):
    y_predDKA = 1
else:
    y_predDKA = 0

if ((pe >.4 and yhistPE <.4)):
    y_predPE = 1
else:
    y_predPE = 0

if ((ich >.4 and yhistICH <.4)):
    y_predICH = 1
else:
    y_predICH = 0

if ((sdh >.4 and yhistSDH <.4)):
    y_predSDH = 1
else:
    y_predSDH = 0

if ((sah >.4 and yhistSAH <.4)):
    y_predSAH = 1
else:
    y_predSAH = 0

if ((seizure >.4 and yhistSeizure <.4)):
    y_predSeizure = 1
else:
    y_predSeizure = 0

if (yhistESRD > .4) and (data['Cr'][0] >= 2):
    y_predESRD = 1
else:
    y_predESRD = 0

if (ckd > .4 or yhistCKD > .4) and (data['Cr'][0] >= 1.4):
    y_predCKD = 1
else:
    y_predCKD = 0

if (data['Cr'][0] >= 1.4 and y_predCKD <.4 and y_predESRD <.4):
    y_predAKI = 1
else:
    y_predAKI = 0

if ((abdominal_pain > .4 and yhistAbdominal_Pain <.4)):
    y_predAbdominal_Pain = 1
else:
    y_predAbdominal_Pain = 0

if (htn > .4 or yhistHTN > .4 or data['Systolic'][0] >= 150):
    y_predHTN = 1
else:
    y_predHTN = 0

if ((asthma >.4 and yhistAsthma <.4)):
    y_predAsthma = 1
else:
    y_predAsthma = 0

if ((etoh_wd >.4 and yhistEtOH_WD <.4)):
    y_predEtOH_WD = 1
else:
    y_predEtOH_WD = 0

if (cad > .4 or yhistACS > .4):
    y_predCAD = 1
else:
    y_predCAD = 0

if (osa > .4 or yhistOSA > .4):
    y_predOSA = 1
else:
    y_predOSA = 0

if (hypothyroidism > .4 or yhisthypothyroid > .4):
    y_predhypothyroid = 1
else:
    y_predhypothyroid = 0

if (yhisthyperthyroid > .4 or hyperthyroidism >.4):
    y_predhyperthyroid = 1
else:
    y_predhyperthyroid = 0

if (ai >.4):
    y_predAI = 1
else:
    y_predAI = 0

if ((yhistCushing > .4 or cushings >.4)):
    y_predCushing = 1
else:
    y_predCushing = 0

if (cva > .4):
    y_predCVA = 1
else:
    y_predCVA  = 0

if ((delirium >.4)):
    y_predDelirium = 1
else:
    y_predDelirium = 0

if ((dld > .4 or yhistDLD > .4)):
    y_predDLD = 1
else:
    y_predDLD = 0

if ((yhistLupus > .4 or lupus >.4)):
    y_predLupus = 1
else:
    y_predLupus = 0

if ((yhistScleroderma >.4 or scleroderma >.4)):
    y_predScleroderma = 1
else:
    y_predScleroderma = 0

if ((pericardial_effusion >.4 and yhistPericardial_Effusion <.4)):
    y_predPericardial_Effusion = 1
else:
    y_predPericardial_Effusion = 0

if ((cholecystitis >.4)):
    y_predCholecystitis = 1
else:
    y_predCholecystitis = 0

if ((ards >.4) and Intubated > .4):
    y_predARDS = 1
else:
    y_predARDS = 0

if (data['Plt'][0] < 50 or data['INR'][0] > 1.5 or data['PTT'][0] > 50):
    y_predCoagulopathy = 1
else:
    y_predCoagulopathy = 0

if ((cellulitis >.4)):
    y_predCellulitis = 1
else:
    y_predCellulitis = 0

if ((yhistTBI > .4 or tbi >.4)):
    y_predTBI = 1
else:
    y_predTBI = 0

if ((burn >.4)):
    y_predBurn = 1
else:
    y_predBurn = 0

if ((pvd >.4)):
    y_predPAD = 1
else:
    y_predPAD = 0

if ((brain_tumor >.4)):
    y_predBrain_Tumor = 1
else:
    y_predBrain_Tumor = 0

if ((yhistGERD > .4)):
    y_predGERD = 1
else:
    y_predGERD = 0

#if y_predxgbpreopUEAngio > .4:
    #y_predpreopUEAngio = 1
#else:
 ##   y_predpreopUEAngio = 0

#if y_predxgbpreopImpella > .4:
   # y_predpreopImpella = 1
#else:
   # y_predpreopImpella = 0

#if y_predxgbpreopCraniotomy > .4:
  #  y_predpreopCraniotomy = 1
#else:
  #  y_predpreopCraniotomy = 0

#if y_predxgbpreopCath > .4:
  #  y_predpreopCath = 1
#else:
  #  y_predpreopCath = 0

#if y_predxgbpreopCABG > .4:
 #   y_predpreopCABG = 1#
#else:
 #   y_predpreopCABG = 0

#if y_predxgbpreopAVR > .4:
 #   y_predpreopAVR = 1
#else:
 #   y_predpreopAVR = 0

#if y_predxgbpreopAngiogram > .4:
 #   y_predpreopAngiogram = 1
#else:
 #   y_predpreopAngiogram = 0

#if y_predxgbpreopAAA > .4:
 #   y_predpreopAAA = 1
#else:
 #   y_predpreopAAA = 0

if (data['Plt'][0] < 10 or data['INR'][0] > 4 or data['PTT'][0] > 120):
    severecoag = 1
else:
    severecoag = 0

if (data['Plt'][0] < 79 or data['INR'][0] > 2 or data['PTT'][0] > 50):
    coag = 1
else:
    coag = 0

if (y_predvented >.4 or y_predGERD >.4 or y_predGI_Bleed >.4 or y_predSAH >.4 or y_predSDH >.4 or y_predICH >.4 or y_predRespiratory_Failure >.4 or y_predTBI >.4 or y_predBurn >.4 or y_predBrain_Tumor >.4 or y_predCoagulopathy >.4):
    SUP = 1
else:
    SUP = 0

if (y_predSAH >.4 or y_predSDH >.4 or y_predTBI >.4 or y_predGI_Bleed >.4 or y_predICH >.4 or y_predBrain_Tumor >.4 or y_predAAA >.4 or y_predCoagulopathy >.4 or data['Hgb'][0] < 7):
    chemDVT = 0
else:
    chemDVT = 1

if (y_predPAD >.4 or y_predCellulitis >.4 or severecoag > .4):
    mechDVT = 0
else:
    mechDVT = 1

if (y_predSAH >.4 or y_predSDH >.4 or y_predTBI >.4 or y_predGI_Bleed >.4 or y_predICH >.4 or y_predAAA >.4):
    Bleed = 1
else:
    Bleed = 0

if (y_predSAH >.4 or y_predSDH >.4 or y_predTBI >.4 or y_predGI_Bleed >.4 or y_predICH >.4 or y_predAAA >.4 or y_predDKA >.4 or y_predCardiac_arrest >.4):
    NPO = 1
else:
    NPO = 0

#PreOpper
if len(op) > 0:
  op.columns=['column1', 'column2']
  op['column1'] = op['column1'].astype(str)
  op['column2'] = op['column2'].astype(str)
  surgeen = op.loc[op['column2'].str.contains("SURGEON")]
  surgeen['column1'] = surgeen['column1'].astype(str)
  surgeen = list(surgeen['column1'])
  procedure = op.loc[op['column2'].str.contains("PROCEDURE")]
  procedure['column1'] = procedure['column1'].astype(str)
  procedure = list(procedure['column1'])
  #hist
  flag=0
  for i in procedure:
      for j in extremity_angiogram:
          if i==j:
              flag=1
              break
  if flag==1:
      yprocextremity_angiogram = 1
  else:
      yprocextremity_angiogram = 0

  flag=0
  for i in procedure:
      for j in pericardial_window:
          if i==j:
              flag=1
              break
  if flag==1:
      yprocpericardial_window = 1
  else:
      yprocpericardial_window = 0

  flag=0
  for i in procedure:
      for j in lung_transplant:
          if i==j:
              flag=1
              break
  if flag==1:
      yproclung_transplant = 1
  else:
      yproclung_transplant = 0

  flag=0
  for i in procedure:
      for j in coronary_angiogram:
          if i==j:
              flag=1
              break
  if flag==1:
      yproccoronary_angiogram = 1
  else:
      yproccoronary_angiogram = 0

  flag=0
  for i in procedure:
      for j in maze:
          if i==j:
              flag=1
              break
  if flag==1:
      yprocmaze = 1
  else:
      yprocmaze = 0

  flag=0
  for i in procedure:
      for j in lvad:
          if i==j:
              flag=1
              break
  if flag==1:
      yproclvad = 1
  else:
      yproclvad = 0

  flag=0
  for i in procedure:
      for j in mvr:
          if i==j:
              flag=1
              break
  if flag==1:
      yprocmvr = 1
  else:
      yprocmvr = 0

  flag=0
  for i in procedure:
      for j in avr:
          if i==j:
              flag=1
              break
  if flag==1:
      yprocavr = 1
  else:
      yprocavr = 0

  flag=0
  for i in procedure:
      for j in tvr:
          if i==j:
              flag=1
              break
  if flag==1:
      yproctvr = 1
  else:
      yproctvr = 0

  flag=0
  for i in procedure:
      for j in CABG:
          if i==j:
              flag=1
              break
  if flag==1:
      yproccabg = 1
  else:
      yproccabg = 0

  flag=0
  for i in procedure:
      for j in impella:
          if i==j:
              flag=1
              break
  if flag==1:
      yprocimpella = 1
  else:
      yprocimpella = 0

  flag=0
  for i in procedure:
      for j in AAA:
          if i==j:
              flag=1
              break
  if flag==1:
      yprocaaa = 1
  else:
      yprocaaa = 0

  flag=0
  for i in procedure:
      for j in oht:
          if i==j:
              flag=1
              break
  if flag==1:
      yprocoht = 1
  else:
      yprocoht = 0

  flag=0
  for i in procedure:
      for j in aortic_dissection:
          if i==j:
              flag=1
              break
  if flag==1:
      yprocaortic_dissection = 1
  else:
      yprocaortic_dissection = 0

  flag=0
  for i in procedure:
      for j in craniotomy:
          if i==j:
              flag=1
              break
  if flag==1:
      yproccraniotomy = 1
  else:
      yproccraniotomy = 0

  flag=0
  for i in procedure:
      for j in kyphoplasty:
          if i==j:
              flag=1
              break
  if flag==1:
      yprockyphoplasty = 1
  else:
      yprockyphoplasty = 0

  flag=0
  for i in procedure:
      for j in ivorlewis:
          if i==j:
              flag=1
              break
  if flag==1:
      yprocivorlewis = 1
  else:
      yprocivorlewis = 0
else:
  yprocextremity_angiogram = 0
  yprocpericardial_window = 0
  yproclung_transplant = 0
  yproccoronary_angiogram = 0
  yprocmaze = 0
  yproclvad = 0
  yprocmvr = 0
  yprocavr = 0
  yproctvr = 0
  yproccabg = 0
  yprocimpella = 0
  yprocaaa = 0
  yprocoht = 0
  yprocaortic_dissection = 0
  yproccraniotomy = 0
  yprockyphoplasty = 0
  yprocivorlewis = 0

