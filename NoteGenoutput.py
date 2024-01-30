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


#NoteGen Output
output_strings1 = []
output_strings2 = []
output_strings3 = []
output_strings4 = []
output_strings5 = []
output_strings6 = []
output_strings7 = []
output_strings8 = []
output_strings9 = []
output_strings10 = []

#print("#1 Neuro:", end=" ")
if (y_predvented >.4):
    output_strings1.append(f"{Dx57Wk1} {Dx57Tx1}")

if (y_predCVA >.4 and y_predAAA >.4):
    output_strings1.append(f"{Dx69Wk3} {Dx69Tx2}")
elif (y_predCVA >.4 and y_predGI_Bleed >.4):
    output_strings1.append(f"{Dx69Wk3} {Dx69Tx2}")
elif (y_predCVA >.4 and y_predSAH >.4):
    output_strings1.append(f"{Dx69Wk3} {Dx69Tx2}")
elif (y_predCVA >.4 and y_predICH >.4):
    output_strings1.append(f"{Dx69Wk3} {Dx69Tx2}")
elif (y_predCVA >.4 and y_predSDH >.4):
    output_strings1.append(f"{Dx69Wk3} {Dx69Tx2}")
elif (y_predCVA >.4 and y_predBrain_Tumor >.4):
    output_strings1.append(f"{Dx69Wk4} {Dx69Tx2}")
elif (y_predCVA >.4 and coag >.4):
    output_strings1.append(f"{Dx69Wk2} {Dx69Tx2}")
elif (y_predCVA >.4):
    output_strings1.append(f"{Dx69Wk1} {Dx69Tx1}")
elif (yhistCVA >.4):
    output_strings1.append(f"{hist48}")

if (y_predDelirium >.4 and y_predALF >.4):
    output_strings1.append(f"{Dx70Wk1} {Dx70Tx2}")
elif (y_predDelirium >.4):
    output_strings1.append(f"{Dx70Wk1} {Dx70Tx1}")

if data['Na'][0] <= 128:
    output_strings1.append(f"{Dx42Tx2}")

if (y_predEtOH_WD >.4 and y_predvented >.4):
    output_strings1.append(f"{Dx64Wk2} {Dx64Tx2}")
elif (y_predEtOH_WD >.4):
    output_strings1.append(f"{Dx64Wk1}, {Dx64Tx1}")
elif (yhistEtOH_WD >.4):
    output_strings1.append(f"{hist43}")

if (y_predmeningitis_encephalitis >.4 and y_predEndocarditis >.4):
    output_strings1.append(f"{Dx26Wk2} {Dx26Tx1}")
elif (y_predmeningitis_encephalitis >.4 and y_predLupus >.4):
    output_strings1.append(f"{Dx72Wk4} {Dx72Tx3}")
elif (y_predmeningitis_encephalitis >.4):
    output_strings1.append(f"{Dx26Wk1} {Dx26Tx1}")

if (y_predICH >.4 and y_predHTN_Emergency >.4):
    output_strings1.append(f"{Dx28Wk2} {Dx28Tx2}")
elif (y_predICH >.4 and y_predSDH >.4):
    output_strings1.append(f"{Dx28Wk3} {Dx28Tx2}")
elif (y_predICH >.4 and y_predSAH >.4):
    output_strings1.append(f"{Dx28Wk4} {Dx28Tx2}")
elif (y_predICH >.4):
    output_strings1.append(f"{Dx28Wk1} {Dx28Tx1}")
elif (yhistICH >.4):
    output_strings1.append(f"{hist34}")

if (yhistICH >.4 and yhistSeizure >.4):
    output_strings1.append(f"{hist34, hist37, histtx37}")
elif (y_predICH >.4 and y_predSeizure >.4):
    output_strings1.append(f"{Dx28Wk5} {Dx28Tx3}")
elif (y_predSeizure >.4 and y_predLupus >.4):
    output_strings1.append(f"{Dx72Wk6} {Dx72Tx3}, {Dx31Tx1}")
elif (y_predSeizure >.4):
    output_strings1.append(f"{Dx31Wk1} {Dx31Tx1}")
elif (yhistSeizure >.4):
    output_strings1.append(f"{hist37, histtx37}")

if (y_predSDH >.4 and y_predHTN_Emergency >.4):
    output_strings1.append(f"{Dx29Wk2} {Dx29Tx3}")
elif (y_predSDH >.4 and y_predSeizure >.4):
    output_strings1.append(f"{Dx29Wk3} {Dx29Tx2}")
elif (y_predSDH >.4):
    output_strings1.append(f"{Dx29Wk1} {Dx29Tx1}")
