import openai
openai.api_key ="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"

#GPT Insert

question1 = "find separate and list active medical problems under heading 'active medical'"
question2 = "find separate and list past medical history under heading 'past medical history'"
question4 = "find separate and list names of active medications only"

prompt1 = f"{Note}\n\n{question1}"
prompt2 = f"{Note}\n\n{question2}"
prompt4 = f"{Note}\n\n{question4}"

def get_response3(prompt):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        temperature=0.5,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

def get_response5(prompt):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        temperature=0.1,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

def get_response4(prompt, max_tokens=maxtoken):
    return openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        temperature=0.09,
        messages=[
            {"role": "system", "content": "edit this existing assessment and plan to incorporate these active diseases," + response1 + " and these medications " + response4 + "keeping same order and format. Also remember to keep diagnoses in first line and therapies.  Do not remove differential diagnosis"},
            {"role": "user", "content": prompt}
        ]
    )

response1 = get_response3(prompt1)
response1 = response1.choices[0].message['content']
response1 = response1.lower()
response1 = response1.translate(str.maketrans(' ', ' ', string.punctuation))

response2 = get_response3(prompt2)
response2 = response2.choices[0].message['content']
response2 = response2.lower()
response2 = response2.translate(str.maketrans(' ', ' ', string.punctuation))

response4 = get_response3(prompt4)
response4 = response4.choices[0].message['content']
response4 = response4.lower()
response4 = response4.translate(str.maketrans(' ', ' ', string.punctuation))

#question5 = "only list diagnoses with ICD-10 codes without duplicates and to" + result_string12
#prompt5 = f"{response1}\n\n{question5}"

#response5 = get_response3(prompt5)
#response5 = response5.choices[0].message['content']
#response5 = response5.lower()
#response5 = response5.translate(str.maketrans(' ', ' ', string.punctuation))
