events = [
    "Mykhailyk passed on the assignment",
    "Vasylko refused",
    "Hrytsko passed on the assignment",
    "Olenka tethered the calf",
    "Danylko passed on the assignment",
]

# Один рядок з генераторним виразом
count = sum(1 for event in events if "passed on the assignment" in event)

print(f"The assignment was passed on {count} times")