elif (yhistSDH >.4):
    output_strings1.append(f"{hist35}")



if (y_predSAH >.4 and y_predSeizure >.4):
    output_strings1.append(f"{Dx30Wk2} {Dx30Tx2}")
elif (y_predSAH >.4):
    output_strings1.append(f"{Dx30Wk1} {Dx30Tx1}")
elif (yhistSAH >.4):
    output_strings1.append(f"{hist36}")

if (y_predTBI >.4):
    output_strings1.append(f"{Dx79Wk1} {Dx79Tx1}")

if (y_predBrain_Tumor >.4 or yhistBrain_Tumor >.4):
    output_strings1.append(f"{Dx82Wk1} {Dx82Tx1}")

if (y_predmeningitis_encephalitis <.4 and y_predDelirium <.4 and data['Na'][0] > 128 and y_predvented <.4 and y_predSDH <.4 and y_predSAH <.4 and y_predICH <.4 and y_predSeizure <.4):
    output_strings1.append(f"{Dx50Tx1}")


#print()
#print("#2 CV:", end=" ")
if (yhistACS >.4):
    output_strings2.append(f"{hist2}")

if (y_predACS >.4 and y_predCardiac_arrest >.4):
    output_strings2.append(f"{Dx5Wk3} {Dx5Tx8}")
elif (y_predACS >.4 and y_predGI_Bleed >.4):
    output_strings2.append(f"{Dx5Wk5} {Dx5Tx9}")
elif (y_predACS >.4 and coag >.4):
    output_strings2.append(f"{Dx5Wk4} {Dx5Tx9}")
elif (y_predACS >.4):
    output_strings2.append(f"{Dx5Wk1} {Dx5Tx1}")
elif ((y_predCAD >.4 or yhistCAD > .4) and Bleed >.4):
    output_strings2.append(f"{Dx65Wk2} {Dx65Tx2}")
elif ((y_predCAD >.4 or yhistCAD > .4) and coag >.4):
    output_strings2.append(f"{Dx65Wk2} {Dx65Tx2}")
elif (y_predCAD >.4 or yhistCAD > .4):
    output_strings2.append(f"{Dx65Wk1} {Dx65Tx1}")


if (y_predAAA >.4 and y_predHypotensionShock >.4):
    output_strings2.append(f"{Dx6Wk5} {Dx6Tx4}")
elif (y_predAAA >.4 and y_predHTN_Emergency >.4):
    output_strings2.append(f"{Dx6Wk4} {Dx6Tx3}")
elif (y_predAAA >.4 and y_predCHF >.4):
    output_strings2.append(f"{Dx6Wk3} {Dx6Tx2}")
elif (y_predAAA >.4 and y_predTachycardia >.4):
    output_strings2.append(f"{Dx6Wk2} {Dx6Tx1}")
elif (yhistAAA >.4):
    output_strings2.append(f"{hist3}")
elif (y_predAAA >.4):
    output_strings2.append(f"{Dx6Wk1} {Dx6Tx1}")

if (y_predTachycardia >.4 and y_predRespiratory_Failure >.4 and y_predHTN_Emergency >.4):
    output_strings2.append(f"{Dx7Wk4} {Dx7Tx3}")
elif (y_predTachycardia >.4 and y_predHypotensionShock >.4 and y_predafib >.4):
    output_strings2.append(f"{Dx7Wk9} {Dx7Tx8}")
elif (y_predTachycardia >.4 and y_predHypotensionShock >.4):
    output_strings2.append(f"{Dx7Wk5} {Dx7Tx4}")
elif (y_predTachycardia >.4 and y_predCHF >.4):
    output_strings2.append(f"{Dx7Wk2} {Dx7Tx2}")
elif (y_predTachycardia >.4 and y_predHTN_Emergency >.4):
    output_strings2.append(f"{Dx7Wk3} {Dx7Tx3}")
elif (y_predTachycardia >.4 and y_predCOPD >.4):
    output_strings2.append(f"{Dx7Wk6} {Dx7Tx5}")
elif (y_predTachycardia >.4 and y_predafib >.4):
    output_strings2.append(f"{Dx7Wk8} {Dx7Tx7}")
elif (y_predTachycardia >.4 and y_predPE >.4):
    output_strings2.append(f"{Dx7Wk7} {Dx7Tx6}")
elif (y_predTachycardia >.4):
    output_strings2.append(f"{Dx7Wk1} {Dx7Tx1}")

if (y_predBradycardia >.4 and y_predHypotensionShock >.4):
    output_strings2.append(f"{Dx8Wk4} {Dx8Tx3}")
