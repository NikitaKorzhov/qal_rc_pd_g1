import random

class Person:
    def __init__(self, name: str):
        self.name = name

class Message:
    def __init__(self, text: str):
        self._text = text

    @property
    def text(self) -> str:
        return self._text

    def distort(self):
        words = self._text.split()
        if words:
            rand_idx = random.randint(0, len(words) - 1)
            words[rand_idx] = "???"
            self._text = " ".join(words)

class TelephoneChain:
    def __init__(self, start_message: str, names: list[str]):
        self.people = [Person(name) for name in names]
        self.message = Message(start_message)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> tuple[str, str]:
        if self.index >= len(self.people):
            raise StopIteration

        current_person = self.people[self.index]
        
        if self.index > 0 and random.random() < 0.3:
            self.message.distort()

        self.index += 1
        return (current_person.name, self.message.text)


people_list = ["Horpyna", "Paraska", "Yavdoha", "Oksana", "Halyna", "Ivanivna", "Aryna"]
phone_game = TelephoneChain("The calf ran away from the shed and hid", people_list)

for person, msg in phone_game:
    print(f"{person}: {msg}")