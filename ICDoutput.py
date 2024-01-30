
output_strings12 = []
output_strings13 = []
output_strings14 = []

if (y_predmeningitis_encephalitis >.4 or yhistmeningitis_encephalitis >.4):
    output_strings12.append(f"meningitis/encephalitis G03.9/G04.90")
if (y_predACS >.4 or yhistACS >.4):
    output_strings12.append(f"ACS I24.9")
if (y_predAAA >.4 or yhistAAA >.4):
    output_strings12.append(f"AAA I71.4")
if (y_predTachycardia >.4 or yhistTachycardia >.4):
     output_strings12.append(f"Tachycardia R00.0")
if (y_predBradycardia >.4 or yhistBradycardia >.4):
    output_strings12.append(f"Bradycardia R00.1")
if (y_predCHF >.4 or yhistCHF >.4):
    output_strings12.append(f"CHF I50.9")
if (y_predHTN_Emergency >.4 or yhistHTN_Emergency >.4):
    output_strings12.append(f"HTN Emergency I16.1" "HTN I10")
if (y_predHypotensionShock >.4 or yhistHypotensionShock >.4):
    output_strings12.append(f"Hypotension I95.9 Shock R57.0")
if (y_predCardiac_arrest >.4 or yhistCardiac_arrest >.4):
    output_strings12.append(f"Cardiac arrest I46.9")
if (y_predAirway_Obstruction >.4 or yhistAirway_Obstruction >.4):
    output_strings12.append(f"Airway_Obstruction J98.8")
if (y_predPneumonia >.4 or yhistPneumonia >.4):
    output_strings12.append(f"Pneumonia J18.9, Sepsis A41.9")
if (y_predCOPD >.4 or yhistCOPD >.4):
    output_strings12.append(f"COPD J44.9")
if (y_predPneumothorax >.4 or yhistPneumothorax >.4):
    output_strings12.append(f"Pneumothorax J93.9")
if (y_predRespiratory_Failure >.4 or yhistRespiratory_Failure >.4):
    output_strings12.append(f"Respiratory Failure J96")
if (y_predALF >.4 or yhistALF >.4):
    output_strings12.append(f"ALF K72.00 Cirrhosis K74.60")
if (y_predGI_Bleed >.4 or yhistGI_Bleed >.4):
    output_strings12.append(f"GI Bleed K92.2")
if (y_predacutePancreatitis >.4 or yhistPancreatitis >.4):
    output_strings12.append(f"Pancreatitis K85.90")
if (y_predColitis >.4 or yhistColitis >.4):
    output_strings12.append(f"Colitis K52.9", "Sepsis A41.9")
if (y_predGastroenteritis >.4 or yhistGastroenteritis >.4):
    output_strings12.append(f"Gastroenteritis K52.9")
if (y_predBacteremia >.4 or yhistBacteremia >.4):
    output_strings12.append(f"Bacteremia R78.81", "Sepsis A41.9")
if (y_predEndocarditis >.4 or yhistEndocarditis >.4):
    output_strings12.append(f"Endocarditis I38", "Sepsis A41.9")
if (y_predUTI >.4 or yhistUTI >.4):
    output_strings12.append(f"UTI N39.0 Sepsis A41.9")
if (y_predvented >.4 or yhistvented >.4):
    output_strings12.append(f"vented ARF J96")
if (y_predafib >.4 or yhistafib >.4):
    output_strings12.append(f"Atrial fibrillation I48.0")
if (y_predDM >.4 or yhistDM >.4):
    output_strings12.append(f"DM E11.8")
if (y_predDKA >.4):
    output_strings12.append(f"DM E11.8" "Acidosis E87.2" "DKA E11.10")
if (y_predPE >.4 or yhistPE >.4):
    output_strings12.append(f"PE I26.99")
if (y_predICH >.4 or yhistICH >.4):
    output_strings12.append(f"ICH I62.9")
if (y_predSDH >.4 or yhistSDH >.4):
    output_strings12.append(f"SDH S06.5X9A")
if (y_predSAH >.4 or yhistSAH >.4):
    output_strings12.append(f"SAH I60.9")