elif (y_predBradycardia >.4 and y_predCHF >.4):
    output_strings2.append(f"{Dx8Wk2} {Dx8Tx2}")
elif (y_predBradycardia >.4 and y_predHTN_Emergency >.4):
    output_strings2.append(f"{Dx8Wk3} {Dx8Tx1}")
elif (y_predBradycardia >.4):
    output_strings2.append(f"{Dx8Wk1} {Dx8Tx1}")

if (y_predEtOH_WD >.4):
    output_strings2.append(f"{Dx64Tx3}")

if (y_predCHF >.4 and y_predCardiac_arrest >.4):
    output_strings2.append(f"{Dx9Wk4} {Dx9Tx3}")
elif (y_predCHF >.4 and y_predHypotensionShock >.4):
    output_strings2.append(f"{Dx9Wk3} {Dx9Tx3}")
elif (y_predCHF >.4 and y_predEndocarditis >.4):
    output_strings2.append(f"{Dx9Wk7} {Dx9Tx6}")
elif (y_predCHF >.4 and y_predHTN_Emergency >.4):
    output_strings2.append(f"{Dx9Wk2} {Dx9Tx2}")
elif (y_predCHF >.4 and y_predALF >.4):
    output_strings2.append(f"{Dx9Wk6} {Dx9Tx5}")
elif (y_predCHF >.4 and y_predAKI >.4):
    output_strings2.append(f"{Dx9Wk9} {Dx9Tx8}")
elif (y_predCHF >.4 and y_predSAH >.4):
    output_strings2.append(f"{Dx9Wk8} {Dx9Tx7}")
elif (y_predCHF >.4 and y_predRespiratory_Failure >.4):
    output_strings2.append(f"{Dx9Wk5} {Dx9Tx4}")
elif (y_predCHF >.4):
    output_strings2.append(f"{Dx9Wk1} {Dx9Tx1}")


if (y_predHTN_Emergency >.4 and y_predRespiratory_Failure >.4):
    output_strings2.append(f"{Dx10Wk2} {Dx10Tx2}")
elif (y_predHTN_Emergency >.4 and y_predICH >.4):
    output_strings2.append(f"{Dx10Wk3} {Dx10Tx3}")
elif (y_predHTN_Emergency >.4 and y_predSDH >.4):
    output_strings2.append(f"{Dx10Wk4} {Dx10Tx4}")
elif (y_predHTN_Emergency >.4 and y_predSAH >.4):
    output_strings2.append(f"{Dx10Wk5} {Dx10Tx5}")
elif (y_predHTN_Emergency >.4 and y_predAKI >.4):
    output_strings2.append(f"{Dx10Wk7} {Dx10Tx6}")
elif (y_predHTN_Emergency >.4 and y_predESRD >.4):
    output_strings2.append(f"{Dx10Wk7} {Dx10Tx6}")
elif (y_predHTN_Emergency >.4):
    output_strings2.append(f"{Dx10Wk1} {Dx10Tx1}")
elif (y_predHTN >.4 and y_predHypotensionShock >.4):
    output_strings2.append(f"{Dx62Wk2} {Dx62Tx2}")
elif (y_predHTN >.4 and y_predICH >.4):
    output_strings2.append(f"{Dx62Wk1} {Dx28Tx5}")
elif (y_predICH >.4 or y_predSDH >.4):
    output_strings2.append(f"{Dx28Tx5}")
elif (y_predCVA >.4):
    output_strings2.append(f"{Dx62Tx4}")
elif (y_predHTN >.4 and  data['Systolic'][0] >= 150 and data['Systolic'][0] < 195):
    output_strings2.append(f"{Dx62Wk1} {Dx62Tx3}")
elif (y_predHTN >.4 or yhistHTN):
    output_strings2.append(f"{Dx62Wk1} {Dx62Tx1}")

if (y_predHypotensionShock >.4 and y_predPneumonia >.4):
    output_strings2.append(f"{Dx11Wk2} {Dx11Tx2}")
elif (y_predHypotensionShock >.4 and y_predPneumothorax >.4):
    output_strings2.append(f"{Dx11Wk3} {Dx11Tx3}")
elif (y_predHypotensionShock >.4 and y_predPE >.4):
    output_strings2.append(f"{Dx11Wk4} {Dx11Tx4}")
elif (y_predHypotensionShock >.4 and y_predALF >.4):
    output_strings2.append(f"{Dx11Wk5} {Dx11Tx5}")
