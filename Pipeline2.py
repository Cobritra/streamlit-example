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



#screen grabber pipeline
warnings.filterwarnings('ignore')
nlp2 = medspacy.load()
nlp2.remove_pipe("medspacy_context")
nlp2.pipe_names
preprocessor2 = Preprocessor(nlp2.tokenizer)
nlp2.tokenizer = preprocessor2

preprocess_rules2 = [
   # PreprocessingRule(lambda x: x.lower(), desc="Lowercase text"),
    PreprocessingRule(r"~", repl=" ", desc="crush tilda"),
    PreprocessingRule(r"\[\*\*[^\]]+\]", desc="Remove all other bracketed placeholder text from MIMIC"),
    PreprocessingRule("dx'd", repl="Diagnosed", desc="Replace abbreviation"),
    PreprocessingRule(r"tx'd", repl="Treated", desc="Replace abbreviation"),
    PreprocessingRule(r"\[\*\*[\d]{1,4}-[\d]{1,2}(-[\d]{1,2})?\*\*\]", repl="01-01-2010", desc="Replace MIMIC date brackets with a generic date."),
    PreprocessingRule(r"\[\*\*[\d]{4}\*\*\]", repl="2010", desc="Replace MIMIC year brackets with a generic year."),
]

preprocessor2.add(preprocess_rules2)
target_matcher2 = nlp2.get_pipe("medspacy_target_matcher")

target_rules2 = [
        TargetRule("", "number",
               pattern=[{"LIKE_NUM": True}]),
        TargetRule("male", "male", pattern=[{'LOWER': {'IN': ['man', 'y/o/m', 'yom']}}]),
        TargetRule("male", "male",
                   pattern=[{'LOWER': {'IN': ['year', 'y', 'y/']}},
                            {'LOWER': {'IN': ['old', 'o', '/o']}},
                            {'LOWER': {'IN': ['man', 'male', 'm']}}]),
        TargetRule("female", "female", pattern=[{'LOWER': {'IN': ['woman', 'y/o/w', 'yow', 'female']}}]),
        TargetRule("female", "female",
                   pattern=[{'LOWER': {'IN': ['year', 'y', 'y/']}},
                            {'LOWER': {'IN': ['old', 'o', '/o']}},
                            {'LOWER': {'IN': ['woman', 'female', 'w']}}]),
        TargetRule("male", "male",
                   pattern=[{'LOWER': {'IN': ['year', 'yo', 'y/o', 'year', 'y.o.']}},
                            {'LOWER': {'IN': ['old', 'man', 'male', 'm']}}]) ,
        TargetRule("female", "female",
                   pattern=[{'LOWER': {'IN': ['year', 'yo', 'y/o', 'year', 'y.o.']}},
                            {'LOWER': {'IN': ['old', 'woman', 'female', 'f', 'w']}}]) ,

]

target_matcher2.add(target_rules2)
context2 = nlp2.add_pipe("medspacy_context", config={"rules": None})

