import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Hello World

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))

st.text_area(label="Note")

Op_Note = 'cc' #@param {type:"string"}
Na = None #@param {type:"number"}
K = None #@param {type:"number"}ient is a 55 year old man with past medical hx of ALS, diabetes, respiratory failure 2/2 ALS for which he has been ventilator dependent for several years, chronic loculated hydropneumothorax, DM, dysphagia brought in to ED 2/2 progressive increase of WOB, ventilator asynchrony and respiratory distress at home.  The patient underwent CT chest which reveals increase air surrounding lung in hydropneumothorax.  Pulmonary evaluating.
AG = None #@param {type:"number"}
Cr = None #@param {type:"number"}
Hgb = None #@param {type:"number"}
Plt = None #@param {type:"number"}
INR = None #@param {type:"number"}
aPTT = None #@param {type:"number"}
SBP  = None #@param {type:"number"}
Intubated = 0 #@param {type:"integer"}
Narrative = '0' #@param {type:"string"}
maxtoken  = None #@param {type:"number"}
Note = Note.lower()
Op_Note = Op_Note.lower()
#screen grabber values


def convert_spelled_numbers_to_numerals(text):
    spelled_number_pattern = r'\b(zero|one|two|three|four|five|six|seven|eight|nine|ten)\b'
    numerals = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10', 'hundred': '100', 'thousand': '1000'}

    def replace_number(match):
        return numerals.get(match.group(0), match.group(0))

    converted_text = re.sub(spelled_number_pattern, replace_number, Note)
    return converted_text


Note = convert_spelled_numbers_to_numerals(Note)


def convert_words_to_ordinals(text):
    ordinals = {
        'first': '1t',
        'second': '2t',
        'third': '3t',
        'fourth': '4t',
        'fifth': '5t',
        'sixth': '6t',
        'seventh': '7t',
        'eighth': '8t',
        'ninth': '9t',
        'tenth': '10h',
        # Add more ordinals as needed
    }

    # Define a regular expression pattern to match words in the dictionary
    ordinal_pattern = r'\b(' + '|'.join(re.escape(key) for key in ordinals.keys()) + r')\b'

    def replace_word(match):
        word = match.group(0)
        return ordinals.get(word, word)

    converted_text = re.sub(ordinal_pattern, replace_word, text, flags=re.IGNORECASE)
    return converted_text

Note = convert_words_to_ordinals(Note)
doc2 = nlp2(Note)

data = pd.DataFrame(data={'Number': [0], 'Note': [Note], 'Op Note': [Op_Note], 'Na': [Na], 'K': [K], 'AG': [AG], 'Cr': [Cr], 'Hgb': [Hgb], 'Systolic': [SBP], 'Vented': [Intubated], 'Plt': [Plt], 'INR': [INR], 'PTT': [aPTT]})

#medspacy history and negation calculator
#doc3 = nlp(el)
doc3 = nlp(response1)
doc = nlp(response2)
docop = nlp(Op_Note)



#NoteGen Output
print()
print()
print()
print()
print('\033[1m' + '*********       Assessment and Plan     *********' + '\033[0m')
print()
print(response3.choices[0].message['content'])


print()
print("I spent a total of greater than 60 minutes formulating critical care for this patient today. I saw this patient and completed a full visual exam via audio-visual HIPAA compliant technology.")
print()
print()
print('\033[1m' + '*********      Operative Assessment and Plan     *********' + '\033[0m')
print()

if yprocextremity_angiogram >.4:
    print(Op1)

if yprocimpella > .4:
    print(Op2)

if yproccraniotomy > .4:
    print(Op3)

if yproccoronary_angiogram > .4:
    print(Op4)

if yproccabg > .4:
    print(Op5)

if yprocavr > .4:
    print(Op6)

if yprocaaa > .4:
    print(Op7)

if yprocpericardial_window > .4:
    print(Op8)

if yprocmvr > .4:
    print(Op9)


