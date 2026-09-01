import random

class TelephoneChain:
    def __init__(self, start_message: str, people: list[str]):
        self.people = people.copy()
        self.current_message = start_message
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> tuple[str, str]:
        if self.index >= len(self.people):
            raise StopIteration

        current_person = self.people[self.index]
        self.index += 1

        if self.index > 1 and self.current_message:
            if random.random() < 0.3:
                words = self.current_message.split()
                if words:
                    rand_idx = random.randint(0, len(words) - 1)
                    words[rand_idx] = "???"
                    self.current_message = " ".join(words)

        return (current_person, self.current_message)


people_list = ["Horpyna", "Paraska", "Yavdoha", "Oksana","Halyna","Ivanivna","Aryna"]
phone_game = TelephoneChain("The calf ran away from the shed and hid", people_list)

for person, msg in phone_game:
    print(f"{person}: {msg}")