elif (y_predHypotensionShock >.4 and y_predGI_Bleed >.4):
    output_strings2.append(f"{Dx11Wk6} {Dx11Tx6}")
elif (y_predHypotensionShock >.4 and y_predColitis >.4):
    output_strings2.append(f"{Dx11Wk7} {Dx11Tx2}")
elif (y_predHypotensionShock >.4 and y_predBacteremia >.4):
    output_strings2.append(f"{Dx11Wk8} {Dx11Tx2}")
elif (y_predHypotensionShock >.4 and y_predmeningitis_encephalitis >.4):
    output_strings2.append(f"{Dx11Wk9} {Dx11Tx2}")
elif (y_predHypotensionShock >.4 and y_predEndocarditis >.4):
    output_strings2.append(f"{Dx11Wk8} {Dx11Tx2}")
elif (y_predHypotensionShock >.4 and y_predUTI >.4):
    output_strings2.append(f"{Dx11Wk9} {Dx11Tx2}")
elif (y_predHypotensionShock >.4 and y_predColitis >.4):
    output_strings2.append(f"{Dx11Wk9} {Dx11Tx2}")
elif (y_predHypotensionShock >.4 and y_predICH >.4):
    output_strings2.append(f"{Dx11Wk8} {Dx11Tx2}")
elif (y_predHypotensionShock >.4):
    output_strings2.append(f"{Dx11Wk1} {Dx11Tx1}")

if (y_predCardiac_arrest >.4 and y_predBradycardia >.4):
    output_strings2.append(f"{Dx12Wk2} {Dx12Tx2}")
elif (y_predCardiac_arrest >.4 and y_predHypotensionShock >.4):
    output_strings2.append(f"{Dx12Wk2} {Dx12Tx2}")
elif (y_predCardiac_arrest >.4):
    output_strings2.append(f"{Dx12Wk1} {Dx12Tx1}")

if (y_predafib >.4 and Bleed >.4):
    output_strings2.append(f"{Dx58Wk2} {Dx58Tx2}")
elif (y_predafib >.4 and coag >.4):
    output_strings2.append(f"{Dx58Wk2} {Dx58Tx2}")
elif (y_predafib >.4):
    output_strings2.append(f"{Dx58Wk1} {Dx58Tx1}")

if (y_predPAD >.4):
    output_strings2.append(f"{Dx81Wk1} {Dx81Tx1}")
if yhistPAD > .4:
    output_strings2.append(f"{hist61}")

if (y_predPericardial_Effusion >.4 and y_predCardiac_arrest >.4):
    output_strings2.append(f"{Dx74Wk3} {Dx74Tx2}")
elif (y_predPericardial_Effusion >.4 and y_predAAA >.4):
    output_strings2.append(f"{Dx74Wk2} {Dx74Tx2}")
elif (y_predPericardial_Effusion >.4 and y_predESRD >.4):
    output_strings2.append(f"{Dx74Wk4} {Dx74Tx2}")
elif (y_predPericardial_Effusion >.4 and y_predLupus >.4):
    output_strings2.append(f"{Dx74Wk5} {Dx74Tx2}")
elif (y_predPericardial_Effusion >.4):
    output_strings2.append(f"{Dx74Wk1} {Dx74Tx1}")

if (y_predACS <.4 and y_predAAA <.4 and data['Systolic'][0] < 150 and y_predCVA <.4 and y_predPericardial_Effusion <.4 and y_predSDH <.4 and y_predCAD <.4 and y_predICH <.4 and y_predTachycardia <.4 and y_predBradycardia <.4 and y_predCHF <.4 and y_predHTN_Emergency <.4 and
    y_predHypotensionShock <.4 and y_predCardiac_arrest <.4 and y_predafib <.4):
    output_strings2.append(f"{Dx46Tx1}")

#print()
#print("#3 Pulm:", end=" ")

if (y_predARDS >.4):
    output_strings3.append(f"{Dx78Wk1} {Dx78Tx1}")
elif (y_predvented >.4 and y_predCHF >.4):
    output_strings3.append(f"{Dx57Wk2} {Dx57Tx2}")
elif (y_predvented >.4 and y_predHTN_Emergency >.4):
    output_strings3.append(f"{Dx57Wk2} {Dx57Tx2}")
elif (y_predvented >.4 and y_predCardiac_arrest >.4):
    output_strings3.append(f"{Dx57Wk3} {Dx57Tx1}")
elif (y_predvented >.4):
    output_strings3.append(f"{Dx57Wk1} {Dx57Tx1}")

if (y_predAirway_Obstruction >.4):
    output_strings3.append(f"{Dx13Wk1} {Dx13Tx1}")

