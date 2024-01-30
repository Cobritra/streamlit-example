
#response1_text = response1.choices[0].message['content']
question3 = "edit this assessment and plan to incorporate these active diseases" + response1 + "keeping same format"
prompt3 = f"{result_string10}\n\n{question3}"
response3 = get_response4(result_string10)



question5 = "only list diagnoses with ICD-10 codes without duplicates and to" + result_string12
prompt5 = f"{response1}\n\n{question5}"

response5 = get_response3(prompt5)
response5 = response5.choices[0].message['content']