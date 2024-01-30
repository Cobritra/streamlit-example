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

warnings.filterwarnings('ignore')
zp = pd.DataFrame(doc2._.context_graph.edges)

warnings.filterwarnings('ignore')
if len(zp) > 0:
  zp.columns=['column1', 'column2']
  zp['column1'] = zp['column1'].astype(str)
  zp['column2'] = zp['column2'].astype(str)
  NaSodium = zp.loc[zp['column2'].str.contains("NA")]
  NaSodium['column1'] = NaSodium['column1'].astype(float)
  NaSodium = list(NaSodium['column1'])
  KPotassium = zp.loc[zp['column2'].str.contains("K")]
  KPotassium['column1'] = KPotassium['column1'].astype(float)
  KPotassium = list(KPotassium['column1'])
  CrCreatinine = zp.loc[zp['column2'].str.contains("CREATININE")]
  CrCreatinine['column1'] = CrCreatinine['column1'].astype(float)
  CrCreatinine = list(CrCreatinine['column1'])
  BiliBilirubin = zp.loc[zp['column2'].str.contains("BILIRUBIN")]
  BiliBilirubin['column1'] = BiliBilirubin['column1'].astype(float)
  BiliBilirubin = list(BiliBilirubin['column1'])
  ClChloride = zp.loc[zp['column2'].str.contains("CHLORIDE")]
  ClChloride['column1'] = ClChloride['column1'].astype(float)
  ClChloride = list(ClChloride['column1'])
  CO2co2 = zp.loc[zp['column2'].str.contains("CO2")]
  CO2co2['column1'] = CO2co2['column1'].astype(float)
  CO2co2 = list(CO2co2['column1'])
  GlGlucose = zp.loc[zp['column2'].str.contains("GLUCOSE")]
  GlGlucose['column1'] = GlGlucose['column1'].astype(float)
  GlGlucose = list(GlGlucose['column1'])
  AlbAlbumin = zp.loc[zp['column2'].str.contains("ALBUMIN")]
  AlbAlbumin['column1'] = AlbAlbumin['column1'].astype(float)
  AlbAlbumin = list(AlbAlbumin['column1'])
  PrProtein = zp.loc[zp['column2'].str.contains("PROTEIN")]
  PrProtein['column1'] = PrProtein['column1'].astype(float)
  PrProtein = list(PrProtein['column1'])
  AstAST = zp.loc[zp['column2'].str.contains("AST")]
  AstAST['column1'] = AstAST['column1'].astype(float)
  AstAST = list(AstAST['column1'])
  AltALT = zp.loc[zp['column2'].str.contains("ALT")]
  AltALT['column1'] = AltALT['column1'].astype(float)
  AltALT = list(AltALT['column1'])
  wbcWBC = zp.loc[zp['column2'].str.contains("WBC")]
  wbcWBC['column1'] = wbcWBC['column1'].astype(float)
  wbcWBC = list(wbcWBC['column1'])
  hgbHGB = zp.loc[zp['column2'].str.contains("HEMOGLOBIN]")]
  hgbHGB['column1'] = hgbHGB['column1'].astype(float)
  hgbHGB = list(hgbHGB['column1'])
  pltPLT = zp.loc[zp['column2'].str.contains("PLATELET")]
  pltPLT['column1'] = pltPLT['column1'].astype(float)
  pltPLT = list(pltPLT['column1'])
  TTemp = zp.loc[zp['column2'].str.contains("TEMPERATURE")]
  TTemp['column1'] = TTemp['column1'].astype(float)
  TTemp = list(TTemp['column1'])
  bpBP = zp.loc[zp['column2'].str.contains("BP")]
  bpBP['column1'] = bpBP['column1'].astype(float)
  bpBP = list(bpBP['column1'])
  sbpSBP = zp.loc[zp['column2'].str.contains("SYSTOLIC")]
  sbpSBP['column1'] = sbpSBP['column1'].astype(float)
  sbpSBP = list(sbpSBP['column1'])
  dbpDBP = zp.loc[zp['column2'].str.contains("DIASTOLIC")]
  dbpDBP['column1'] = dbpDBP['column1'].astype(float)
  dbpDBP = list(dbpDBP['column1'])
  mapMAP = zp.loc[zp['column2'].str.contains("MAP")]
  mapMAP['column1'] = mapMAP['column1'].astype(float)
  mapMAP = list(mapMAP['column1'])
  HRHeartrate = zp.loc[zp['column2'].str.contains("HEART RATE")]
  HRHeartrate['column1'] = HRHeartrate['column1'].astype(float)
  HRHeartrate = list(HRHeartrate['column1'])
  O2satSPO2 = zp.loc[zp['column2'].str.contains("O2 SAT")]
  O2satSPO2['column1'] = O2satSPO2['column1'].astype(float)
  O2satSPO2 = list(O2satSPO2['column1'])
  RRResp = zp.loc[zp['column2'].str.contains("RESPIRATORY RATE")]
  RRResp['column1'] = RRResp['column1'].astype(float)
  RRResp = list(RRResp['column1'])
  aPTTptt = zp.loc[zp['column2'].str.contains("PTT")]
  aPTTptt['column1'] = aPTTptt['column1'].astype(float)
  aPTTptt = list(aPTTptt['column1'])
  PTpt = zp.loc[zp['column2'].str.contains("PT")]
  PTpt['column1'] = PTpt['column1'].astype(float)
  PTpt = list(PTpt['column1'])
  inrINR = zp.loc[zp['column2'].str.contains("INR")]
  inrINR['column1'] = inrINR['column1'].astype(float)
  inrINR = list(inrINR['column1'])
  sysef = zp.loc[zp['column2'].str.contains("SYSEF")]
  sysef['column1'] = sysef['column1'].astype(float)
  sysef = list(sysef['column1'])
  kuL = zp.loc[zp['column2'].str.contains("KUL")]
  kuL['column1'] = kuL['column1'].astype(float)
  kuL = list(kuL['column1'])
  last7 = zp.loc[zp['column2'].str.contains("LAST7")]
  last7['column1'] = last7['column1'].astype(float)
  last7 = list(last7['column1'])
  KPotassium = [elem for elem in KPotassium if elem not in kuL]
  sbpSBP = [elem for elem in sbpSBP if elem not in sysef]
  inrINR = [elem for elem in inrINR if elem not in last7]


  #harmonizing variable sources: this filters impossible variables and allows input of variables automatically and manually without error
  NaSodiummod = [num for num in NaSodium if num > 99 and num < 200]
  KPotassiummod = [num for num in KPotassium if num > 1.5 and num < 10]
  CrCreatininemod = [num for num in CrCreatinine if num > .2 and num < 20]
  BiliBilirubinmod = [num for num in BiliBilirubin if num > .2 and num < 50]
  ClChloridemod = [num for num in ClChloride if num > 65 and num < 130]
  CO2co2mod = [num for num in CO2co2 if num > 1 and num < 50]
  GlGlucosemod = [num for num in GlGlucose if num > 6 and num < 2000]
  AlbAlbuminmod = [num for num in AlbAlbumin if num > .6 and num < 6]
  PrProteinmod = [num for num in PrProtein if num > 1 and num < 11]
  AstASTmod = [num for num in AstAST if num > 6 and num < 2500]
  AltALTmod = [num for num in AltALT if num > 6 and num < 2500]
  wbcWBCmod = [num for num in wbcWBC if num > 0 and num < 200]
  hgbHGBmod = [num for num in hgbHGB if num > 0 and num < 20]
  pltPLTmod = [num for num in pltPLT if num >= 1 and num < 1000]
  TTempmod = [num for num in TTemp if num > 32 and num < 108]
  bpBPmod = [num for num in bpBP if num > 32 and num < 300]
  sbpSBPmod = [num for num in sbpSBP if num > 32 and num < 300]
  dbpDBPmod = [num for num in dbpDBP if num > 32 and num < 300]
  mapMAPmod = [num for num in mapMAP if num > 32 and num < 180]
  HRHeartratemod = [num for num in HRHeartrate if num > 12 and num < 280]
  O2satSPO2mod = [num for num in O2satSPO2 if num > 22 and num < 100]
  RRRespmod = [num for num in RRResp if num > 3 and num < 44]
  aPTTpttmod = [num for num in aPTTptt if num > 8 and num < 300]
  PTptmod = [num for num in PTpt if num > 5 and num < 45]
  inrINRmod = [num for num in inrINR if num > .5 and num < 18]
  def get_number_farthest_from_stdev(num):
    if len(num) > 0:
      mean = statistics.mean(num)
      stdev = statistics.stdev(num)
      diffs = [abs(num - mean) for num in num]
      farthest_index = diffs.index(max(diffs))
      return num[farthest_index]
    else:
      num = num
  if len(NaSodiummod) > 1:
    NaSodiumvec = get_number_farthest_from_stdev(NaSodiummod)
  elif len(NaSodiummod) == 1:
    NaSodiumvec = float(NaSodiummod[0])
  elif len(NaSodiummod) == 0:
    NaSodiumvec = 140
  if len(KPotassiummod) > 1:
    KPotassiumvec = get_number_farthest_from_stdev(KPotassiummod)
  else:
    if len(KPotassiummod) == 1:
      KPotassiumvec = float(KPotassiummod[0])
    else:
      KPotassiumvec = 4
  if len(CrCreatininemod) > 1:
    CrCreatininevec = get_number_farthest_from_stdev(CrCreatininemod)
  else:
    if len(CrCreatininemod) == 1:
      CrCreatininevec = float(CrCreatininemod[0])
    else:
      CrCreatininevec = 1
  if len(ClChloridemod) > 1:
    ClChloridevec = get_number_farthest_from_stdev(ClChloridemod)
  else:
    if len(ClChloridemod) == 1:
      ClChloridevec = float(ClChloridemod[0])
    else:
      ClChloridevec = None
  if len(CO2co2mod) > 1:
    CO2co2vec = get_number_farthest_from_stdev(CO2co2mod)
  else:
    if len(CO2co2mod) == 1:
      CO2co2vec = float(CO2co2mod[0])
    else:
      CO2co2vec = None
  if len(GlGlucosemod) > 1:
    GlGlucosevec = get_number_farthest_from_stdev(GlGlucosemod)
  else:
    if len(GlGlucosemod) == 1:
      GlGlucosevec = float(GlGlucosemod[0])
    else:
      GlGlucosevec = None
  if len(BiliBilirubinmod) > 1:
    BiliBilirubinvec = get_number_farthest_from_stdev(BiliBilirubinmod)
  else:
    if len(BiliBilirubinmod) == 1:
      BiliBilirubinvec = float(BiliBilirubinmod[0])
    else:
      BiliBilirubinvec = None
  if len(AlbAlbuminmod) > 1:
    AlbAlbuminvec = get_number_farthest_from_stdev(AlbAlbuminmod)
  else:
    if len(AlbAlbuminmod) == 1:
      AlbAlbuminvec = float(AlbAlbuminmod[0])
    else:
      AlbAlbuminvec = None
  if len(PrProteinmod) > 1:
    PrProteinvec = get_number_farthest_from_stdev(PrProteinmod)
  else:
    if len(PrProteinmod) == 1:
      PrProteinvec = float(PrProteinmod[0])
    else:
      PrProteinvec = None
  if len(AstASTmod) > 1:
    AstASTvec = get_number_farthest_from_stdev(AstASTmod)
  else:
    if len(AstASTmod) == 1:
      AstASTvec = float(AstASTmod[0])
    else:
      AstASTvec = None
  if len(AltALTmod) > 1:
    AltALTvec = get_number_farthest_from_stdev(AltALTmod)
  else:
    if len(AltALTmod) == 1:
      AltALTvec = float(AltALTmod[0])
    else:
      AltALTvec = None
  if len(wbcWBCmod) > 1:
    wbcWBCvec = get_number_farthest_from_stdev(wbcWBCmod)
  else:
    if len(wbcWBCmod) == 1:
      wbcWBCvec = float(wbcWBCmod[0])
    else:
      wbcWBCvec = None
  if len(hgbHGBmod) > 1:
    hgbHGBvec = get_number_farthest_from_stdev(hgbHGBmod)
  else:
    if len(hgbHGBmod) == 1:
      hgbHGBvec = float(hgbHGBmod[0])
    else:
      hgbHGBvec = 12
  if len(pltPLTmod) > 1:
    pltPLTvec = get_number_farthest_from_stdev(pltPLTmod)
  else:
    if len(pltPLTmod) == 1:
      pltPLTvec = float(pltPLTmod[0])
    else:
      pltPLTvec = 300
  if len(TTempmod) > 1:
    TTempvec = get_number_farthest_from_stdev(TTempmod)
  else:
    if len(TTempmod) == 1:
      TTempvec = float(TTempmod[0])
    else:
      TTempvec = None
  if len(bpBPmod) > 1:
    bpBPvec = get_number_farthest_from_stdev(bpBPmod)
  else:
    if len(bpBPmod) == 1:
      bpBPvec = float(bpBPmod[0])
    else:
      bpBPvec = None
  if len(sbpSBPmod) > 1:
    sbpSBPvec = get_number_farthest_from_stdev(sbpSBPmod)
  else:
    if len(sbpSBPmod) == 1:
      sbpSBPvec = float(sbpSBPmod[0])
    else:
      sbpSBPvec = 120
  if len(dbpDBPmod) > 1:
    dbpDBPvec = get_number_farthest_from_stdev(dbpDBPmod)
  else:
    if len(dbpDBPmod) == 1:
      dbpDBPvec = float(dbpDBPmod[0])
    else:
      dbpDBPvec = None
  if len(mapMAPmod) > 1:
    mapMAPvec = get_number_farthest_from_stdev(mapMAPmod)
  else:
    if len(mapMAPmod) == 1:
      mapMAPvec = float(mapMAPmod[0])
    else:
      mapMAPvec = None
  if len(HRHeartratemod) > 1:
    HRHeartratevec = get_number_farthest_from_stdev(HRHeartratemod)
  else:
    if len(HRHeartratemod) == 1:
      HRHeartratevec = float(HRHeartratemod[0])
    else:
      HRHeartratevec = None
  if len(RRRespmod) > 1:
    RRRespvec = get_number_farthest_from_stdev(RRRespmod)
  else:
    if len(RRRespmod) == 1:
      RRRespvec = float(RRRespmod[0])
    else:
      RRRespvec = None
  if len(O2satSPO2mod) > 1:
    O2satSPO2vec = get_number_farthest_from_stdev(O2satSPO2mod)
  else:
    if len(O2satSPO2mod) == 1:
      O2satSPO2vec = float(O2satSPO2mod[0])
    else:
      O2satSPO2vec = None
  if (len(NaSodiummod) > .1 and len(ClChloridemod) > .1 and len(CO2co2mod) > .1):
    agAG = (NaSodiumvec-ClChloridevec-CO2co2vec)
  else:
    agAG = 10
  if len(aPTTpttmod) > 1:
    aPTTpttvec = get_number_farthest_from_stdev(aPTTpttmod)
  else:
    if len(aPTTpttmod) == 1:
      aPTTpttvec = float(aPTTpttmod[0])
    else:
      aPTTpttvec = 30
  if len(PTptmod) > 1:
    PTptvec = get_number_farthest_from_stdev(PTptmod)
  else:
    if len(PTptmod) == 1:
      PTptvec = float(PTptmod[0])
    else:
      PTptvec = 15
  if len(inrINRmod) > 1:
    inrINRvec = get_number_farthest_from_stdev(inrINRmod)
  else:
    if len(inrINRmod) == 1:
      inrINRvec = float(inrINRmod[0])
    else:
      inrINRvec = 1