if (y_predvented >.4 or yhisttrach >.4) and (y_predCOPD >.4 and y_predPneumonia >.4 and y_predRespiratory_Failure >.4):
    output_strings3.append(f"{Dx57Wk4} {Dx57Tx5}")
elif (y_predvented >.4 or yhisttrach >.4) and (y_predCOPD >.4 and y_predPneumonia >.4):
    output_strings3.append(f"{Dx57Wk4} {Dx57Tx5}")
elif (y_predCOPD >.4 and y_predPneumonia >.4 and y_predRespiratory_Failure >.4):
    output_strings3.append(f"{Dx57Wk6} {Dx57Tx6}")
elif (y_predvented >.4 or yhisttrach >.4) and (y_predPneumonia >.4):
    output_strings3.append(f"{Dx57Wk5} {Dx57Tx4}")
elif (y_predRespiratory_Failure >.4 and y_predPneumonia >.4):
    output_strings3.append(f"{Dx17Wk4} {Dx17Tx4}")
elif (y_predCOPD >.4) and (y_predvented >.4 or yhisttrach >.4):
    output_strings3.append(f"{Dx14Wk7} {Dx14Tx6}")
elif (y_predCOPD >.4 and y_predRespiratory_Failure >.4):
    output_strings3.append(f"{Dx14Wk6} {Dx14Tx5}")
elif (y_predCOPD >.4 and y_predPneumonia >.4):
    output_strings3.append(f"{Dx14Wk4} {Dx14Tx3}")
elif (y_predCOPD >.4):
    output_strings3.append(f"{Dx14Wk1} {Dx14Tx1}")
elif (yhistCOPD >.4):
    output_strings3.append(f"{hist12} {histtx12}")
elif (y_predPneumonia >.4):
    output_strings3.append(f"{Dx15Wk1}")

if yhisttrach >.4:
    output_strings3.append(f"{hist75} {histtx75}")

if (y_predCOPD >.4 and y_predPneumothorax >.4):
    output_strings3.append(f"{Dx14Wk5} {Dx14Tx4}")
elif (y_predCOPD >.4 and y_predTachycardia >.4):
    output_strings3.append(f"{Dx14Wk3} {Dx14Tx1}")
elif (y_predCOPD >.4 and y_predACS >.4):
    output_strings3.append(f"{Dx14Wk2} {Dx14Tx2}")


if (y_predAsthma >.4 and y_predRespiratory_Failure >.4):
    output_strings3.append(f"{Dx63Wk2} {Dx63Tx2}")
elif (y_predAsthma >.4 and y_predvented >.4):
    output_strings3.append(f"{Dx63Wk2} {Dx63Tx2}")
elif (y_predAsthma >.4):
    output_strings3.append(f"{Dx63Wk1} {Dx63Tx1}")
elif (yhistAsthma >.4):
    output_strings3.append(f"{hist41} {histtx41}")

if (y_predPneumothorax >.4):
    output_strings3.append(f"{Dx16Wk1} {Dx16Tx1}")
elif yhistPneumothorax >.4:
    output_strings3.append(f"{hist13}")

if (y_predRespiratory_Failure >.4 and y_predHypotensionShock >.4):
    output_strings3.append(f"{Dx17Wk2} {Dx17Tx2}")
elif (y_predRespiratory_Failure >.4 and y_predPneumothorax >.4):
    output_strings3.append(f"{Dx17Wk5} {Dx17Tx5}")
elif (y_predRespiratory_Failure >.4 and y_predALF >.4):
    output_strings3.append(f"{Dx17Wk7} {Dx17Tx7}")
elif (y_predRespiratory_Failure >.4 and y_predmeningitis_encephalitis >.4):
    output_strings3.append(f"{Dx17Wk8} {Dx17Tx8}")
elif (y_predRespiratory_Failure >.4 and y_predICH >.4):
    output_strings3.append(f"{Dx17Wk8} {Dx17Tx8}")
elif (y_predRespiratory_Failure >.4 and y_predSDH >.4):
    output_strings3.append(f"{Dx17Wk8} {Dx17Tx8}")
elif (y_predRespiratory_Failure >.4 and y_predSAH >.4):
    output_strings3.append(f"{Dx17Wk8} {Dx17Tx8}")
elif (y_predRespiratory_Failure >.4 and y_predSeizure >.4):
    output_strings3.append(f"{Dx17Wk8} {Dx17Tx8}")
elif (y_predRespiratory_Failure >.4):
    output_strings3.append(f"{Dx17Wk1} {Dx17Tx1}")

