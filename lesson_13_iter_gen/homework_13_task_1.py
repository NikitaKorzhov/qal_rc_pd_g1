class Person:
    def __init__(self,name):
        self.__name=name

    def say_to(self,other_name):
        return f"{self.__name} says {other_name}: pass it on!"

    def tethered_calf(self):
        return f"{self.__name} says: tethered the calf!"

class ChainOfOrders:
    def __init__(self, names: list[str]):
        self.names = ["Senior"] + names.copy()

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if not self.names:
            raise StopIteration

        speaker = Person(self.names.pop(0))

        if not self.names:
            return speaker.tethered_calf()

        return speaker.say_to(self.names[0])


names = ["Mykhailo", "Petro", "Pavlo"]
chain = ChainOfOrders(names)

for n in chain:
    print(n)