if (y_predSeizure >.4 or yhistSeizure >.4):
    output_strings12.append(f"Seizures R56.9")
if (y_predESRD >.4 or yhistESRD >.4):
    output_strings12.append(f"ESRD N18.6")
if (y_predCKD >.4 or yhistCKD >.4):
    output_strings12.append(f"CKD N18.9")
if (y_predAKI >.4 or yhistAKI >.4):
    output_strings12.append(f"AKI N17.9")
if (y_predAsthma >.4 or yhistAsthma >.4):
    output_strings12.append(f"Asthma J45.909")
if (y_predHTN >.4 or yhistHTN >.4) or (y_predHTN >.4 or data['Systolic'][0] > 139):
    output_strings12.append(f"HTN I10")
if (y_predEtOH_WD >.4 or yhistEtOH_WD >.4):
    output_strings12.append(f"EtOH Withdrawal F10.20")
if (y_predCAD >.4 or yhistCAD >.4):
    output_strings12.append(f"CAD I25.10")
if (y_predOSA >.4 or yhistOSA >.4):
    output_strings12.append(f"OSA G47.33")
if (y_predhypothyroid >.4 or yhisthypothyroid >.4):
    output_strings12.append(f"Hypothyroid E03.9")
if (y_predhyperthyroid >.4 or yhisthyperthyroid >.4):
    output_strings12.append(f"Hyperthyroid E05.90")
if (y_predCVA >.4 or yhistCVA >.4):
    output_strings12.append(f"CVA I63.9")
if (y_predDelirium >.4 or yhistDelirium >.4):
    output_strings12.append(f"Delirium R41.0")
if (y_predDLD >.4 or yhistDLD >.4):
    output_strings12.append(f"HLD E78.5")
if (y_predAI >.4 or yhistAI >.4):
    output_strings12.append(f"Adrenal Insufficiency E27.1")
if (y_predLupus >.4 or yhistLupus >.4):
    output_strings12.append(f"Lupus M32.9")
if (y_predCushing >.4 or yhistCushing >.4):
    output_strings12.append(f"Cushings Disease E24.0")
if (y_predScleroderma >.4 or yhistScleroderma >.4):
    output_strings12.append(f"Scleroderma M34.9")
if (y_predPericardial_Effusion >.4 or yhistPericardial_Effusion >.4):
    output_strings12.append(f"Pericardial Effusion I31.39")
if (y_predCholecystitis >.4 or yhistCholecystitis >.4):
    output_strings12.append(f"Cholecystitis  K81.9")
if (y_predARDS >.4 or yhistARDS >.4):
    output_strings12.append(f"ARDS J80")
if (y_predCellulitis >.4 or yhistCellulitis >.4):
    output_strings12.append(f"Cellulitis L03.90 Sepsis A41.9")
if (y_predTBI >.4 or yhistTBI >.4):
    output_strings12.append(f"TBI/Head Trauma S06.9XAA S09.90XA")
if (y_predBurn >.4 or yhistBurn >.4):
    output_strings12.append(f"Burn T30.0")
if (y_predPAD >.4 or yhistPAD >.4):
    output_strings12.append(f"PAD I73.9")
if (y_predBrain_Tumor >.4 or yhistBrain_Tumor >.4):
    output_strings12.append(f"Brain Tumor D49.6")
if (y_predGERD >.4 or yhistGERD >.4):
    output_strings12.append(f"GERD K21.9")
if data['Na'][0] >= 150:
    output_strings12.append(f"Hypernatremia E87.0")
if data['Na'][0] <= 130:
    output_strings12.append(f"Hyponatremia E87.1")
if data['K'][0] >= 5.8:
    output_strings12.append(f"Hyperkalemia E87.5")
if data['K'][0] <= 3.4:
    output_strings12.append(f"Hypokalemia E87.6")
if data['Hgb'][0] <= 10:
    output_strings12.append(f"Anemia D64.9")
if data['AG'][0] >= 16:
    output_strings12.append(f"Anion Gap Acidosis E87.2")
if (y_predCoagulopathy >.4):
    output_strings12.append(f"Coagulopathy I73.9")