if (y_predPE >.4 and y_predGI_Bleed >.4):
    output_strings3.append(f"{Dx18Wk3} {Dx18Tx2}")
elif (y_predPE >.4 and y_predICH >.4):
    output_strings3.append(f"{Dx18Wk3} {Dx18Tx2}")
elif (y_predPE >.4 and y_predSDH >.4):
    output_strings3.append(f"{Dx18Wk3} {Dx18Tx2}")
elif (y_predPE >.4 and y_predSAH >.4):
    output_strings3.append(f"{Dx18Wk3} {Dx18Tx2}")
elif (y_predPE >.4 and coag >.4):
    output_strings3.append(f"{Dx18Wk2} {Dx18Tx2}")
elif (y_predPE >.4):
    output_strings3.append(f"{Dx18Wk1} {Dx18Tx1}")
elif (yhistPE > .4):
    output_strings3.append(f"{hist33}")

if (y_predOSA >.4 and y_predvented <.5):
    output_strings3.append(f"{Dx66Wk1} {Dx66Tx1}")

if (y_predAirway_Obstruction >.4 or y_predPE >.4 or y_predCOPD >.4 or y_predPneumonia >.4 or y_predPneumothorax >.4 or y_predvented >.4 or y_predRespiratory_Failure >.4):
    print()
else: output_strings3.append(f"{Dx47Tx1}")

#print()
#print("#4 GI:", end=" ")

if (y_predALF >.4):
      output_strings4.append(f"{Dx19Wk1} {Dx19Tx1}")
elif (yhistALF >.4):
      output_strings4.append(f"{hist15} {histtx15}")

if (y_predGI_Bleed >.4 and  y_predALF >.4):
      output_strings4.append(f"{Dx20Wk2} {Dx20Tx2}")
elif (y_predGI_Bleed >.4 and  y_predACS >.4):
      output_strings4.append(f"{Dx20Wk3} {Dx20Tx2}")
elif (y_predGI_Bleed >.4):
      output_strings4.append(f"{Dx20Wk1} {Dx20Tx1}")

if (y_predacutePancreatitis >.4):
      output_strings4.append(f"{Dx21Wk1} {Dx21Tx1}")
elif (yhistPancreatitis >.4):
      output_strings4.append(f"{hist17}")

if (y_predColitis >.4):
      output_strings4.append(f"{Dx22Wk1} {Dx22Tx1}")
elif (yhistColitis >.4):
      output_strings4.append(f"{hist18}")

if (y_predGastroenteritis >.4):
      output_strings4.append(f"{Dx23Wk1} {Dx23Tx1}")

if (y_predGERD >.4):
      output_strings4.append(f"{Dx83Wk1} {Dx83Tx1}")

if (y_predGI_Bleed >.4 or y_predacutePancreatitis >.4 or y_predALF >.4 or y_predColitis >.4 or y_predGastroenteritis >.4):
      print()
elif (NPO >.4):
      output_strings4.append(f"{Dx48Tx2}")
else: output_strings4.append(f"{Dx48Tx1}")

#print()
#print("#5 Renal:", end=" ")

if (data['AG'][0] >= 16 and y_predDKA >.4):
    output_strings5.append(f"{Dx59Wk2} {Dx59Tx2}")
elif (data['AG'][0] >= 16):
    output_strings5.append(f"{Dx59Wk1} {Dx59Tx1}")

if (y_predESRD >.4 and data['Cr'][0] >= 2):
    output_strings5.append(f"{Dx60Wk1} {Dx60Tx1}")
elif (y_predCKD >.4 and data['Cr'][0] >= 1.4):
    output_strings5.append(f"{Dx61Wk1} {Dx61Tx1}")
elif (y_predAKI >.4 and data['Cr'][0] >= 1.4):
    output_strings5.append(f"{Dx37Wk1} {Dx37Tx1}")

if data['Na'][0] >= 150:
    output_strings5.append(f"{Dx41Wk1} {Dx41Tx1}")

if data['Na'][0] <= 130:
    output_strings5.append(f"{Dx42Wk1} {Dx42Tx1}")

if data['K'][0] >= 5.8:
    output_strings5.append(f"{Dx43Wk1} {Dx43Tx1}")

if data['K'][0] <= 3.4:
    output_strings5.append(f"{Dx44Wk1} {Dx44Tx1}")

if (data['Na'][0] <= 150 and data['Na'][0] >= 130 and data['K'][0] <= 5.8 and data['K'][0] >= 3.4 and y_predESRD <.4 and y_predCKD <.4 and y_predAKI <.4):
    output_strings5.append(f"{Dx49Tx1}")

