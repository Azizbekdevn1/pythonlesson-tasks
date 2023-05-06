# Sana:7.05.2023
# Mavzu:Json
# Muallif:Murodov Azizbek

import json

data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
talaba_json = """{"ism": "Hasan", "familiya": "Husanov", "tyil": 2000}"""
data_json = json.dumps(data)
talaba = json.loads(talaba_json)
print(data_json)
print(type(data_json))
with open("data.json", "w") as f:
    json.dump(data, f)
with open("talaba.json", "w") as file:
    json.dump(talaba, file)

print(type(talaba))
print(talaba["ism"])
print(talaba["familiya"])
with open("students.json") as f:
    students = json.load(f)
students_json = json.dumps(students, indent=4)
print(students_json)

for item in students["student"]:
    print(
        f"{item['name']} {item['lastname']} ,{item['year']}-kurs, {item['faculty']} talabasi"
    )
with open("api-result.json") as f:
    wiki = json.load(f)

print(wiki["query"]["pages"]["13801"]["title"])
print(wiki["query"]["pages"]["13801"]["extract"])