if (data['Plt'][0] < 100):
    output_strings12.append(f"Thrombocytopenia D69.6")
#if (y_predxgbpreopUEAngio >.4):
 #   output_strings12.append(f"Peripheral Angiopathy I73.9")
#if y_predxgbpreopImpella > .4:
 #   output_strings12.append(f"Cardiogenic Shock R57.0")
#if y_predxgbpreopCraniotomy > .4:
 #   output_strings12.append(f"S/P Craniotomy Z98.890")
#if y_predxgbpreopCath > .4:
 #   output_strings12.append(f"ACS I24.9")
#if y_predxgbpreopCABG > .4:
 #   output_strings12.append(f"CAD I25.10")
#if y_predxgbpreopAVR > .4:
 #   output_strings12.append(f"S/P AVR Z95.2")
#if y_predxgbpreopAngiogram > .4:
 #   output_strings12.append(f"S/P Angiogram Z98.890")
#if y_predxgbpreopAAA > .4:
    #output_strings12.append(f"EVAR Z86.79")

if (y_predmeningitis_encephalitis >.4):
    output_strings13.append(f"meningitis/encephalitis G03.9/G04.90")
if (y_predACS >.4):
    output_strings13.append(f"ACS I24.9")
if (y_predAAA >.4):
    output_strings13.append(f"AAA I71.4")
if (y_predTachycardia >.4):
     output_strings13.append(f"Tachycardia R00.0")
if (y_predBradycardia >.4):
    output_strings13.append(f"Bradycardia R00.1")
if (y_predCHF >.4):
    output_strings13.append(f"CHF I50.9")
if (y_predHTN_Emergency >.4):
    output_strings13.append(f"HTN Emergency I16.1 HTN I10")
if (y_predHypotensionShock >.4):
    output_strings13.append(f"Hypotension I95.9 Shock R57.0")
if (y_predCardiac_arrest >.4):
    output_strings13.append(f"Cardiac arrest I46.9")
if (y_predAirway_Obstruction >.4):
    output_strings13.append(f"Airway_Obstruction J98.8")
if (y_predPneumonia >.4):
    output_strings13.append(f"Pneumonia J18.9, Sepsis A41.9")
if (y_predCOPD >.4):
    output_strings13.append(f"COPD J44.9")
if (y_predPneumothorax >.4):
    output_strings13.append(f"Pneumothorax J93.9")
if (y_predRespiratory_Failure >.4):
    output_strings13.append(f"Respiratory Failure J96")
if (y_predALF >.4):
    output_strings13.append(f"ALF K72.00 Cirrhosis K74.60")
if (y_predGI_Bleed >.4):
    output_strings13.append(f"GI Bleed K92.2")
if (y_predacutePancreatitis >.4):
    output_strings13.append(f"Pancreatitis K85.90")
if (y_predColitis >.4):
    output_strings13.append(f"Colitis K52.9", "Sepsis A41.9")
if (y_predGastroenteritis >.4):
    output_strings13.append(f"Gastroenteritis K52.9")
if (y_predBacteremia >.4):
    output_strings13.append(f"Bacteremia R78.81", "Sepsis A41.9")
if (y_predEndocarditis >.4):
    output_strings13.append(f"Endocarditis I38", "Sepsis A41.9")
if (y_predUTI >.4):
    output_strings13.append(f"UTI N39.0 Sepsis A41.9")
if (y_predvented >.4):
    output_strings13.append(f"vented ARF J96")
if (afib >.4):
    output_strings13.append(f"Atrial fibrillation I48.0")
if data['Na'][0] >= 150:
    output_strings13.append(f"Hypernatremia E87.0")
if data['Na'][0] <= 130:
    output_strings13.append(f"Hyponatremia E87.1")
if data['K'][0] >= 5.8:
    output_strings13.append(f"Hyperkalemia E87.5")
if data['K'][0] <= 3.4:
    output_strings13.append(f"Hypokalemia E87.6")
if data['Hgb'][0] <= 10:
    output_strings13.append(f"Anemia D64.9")
if (y_predDM >.4):
    output_strings13.append(f"DM E11.8")