#print()
#print("#6 ID:", end=" ")

if (y_predBacteremia >.4 and y_predPneumonia >.4):
    output_strings6.append(f"{Dx25Wk2} {Dx25Tx1}")
elif (y_predBacteremia >.4 and y_predALF >.4):
    output_strings6.append(f"{Dx25Wk3} {Dx25Tx1}")
elif (y_predBacteremia >.4 and y_predacutePancreatitis >.4):
    output_strings6.append(f"{Dx25Wk4} {Dx25Tx2}")
elif (y_predBacteremia >.4 and y_predColitis >.4):
    output_strings6.append(f"{Dx25Wk4} {Dx25Tx2}")
elif (y_predBacteremia >.4 and y_predGastroenteritis >.4):
    output_strings6.append(f"{Dx25Wk4} {Dx25Tx2}")
elif (y_predBacteremia >.4 and y_predmeningitis_encephalitis >.4):
    output_strings6.append(f"{Dx25Wk5} {Dx25Tx3}")
elif (y_predBacteremia >.4 and y_predEndocarditis >.4):
    output_strings6.append(f"{Dx25Wk6} {Dx25Tx1}")
elif (y_predBacteremia >.4 and y_predUTI >.4):
    output_strings6.append(f"{Dx25Wk7} {Dx25Tx1}")
elif (y_predBacteremia >.4):
    output_strings6.append(f"{Dx25Wk1} {Dx25Tx1}")

if (y_predEndocarditis >.4):
    output_strings6.append(f"{Dx27Wk1} {Dx27Tx1}")
elif (yhistEndocarditis >.4):
    output_strings6.append(f"{hist21}")

if (y_predmeningitis_encephalitis >.4 and y_predEndocarditis >.4):
    output_strings6.append(f"{Dx26Wk2} {Dx26Tx1}")
elif (y_predmeningitis_encephalitis >.4):
    output_strings6.append(f"{Dx26Wk1}, {Dx26Tx1}")

if (y_predPneumonia >.4 and y_predALF >.4):
    output_strings6.append(f"{Dx15Wk2} {Dx15Tx1}")
elif (y_predPneumonia >.4 and y_predEndocarditis >.4):
    output_strings6.append(f"{Dx15Wk5} {Dx15Tx2}")
elif (y_predPneumonia >.4 and y_predBacteremia >.4):
    output_strings6.append(f"{Dx15Wk4} {Dx15Tx2}")
elif (y_predPneumonia >.4):
    output_strings6.append(f"{Dx15Wk1} {Dx15Tx1}")

if (y_predUTI >.4):
    output_strings6.append(f"{Dx33Wk1} {Dx33Tx1}")
elif (yhistUTI >.4):
    output_strings6.append(f"{hist22}")

if (y_predCellulitis >.4) and (y_predHypotensionShock > .4 or y_predDelirium >.4):
    output_strings6.append(f"{Dx34Wk2} {Dx34Tx2}")
elif (y_predCellulitis >.4):
    output_strings6.append(f"{Dx34Wk1} {Dx34Tx1}")

if (y_predCholecystitis >.4):
    output_strings6.append(f"{Dx75Wk1} {Dx75Tx1}")

if (y_predBacteremia >.4 or y_predCellulitis >.4 or y_predmeningitis_encephalitis >.4 or y_predPneumonia >.4 or y_predEndocarditis >.4 or y_predUTI >.4):
  print(" ")
else: output_strings6.append(f"{Dx53Tx1}")

#print("#7 Endo:", end=" ")

#Workup
if (y_predDKA >.4 and data['AG'][0] >= 16):
    output_strings7.append(f"{Dx38Wk1} {Dx38Tx1}")
elif (y_predDM >.4):
    output_strings7.append(f"{Dx36Wk1} {Dx36Tx1}")
elif (y_predDKA >.4):
    output_strings7.append(f"{Dx36Wk1} {Dx36Tx1}")
else:
    output_strings7.append(f"{Dx52Tx1}")

if (y_predDLD >=.4):
    output_strings7.append(f"{Dx71Wk1} {Dx71Tx1}")

if (y_predhypothyroid >.4):
    output_strings7.append(f"{Dx67Wk1} {Dx67Tx1}")
elif (y_predhyperthyroid >.4):
    output_strings7.append(f"{Dx68Wk1} {Dx68Tx1}")

if (y_predAI >.4):
    output_strings7.append(f"{Dx76Wk1} {Dx76Tx1}")
elif (y_predCushing >.4):
    output_strings7.append(f"{Dx77Wk1} {Dx77Tx1}")