else:
  zp=""



#data input display
if len(zp) > 0:
  if Na == None:
    Na = NaSodiumvec
  elif (NaSodiumvec == None and Na == None):
    Na = 140

  if K == None:
    K = KPotassiumvec
  elif (KPotassiumvec == None and K == None):
    K = 4

  if AG == None:
    AG = agAG
  elif (agAG == None and AG == None):
    AG = 10

  if Cr == None:
    Cr = CrCreatininevec
  elif (CrCreatininevec == None and Cr == None):
    Cr = 1

  if Hgb == None:
    Hgb = hgbHGBvec
  elif (hgbHGBvec == None and Hgb == None):
    Hgb = 12

  if Plt == None:
    Plt = pltPLTvec
  elif (pltPLTvec == None and Plt == None):
    Plt = 300

  if SBP == None:
    SBP = sbpSBPvec
  elif (sbpSBPvec == None and SBP == None):
    SBP = 120

  if aPTT == None:
    aPTT = aPTTpttvec
  elif (aPTTpttvec == None and aPTT == None):
    aPTT = 30

  if INR == None:
    INR = inrINRvec
  elif (inrINRvec == None and INR == None):
    INR = 1
else:
  if (Na == None):
    Na = 140

  if K == None:
    K = 4

  if AG == None:
    AG = 10

  if Cr == None:
    Cr = 1

  if Hgb == None:
    Hgb = 12

  if Plt == None:
    Plt = 300

  if SBP == None:
    SBP = 120

  if aPTT == None:
    aPTT = 30

  if INR == None:
    INR = 1