if (y_predDKA >.4):
    output_strings13.append(f"DM E11.8 Acidosis E87.2 DKA E11.10")
if data['AG'][0] >= 16:
    output_strings13.append(f"Anion Gap Acidosis E87.2")
if (y_predPE >.4):
    output_strings13.append(f"PE I26.99")
if (y_predICH >.4):
    output_strings13.append(f"ICH I62.9")
if (y_predSDH >.4):
    output_strings13.append(f"SDH S06.5X9A")
if (y_predSAH >.4):
    output_strings13.append(f"SAH I60.9")
if (y_predSeizure >.4):
    output_strings13.append(f"Seizures R56.9")
if (y_predESRD >.4 and data['Cr'][0] >= 2):
    output_strings13.append(f"ESRD N18.6")
if (y_predCKD >.4 and data['Cr'][0] >= 1.4):
    output_strings13.append(f"CKD N18.9")
if (y_predAKI >.4 and data['Cr'][0] >= 1.4):
    output_strings13.append(f"AKI N17.9")
if (y_predAsthma >.4):
    output_strings13.append(f"Asthma J45.909")
if (y_predHTN >.4 and data['Systolic'][0] > 140):
    output_strings13.append(f"HTN I10")
if (y_predEtOH_WD >.4):
    output_strings13.append(f"EtOH Withdrawal F10.20")
if (y_predCAD >.4):
    output_strings13.append(f"CAD I25.10")
if (y_predOSA >.4):
    output_strings13.append(f"OSA G47.33")
if (y_predhypothyroid >.4):
    output_strings13.append(f"Hypothyroid E03.9")
if (y_predhyperthyroid >.4):
    output_strings13.append(f"Hyperthyroid E05.90")
if (y_predCVA >.4):
    output_strings13.append(f"CVA I63.9")
if (y_predDelirium >.4):
    output_strings13.append(f"Delirium R41.0")
if (y_predDLD >.4):
    output_strings13.append(f"HLD E78.5")
if (y_predAI >.4):
    output_strings13.append(f"Adrenal Insufficiency E27.1")
if (y_predLupus >.4):
    output_strings13.append(f"Lupus M32.9")
if (y_predCushing >.4):
    output_strings13.append(f"Cushings Disease E24.0")
if (y_predScleroderma >.4):
    output_strings13.append(f"Scleroderma M34.9")
if (y_predPericardial_Effusion >.4):
    output_strings13.append(f"Pericardial Effusion I31.39")
if (y_predCholecystitis >.4):
    output_strings13.append(f"Cholecystitis    K81.9")
if (y_predARDS >.4):
    output_strings13.append(f"ARDS J80")
if (y_predCellulitis >.4):
    output_strings13.append(f"Cellulitis   L03.90 Sepsis A41.9")
if (y_predTBI >.4):
    output_strings13.append(f"TBI/Head Trauma S06.9XAA S09.90XA")
if (y_predBurn >.4):
    output_strings13.append(f"Burn T30.0")
if (y_predPAD >.4):
    output_strings13.append(f"PAD I73.9")
if (y_predBrain_Tumor >.4):
    output_strings13.append(f"Brain Tumor D49.6")
if (y_predCoagulopathy >.4):
    output_strings13.append(f"Coagulopathy I73.9")
if (data['Plt'][0] < 100):
    output_strings13.append(f"Thrombocytopenia D69.6")
if (y_predGERD >.4):
    output_strings13.append(f"GERD K21.9")
#if (y_predxgbpreopUEAngio >.4):
    #output_strings13.append(f"Peripheral Angiopathy I73.9")
#if y_predxgbpreopImpella > .4:
    #output_strings13.append(f"Cardiogenic Shock R57.0")
#if y_predxgbpreopCraniotomy > .4:
    #output_strings13.append(f"S/P Craniotomy Z98.890")
#if y_predxgbpreopCath > .4:
    #output_strings13.append(f"ACS I24.9")
##if y_predxgbpreopCABG > .4:
   # output_strings13.append(f"CAD I25.10")
#if y_predxgbpreopAVR > .4:
   # output_strings13.append(f"S/P AVR Z95.2")