#print()
#print("#8 Heme/Onc:", end=" ")

#workup
if data['Hgb'][0] <= 9:
    output_strings8.append(f"{Dx39Wk1} {Dx39Tx1}")
if (data['Hgb'][0] > 9):
    output_strings8.append(f"{Dx51Tx1}")

if (data['AG'][0] < 0):
    output_strings8.append(f"{Dx59Wk3} {Dx59Tx3}")

if (data['AG'][0] > 16 and y_predDKA < .4):
    output_strings8.append(f"{Dx59Wk1} {Dx59Tx1}")

if (coag >.4 and Bleed >.4):
    output_strings8.append(f"{Dx45Wk2} {Dx45Tx2}")
elif (coag >.4):
    output_strings8.append(f"{Dx45Wk1} {Dx45Tx1}")

if (y_predLupus >.4 and y_predRespiratory_Failure >.4):
    output_strings8.append(f"{Dx72Wk3} {Dx72Tx2}")
elif (y_predLupus >.4 and y_predHTN_Emergency >.4):
    output_strings8.append(f"{Dx72Wk2} {Dx72Tx2}")
elif (y_predLupus >.4 and y_predAKI >.4):
    output_strings8.append(f"{Dx72Wk5} {Dx72Tx4}")
elif (y_predLupus >.4 and y_predCKD >.4):
    output_strings8.append(f"{Dx72Wk5} {Dx72Tx4}")
elif (y_predLupus >.4 and y_predESRD >.4):
    output_strings8.append(f"{Dx72Wk5} {Dx72Tx4}")
elif (y_predLupus >.4 and y_predmeningitis_encephalitis >.4):
    output_strings8.append(f"{Dx72Wk4} {Dx72Tx3}")
elif (y_predLupus >.4):
    output_strings8.append(f"{Dx72Wk1} {Dx72Tx1}")

if (y_predScleroderma >.4):
    output_strings8.append(f"{Dx73Wk1} {Dx73Tx1}")

if (y_predBurn >.4):
    output_strings8.append(f"{Dx80Wk1} {Dx80Tx1}")

#print()
#print("#9 PPx:", end=" ")
if (SUP <.4 and chemDVT <.4 and mechDVT <.4 and y_predALF <.4 and data['INR'][0] > 2):
     output_strings9.append(f"INR elevated, DVT Prophylaxis.")
elif (SUP >.4 and chemDVT <.4 and mechDVT <.4 and y_predALF <.4 and data['INR'][0] > 2):
    output_strings9.append(f"INR elevated, DVT Prophylaxis. Continue PPI or H2 blocker")
elif (SUP <.4 and chemDVT <.4 and mechDVT <.4):
    output_strings9.append(f"{Dx54Tx1}")
elif (SUP >.4 and chemDVT <.4 and mechDVT <.4):
    output_strings9.append(f"{Dx54Tx2}")
elif (SUP >.4 and chemDVT <.4 and mechDVT >.4):
    output_strings9.append(f"{Dx54Tx3}")
elif (SUP <.4 and chemDVT <.4 and mechDVT >.4):
    output_strings9.append(f"{Dx54Tx4}")
elif (SUP >.4 and chemDVT >.4):
    output_strings9.append(f"{Dx54Tx5}")
elif (SUP <.4 and chemDVT >.4):
    output_strings9.append(f"{Dx54Tx6}")

result_string1 = "\n".join(output_strings1)
result_string2 = "\n".join(output_strings2)
result_string3 = "\n".join(output_strings3)
result_string4 = "\n".join(output_strings4)
result_string5 = "\n".join(output_strings5)
result_string6 = "\n".join(output_strings6)
result_string7 = "\n".join(output_strings7)
result_string8 = "\n".join(output_strings8)
result_string9 = "\n".join(output_strings9)
output_strings10.append(f"{'#1 Neuro:'} {result_string1}\n\n")
output_strings10.append(f"{'#2 CV:'} {result_string2}\n\n")
output_strings10.append(f"{'#3 Pulm:'} {result_string3}\n\n")
output_strings10.append(f"{'#4 GI:'} {result_string4}\n\n")
output_strings10.append(f"{'#5 Renal:'} {result_string5}\n\n")
output_strings10.append(f"{'#6 ID:'} {result_string6}\n\n")
output_strings10.append(f"{'#7 Endo:'} {result_string7}\n\n")
output_strings10.append(f"{'#8 Heme/Onc:'} {result_string8}\n\n")
output_strings10.append(f"{'#9 PPx:'} {result_string9}\n\n")
result_string10 = " ".join(output_strings10)