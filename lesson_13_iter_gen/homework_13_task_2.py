def village_rumor(start_message: str, people: list[str]):
    if not people:
        return
    
    current_msg = start_message

    # First person tells the original message
    first_person = people[0]
    yield f'{first_person} says: "{current_msg}"'

    # Intermediate and last people in the chain
    for i in range(1, len(people)):
        prev_person = people[i - 1]
        current_person = people[i]
        
        # Append the information about who passed it
        current_msg += f" (passed by {prev_person})"

        # If this is the last person in the list
        if i == len(people) - 1:
            yield f'{current_person} passes on: "{current_msg} (and everyone found out!)"'
        else:
            yield f'{current_person} passes on: "{current_msg}"'


# Test example with English text:
for version in village_rumor("The calf ran away!", ["Horypyna", "Paraska", "Yavdokha", "Oksana"]):
    print(version)