#if y_predxgbpreopAngiogram > .4:
   #output_strings13.append(f"S/P Angiogram Z98.890")
#if y_predxgbpreopAAA > .4:
   # output_strings13.append(f"EVAR Z86.79")

if (y_predmeningitis_encephalitis <.4 and yhistmeningitis_encephalitis >.4):
    output_strings14.append(f"meningitis/encephalitis G03.9/G04.90")
if (y_predACS <.4 and yhistACS >.4):
    output_strings14.append(f"ACS I24.9")
if (yhistAAA >.4):
    output_strings14.append(f"AAA I71.4")
if (y_predTachycardia <.4 and yhistTachycardia >.4):
     output_strings14.append(f"Tachycardia R00.0")
if (y_predBradycardia <.4 and yhistBradycardia >.4):
    output_strings14.append(f"Bradycardia R00.1")
if (y_predCHF <.4 and yhistCHF >.4):
    output_strings14.append(f"CHF I50.9")
if (y_predHTN_Emergency <.4 and yhistHTN_Emergency >.4):
    output_strings14.append(f"HTN Emergency I16.1", "HTN I10")
if (y_predHypotensionShock <.4 and yhistHypotensionShock >.4):
    output_strings14.append(f"Hypotension I95.9 Shock R57.0")
if (y_predCardiac_arrest <.4 and yhistCardiac_arrest >.4):
    output_strings14.append(f"Cardiac arrest I46.9")
if (y_predAirway_Obstruction <.4 and yhistAirway_Obstruction >.4):
    output_strings14.append(f"Airway_Obstruction J98.8")
if (y_predPneumonia <.4 and yhistPneumonia >.4):
    output_strings14.append(f"Pneumonia J18.9", "Sepsis A41.9")
if (y_predCOPD <.4 and yhistCOPD >.4):
    output_strings14.append(f"COPD J44.9")
if (y_predPneumothorax <.4 and yhistPneumothorax >.4):
    output_strings14.append(f"Pneumothorax J93.9")
if (y_predRespiratory_Failure <.4 and yhistRespiratory_Failure >.4):
    output_strings14.append(f"Respiratory Failure J96")
if (y_predALF <.4 and yhistALF >.4):
    output_strings14.append(f"ALF K72.00 Cirrhosis K74.60")
if (y_predGI_Bleed <.4 and yhistGI_Bleed >.4):
    output_strings14.append(f"GI Bleed K92.2")
if (y_predacutePancreatitis <.4 and yhistPancreatitis >.4):
    output_strings14.append(f"Pancreatitis K85.90")
if (y_predColitis <.4 and yhistColitis >.4):
    output_strings14.append(f"Colitis K52.9", "Sepsis A41.9")
if (y_predGastroenteritis <.4 and yhistGastroenteritis >.4):
    output_strings14.append(f"Gastroenteritis K52.9")
if (y_predBacteremia <.4 and yhistBacteremia >.4):
    output_strings14.append(f"Bacteremia R78.81", "Sepsis A41.9")
if (y_predEndocarditis <.4 and yhistEndocarditis >.4):
    output_strings14.append(f"Endocarditis I38", "Sepsis A41.9")
if (y_predUTI <.4 and yhistUTI >.4):
    output_strings14.append(f"UTI N39.0", "Sepsis A41.9")
if (y_predvented <.4 and yhistvented >.4):
    output_strings14.append(f"vented ARF J96")
if (afib <.4 and yhistafib >.4):
    output_strings14.append(f"Atrial fibrillation I48.0")
if (y_predDM <.4 and yhistDM >.4):
    output_strings14.append(f"DM E11.8")
if (y_predPE <.4 and yhistPE >.4):
    output_strings14.append(f"PE I26.99")
if (y_predICH <.4 and yhistICH >.4):
    output_strings14.append(f"ICH I62.9")
if (y_predSDH <.4 and yhistSDH >.4):
    output_strings14.append(f"SDH S06.5X9A")
if (y_predSAH <.4 and yhistSAH >.4):
    output_strings14.append(f"SAH I60.9")
