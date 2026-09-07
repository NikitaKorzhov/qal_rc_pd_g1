MINERAL_CATALOG= {    
    "назва": {
        "formula": "хімічна формула",
        "hardness": 6,   
        "origin": "місце знахідки",
        "discovered": 1000
}}

def get_mineral(name:str):
    return MINERAL_CATALOG.get(name,None)

def register_mineral(name, formula, hardness, origin, discovered):
    if name in  MINERAL_CATALOG:
        return f"Mineral {name} already exists"
    if 0<hardness<=10:
        MINERAL_CATALOG[name]={
            "formula":formula,
            "hardness":hardness,
            "origin":origin,
            "discovered":discovered
        }
        return f"{name} included to catalog"
    else:
        return "Hardness should be betwen 0 and 10"
def show_mineral(name):
    mineral=MINERAL_CATALOG[name]
    return f"Formula: {mineral['formula']} | Hardness: {mineral['hardness']} | Origin: {mineral['origin']} | Discovered: {mineral['discovered']}"