context_rules2 = [
    ConTextRule(literal='Na', category='NA', pattern=[{'LOWER': {'IN': ['na:', 'na', 'sodium', 'sodio', 'sod', 'sodium:', 'sodio:', 'sod:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='K', category='K', pattern=[{'LOWER': {'IN': ['k+:', 'potassium', 'potassio', 'pot', 'k+', 'k', 'k:', 'potassium:', 'potassio:', 'pot:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='kul', category='KUL', pattern=[{'LOWER': {'IN': ['k/ul:', 'k/ul:', 'ul']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='last7', category='LAST7', pattern=[{'LOWER': {'IN': ['adpclosure', 'adpclosure:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Systolic EF', category='SYSEF', pattern=[{'LOWER': {'IN': ['systolic', 'sys']}},
                                                              {'LOWER': {'IN': ['ef', 'ef:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Creatinine', category='CREATININE', pattern=[{'LOWER': {'IN': ['cr:', 'creatinine:', 'creatinine', 'creat', 'cr', 'creat:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='protein', category='PROTEIN', pattern=[{'LOWER': {'IN': ['prot', 'protein', 'prot:', 'protein:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Chloride', category='CHLORIDE', pattern=[{'LOWER': {'IN': ['cl:', 'cl', 'chloride', 'chloride:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='CO2', category='CO2', pattern=[{'LOWER': {'IN': ['c02:', 'c02','co2', 'hc03:', 'bicarbonate', 'bicarb', 'co2:', 'hc03', 'bicarbonate:', 'bicarb:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='CO2', category='CO2', pattern=[{'LOWER': {'IN': ['carbon']}},
                                                        {'LOWER': {'IN': ['dioxide']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='BUN', category='BUN', pattern=[{'LOWER': {'IN': ['bun:', 'bun', 'urea:', 'urea']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='BUN', category='BUN', pattern=[{'LOWER': {'IN': ['blood']}},
                                                        {'LOWER': {'IN': ['urea']}},
                                                        {'LOWER': {'IN': ['nitrogen', 'nitrogen:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Calcium', category='CALCIUM', pattern=[{'LOWER': {'IN': ['ca:', 'ca+', 'calcium', 'ca', 'ca+:', 'calcium:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Glucose', category='GLUCOSE', pattern=[{'LOWER': {'IN': ['glucose:', 'glucose', 'fs', 'gluc', 'fs:', 'gluc:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Glucose', category='GLUCOSE', pattern=[{'LOWER': {'IN': ['finger']}},
                                                                {'LOWER': {'IN': ['glucose:', 'glucose', 'stick', 'stick:']}}],max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Hemoglobin', category='HEMOGLOBIN', pattern=[{'LOWER': {'IN': ['hemoglobin:', 'hemoglobin', 'hgb', 'hgb:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='WBC', category='WBC', pattern=[{'LOWER': {'IN': ['wbc:', 'wbc', 'white cell', 'white blood cell', 'white cells', 'white blood cells', 'white cell:', 'white blood cell:', 'white cells:', 'white blood cells:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Platelet', category='Platelet', pattern=[{'LOWER': {'IN': ['platelet:', 'plat', 'platelet', 'platelets', 'plt', 'platelets:', 'plt:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Albumin', category='ALBUMIN', pattern=[{'LOWER': {'IN': ['albumin:', 'albumin', 'alb', 'alb:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Bilirubin', category='BILIRUBIN', pattern=[{'LOWER': {'IN': ['bilirubin:', 'bilirubin', 'bili', 'bili:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='AST', category='AST', pattern=[{'LOWER': {'IN': ['ast:', 'ast', 'aspartate aminotransferase', 'aspartate aminotransferase:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='ALT', category='ALT', pattern=[{'LOWER': {'IN': ['alt:', 'alt', 'alanine transaminase', 'alanine transaminase:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Alk Phos', category='ALK PHOS',
                pattern=[{'LOWER': {'IN': ['ALK', 'alk', 'alkaline', 'alkphos', 'alkphos:']}},
                         {'LOWER': {'IN': ['PHOS', 'phos', 'phosphatase', 'phosphatase:', 'phos:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Alk Phos', category='ALK PHOS', pattern=[{'LOWER': {'IN': ['alkphos', 'alkphos:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Temperature', category='TEMPERATURE', pattern=[{'LOWER': {'IN': ['temp:', 'temp', 'temperature', 'temperature:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Heary Rate', category='HEART RATE', pattern=[{'LOWER': {'IN': ['pulse:', 'pulse', 'hr', 'hr:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Heart Rate', category='HEART RATE',
                pattern=[{'LOWER': {'IN': ['heart', 'pulse']}},
                         {'LOWER': {'IN': ['rate:', 'rate']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Systolic BP', category='SYSTOLIC', pattern=[{'LOWER': {'IN': ['systolic:', 'systolic', 'sbp', 'sbp:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Systolic BP', category='SYSTOLIC',
                pattern=[{'LOWER': {'IN': ['systolic']}},
                         {'LOWER': {'IN': ['blood', 'pressure']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Systolic BP', category='SYSTOLIC',
                pattern=[{'LOWER': {'IN': ['systolic']}},
                         {'LOWER': {'IN': ['blood']}},
                         {'LOWER': {'IN': ['pressure', 'pressure:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Diastolic BP', category='DIASTOLIC', pattern=[{'LOWER': {'IN': ['diastolic:', 'diastolic', 'dbp', 'dbp:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Diastolic BP', category='DIASTOLIC',
                pattern=[{'LOWER': {'IN': ['diastolic']}},
                         {'LOWER': {'IN': ['pressure', 'pressure:']}}]  , max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Diastolic BP', category='DIASTOLIC',
                pattern=[{'LOWER': {'IN': ['diastolic']}},
                         {'LOWER': {'IN': ['blood']}},
                         {'LOWER': {'IN': ['pressure', 'pressure:']}}]  , max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Mean BP', category='MAP', pattern=[{'LOWER': {'IN': ['map:', 'map']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Mean BP', category='MAP', pattern=[{'LOWER': {'IN': ['mean']}},
                                                            {'LOWER': {'IN': ['pressure', 'pressure:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Mean BP', category='MAP', pattern=[{'LOWER': {'IN': ['mean']}},
                                                            {'LOWER': {'IN': ['arterial', 'artery']}},
                                                            {'LOWER': {'IN': ['pressure', 'pressure:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Blood Pressure', category='SYSTOLIC', pattern=[{'LOWER': {'IN': ['bp:', 'bp', 'blood']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Blood Pressure', category='SYSTOLIC', pattern=[{'LOWER': {'IN': ['blood', 'arterial',  'pres:']}},
                                                                  {'LOWER': {'IN': ['pressure', 'pressure:', 'line', 'line:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Respiratory Rate', category='RESPIRATORY RATE', pattern=[{'LOWER': {'IN': ['rr', 'rr:', 'resp', 'resp:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='Respiratory Rate', category='RESPIRATORY RATE', pattern=[{'LOWER': {'IN': ['respiratory', 'resp']}},
                                                                                  {'LOWER': {'IN': ['rate:', 'rate']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='O2 Sat', category='O2 SAT', pattern=[{'LOWER': {'IN': ['spo2', 'spo2:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='O2 Sat', category='O2 SAT', pattern=[{'LOWER': {'IN': ['o2', 'oxygen']}},
                                                              {'LOWER': {'IN': ['sat:', 'sat', 'saturation']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='aPTT', category='PTT', pattern=[{'LOWER': {'IN': ['aptt', 'ptt', 'aptt:', 'ptt:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='aPTT', category='PTT', pattern=[{'LOWER': {'IN': ['partial', 'activated']}},
                                                         {'LOWER': {'IN': ['thromboplastin']}},
                                                         {'LOWER': {'IN': ['time', 'time:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='PT', category='PT', pattern=[{'LOWER': {'IN': ['pt', 'pt:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='PT', category='PT', pattern=[{'LOWER': {'IN': ['prothrombin']}},
                                                      {'LOWER': {'IN': ['time', 'time:']}}],max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='INR', category='INR', pattern=[{'LOWER': {'IN': ['inr', 'inr:']}}], max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='INR', category='INR', pattern=[{'LOWER': {'IN': ['international']}},
                                                        {'LOWER': {'IN': ['normal', 'normalized']}},
                                                        {'LOWER': {'IN': ['ratio', 'ratio:']}}],max_targets = 1, direction='FORWARD'),
    ConTextRule(literal='AGE', category='AGE', pattern=[{'LOWER': {'IN': ['yow', 'y/o/w', 'yom', 'y/o', 'y\o']}}], max_targets = 1, direction='BACKWARD'),
    ConTextRule(literal='Results from last', category='accident', pattern=[{'LOWER': {'IN': ['results from last']}}], max_targets = 1, direction='BACKWARD'),
    ConTextRule(literal='AGE', category='AGE', pattern=[{'LOWER': {'IN': ['year', 'y', 'y/', 'yo']}},
                                                        {'LOWER': {'IN': ['old', 'o', '/o', ""]}},
                                                        {'LOWER': {'IN': ['man', 'male', 'woman', 'female', 'm', 'f', 'w']}}],max_targets = 1, direction='BACKWARD'),
    ConTextRule(literal='AGE', category='AGE', pattern=[{'LOWER': {'IN': ['year', 'yo', 'y/o', 'year', 'o']}},
                                                        {'LOWER': {'IN': ['old', 'man', 'male', 'woman', 'female', 'm', 'f', 'w']}}],max_targets = 1, direction='BACKWARD'),

]
context2.add(context_rules2)