if (y_predSeizure <.4 and yhistSeizure >.4):
    output_strings14.append(f"Seizures R56.9")
if (y_predESRD <.4 and data['Cr'][0] <= 2 and yhistESRD >.4):
    output_strings14.append(f"ESRD N18.6")
if (y_predCKD <.4 and data['Cr'][0] <= 1.4 and yhistCKD >.4):
    output_strings14.append(f"CKD N18.9")
if (y_predAKI <.4 and data['Cr'][0] <= 1.4 and yhistAKI >.4):
    output_strings14.append(f"AKI N17.9")
if (y_predAsthma <.4 and yhistAsthma >.4):
    output_strings14.append(f"Asthma J45.909")
if (y_predHTN <.4 and yhistHTN >.4) or (y_predHTN >.4 and data['Systolic'][0] < 140):
    output_strings14.append(f"HTN I10")
if (y_predEtOH_WD <.4 and yhistEtOH_WD >.4):
    output_strings14.append(f"EtOH Withdrawal F10.20")
if (y_predCAD <.4 and yhistCAD >.4):
    output_strings14.append(f"CAD I25.10")
if (y_predOSA <.4 and yhistOSA >.4):
    output_strings14.append(f"OSA G47.33")
if (y_predhypothyroid <.4 and yhisthypothyroid >.4):
    output_strings14.append(f"Hypothyroid E03.9")
if (y_predhyperthyroid <.4 and yhisthyperthyroid >.4):
    output_strings14.append(f"Hyperthyroid E05.90")
if (y_predCVA <.4 and yhistCVA >.4):
    output_strings14.append(f"CVA I63.9")
if (y_predDelirium <.4 and yhistDelirium >.4):
    output_strings14.append(f"Delirium R41.0")
if (y_predDLD <.4 and yhistDLD >.4):
    output_strings14.append(f"HLD E78.5")
if (y_predAI <.4 and yhistAI >.4):
    output_strings14.append(f"Adrenal Insufficiency E27.1")
if (y_predLupus <.4 and yhistLupus >.4):
    output_strings14.append(f"Lupus M32.9")
if (y_predCushing <.4 and yhistCushing >.4):
    output_strings14.append(f"Cushings Disease E24.0")
if (y_predScleroderma <.4 and yhistScleroderma >.4):
    output_strings14.append(f"Scleroderma M34.9")
if (y_predPericardial_Effusion <.4 and yhistPericardial_Effusion >.4):
    output_strings14.append(f"Pericardial Effusion I31.39")
if (y_predCholecystitis <.4 and yhistCholecystitis >.4):
    output_strings14.append(f"Cholecystitis  K81.9")
if (y_predARDS <.4 and yhistARDS >.4):
    output_strings14.append(f"ARDS J80")
if (y_predCellulitis <.4 and yhistCellulitis >.4):
    output_strings14.append(f"Cellulitis L03.90 Sepsis A41.9")
if (y_predTBI <.4 and yhistTBI >.4):
    output_strings14.append(f"TBI/Head Trauma S06.9XAA S09.90XA")
if (y_predBurn <.4 and yhistBurn >.4):
    output_strings14.append(f"Burn T30.0")
if (y_predPAD <.4 and yhistPAD >.4):
    output_strings14.append(f"PAD I73.9")
if (y_predBrain_Tumor <.4 and yhistBrain_Tumor >.4):
    output_strings14.append(f"Brain Tumor D49.6")
if (y_predGERD <.4 and yhistGERD >.4):
    output_strings14.append(f"GERD K21.9")

result_string12 = "\n".join(output_strings12)
result_string13 = "\n".join(output_strings13)
result_string14 = "\n".join(output_strings14)

print()
print()


#ICD-10 Output
print()
print()
print('\033[1m' + '*********       ICD-10 Code Checker     *********' + '\033[0m')
print()
print(result_string12)

print()
print('\033[1m' + '   Active Dx:' + '\033[0m')
print()
print(result_string13)

print()
print('\033[1m' + '   Inactive Dx:' + '\033[0m')
print()
print(result_string14)

print()
print('\033[1m' + '   Supplemental ICD-10:' + '\033[0m')
print()