print(response5)
#lines = response5.split('\n')
# Print lines starting from the second line (index 1 and onwards)
#for line in lines[1:]:
 #   print(line)



print()
print()
print('\033[1m' + '*********       Prophylaxis Checker     *********' + '\033[0m')
print()
print()
#Prophylaxis Checker
if (SUP >.4):
    print('\033[1m' + 'SUP Indicated' + '\033[0m')
    print('   Reason:')
    if (y_predvented >.4):
        print('     Ventilator')
    if (y_predRespiratory_Failure >.4 and y_predvented <.4):
        print('     NIV')
    if (y_predTBI >.4):
        print('     TBI')
    if (y_predBurn >.4):
        print('     Burns')
    if (y_predCoagulopathy >.4):
        print('     Coagulopathy')
        if (data['INR'][0] >= 1.6):
            print('     INR', data['INR'][0])
        if (data['Plt'][0] <= 50):
            print('     Plt', data['Plt'][0])
        if (data['PTT'][0] >= 50):
            print('     aPTT', data['PTT'][0])
    if (y_predBrain_Tumor > .4):
        print('     Brain Tumor')
    if (y_predGERD >.4):
        print('     GERD')
    if (y_predGI_Bleed >.4):
        print('     GI Bleed')
    if (y_predSAH >.4 or y_predSDH >.4 or y_predICH >.4 or y_predTBI >.4):
        print('    Brain Bleed/Trauma')
else:
    print('\033[1m' + 'No SUP Indicated' + '\033[0m')
print()
if (chemDVT <.4 and mechDVT <.4):
    print('\033[1m' + 'No Mechanical or Chemical DVT PPx Indicated' + '\033[0m')
    print('   Reason:')
    if (y_predPAD >.4):
        print('    PAD')
    if (y_predCellulitis >.4):
        print('    Cellulitis')
    if (severecoag >.4):
        print('    Severe Coagulopathy')
    elif (y_predCoagulopathy >.4):
        print('    Coagulopathy')
        if (data['INR'][0] >= 1.6):
            print('     INR', data['INR'][0])
        if (data['Plt'][0] <= 50):
            print('     Plt', data['Plt'][0])
        if (data['PTT'][0] >= 50):
            print('     aPTT', data['PTT'][0])
    if (y_predSAH >.4 or y_predSDH >.4 or y_predICH >.4 or y_predTBI >.4):
        print('    Brain Bleed/Trauma')
    if (y_predGI_Bleed >.4):
        print('    GI Bleed')
    if (y_predAAA >.4):
        print('    AAA/Dissection')
    if (y_predBrain_Tumor >.4):
        print('     Brain Tumor')
    if (data['Hgb'][0]  < 7):
        print('    Hgb', data['Hgb'][0])
elif (chemDVT < .4 and mechDVT >= .4):
    print('\033[1m' + 'Only Mechanical DVT PPx Indicated' + '\033[0m')
    print('   Reason:')
    if (y_predSAH >.4 or y_predSDH >.4 or y_predICH >.4 or y_predTBI >.4):
        print('    Brain Bleed/Trauma')
    if (y_predGI_Bleed >.4):
        print('     GI Bleed')
    if (y_predAAA >.4):
        print('     AAA/Dissection')
    if (y_predCoagulopathy >.4):
        print('     Coagulopathy')
        if (data['INR'][0] >= 1.6):
            print('     INR', data['INR'][0])
        if (data['Plt'][0] <= 50):
            print('     Plt', data['Plt'][0])
        if (data['PTT'][0] >= 50):
            print('     aPTT', data['PTT'][0])
    if (y_predBrain_Tumor >.4):
        print('     Brain Tumor')
    if (data['Hgb'][0]  < 7):
        print('     Hgb', data['Hgb'][0])
elif (chemDVT >= .4):
        print('\033[1m' + 'Chemical DVT PPx Indicated' + '\033[0m')
print()
print()
print()
print('\033[1m' + '*********       Variable Display     *********' + '\033[0m')
print()
print()
data