def find_calf(log):
    for line in log:
        if not isinstance(line, str):
            continue
        if "tethered" in line:
            yield line
            return

journal = [
    "Mykhailiy received an assignment",
    "Mykhailiy passed it to Vasylko",
    "Vasylko got distracted",
    "Vasylko passed it to Olenka",
    "Olenka tethered the calf near the shed",
    "Olenka went home",
    "Grandpa calmed down",
]

print(f"line is {next(find_calf(journal))}")