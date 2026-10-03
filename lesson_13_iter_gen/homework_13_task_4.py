import itertools
def toloka_queue(persons:list[str]):
    if not persons:
        return
    while True:
        for person in persons:
            yield person

queue = toloka_queue(["Olexandr", "Svitlozar", "Nikita"])

# Take first 10 duties with itertools.islice()
for turn in itertools.islice(queue, 10):
    print(turn)