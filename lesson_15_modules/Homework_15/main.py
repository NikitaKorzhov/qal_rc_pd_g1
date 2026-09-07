import vernadsky_lab as lab

print("Registration of minerals in catalog:")
minerals_data = [
    ("Quartz", "SiO2", 5, "Derived from the German word Quarz of Slavic origin", 1700),
    ("Halite", "NaCl", 5, "mount", 100),
    ("Halite", "NaCl", 5, "mount", 100),
    ("Pyrite", "FeS2", 6, "Derived from the Greek word pyr meaning fire", 1171),
    ("Hematite", "Fe2O3", 6, "Derived from the Greek word haimatitis meaning blood-red", 1565),
    ("Malachite", "Cu2CO3(OH)2", 4, "Derived from the Greek word molochite meaning mallow-green", 300)
]

for name, formula, hardness, origin, discovered in minerals_data:
    result = lab.register_mineral(name, formula, hardness, origin, discovered)
    print(result)
print("\n")

observations=[
    {"researcher":"Pavlo","mineral":"Quartz","note":"can fier"},
    {"researcher":"Richard","mineral":"Quartz","note":"Black"},
    {"researcher":"Richard","mineral":"Quartz","note":"Not soft"},
    {"researcher":"Pavlo","mineral":"Pyrite","note":"Metallic luster"},
    {"researcher":"Richard","mineral":"Malachite","note":"Vibrant green pattern"},
    {"researcher":"Pavlo","mineral":"Calcite","note":"Reacts with acid"},
]
print("Observations registration:")
for obs in observations:
    print(lab.record(obs["researcher"],obs['mineral'],obs['note']))
print("\n")
r=lab.summary()
report=lab.mineral_report("Quartz")
print(report)
print(r)
print("\n")

print(lab.hardest_minerals())
print("\n")
print("Minerals with Greek origin")
print(lab.search_by_origin("greek"))
lab.to_csv("journal.csv")


