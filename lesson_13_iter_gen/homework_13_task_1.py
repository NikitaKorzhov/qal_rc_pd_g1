class ChainOfOrders:
    def __init__(self, names: list[str]):
        self.__speaker = "Senior"
        self.__continue_chain = ": pass it on!"
        self.__end_chain = "says: tethered the calf!"

        self.names = [self.__speaker] + names.copy()

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if not self.names:
            raise StopIteration

        speaker = self.names.pop(0)

        if not self.names:
            return f"{speaker} {self.__end_chain}"

        listener = self.names[0]
        return f"{speaker} says {listener}{self.__continue_chain}"


names = ["Mykhailo", "Petro", "Pavlo"]
chain = ChainOfOrders(names)

for n in chain:
    print(n)