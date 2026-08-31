from abc import ABC, abstractmethod


class MagicCreature(ABC):
    def __init__(self, name, magic_level=1, health=10):
        self.name = name
        self.__validate_magic_level(magic_level)
        self.__validate_health(health)
        self._magic_level = magic_level
        self.__health = health
        self.__alive = True

    @staticmethod
    def __validate_magic_level(value):
        if not isinstance(value, int):
            raise TypeError("Magic level should be an integer")
        if not 1 <= value <= 10:
            raise ValueError("Magic level should be from 1 to 10!")

    @staticmethod
    def __validate_health(value):
        if not isinstance(value, int):
            raise TypeError("Health should be an integer")
        if not 0 <= value <= 100:
            raise ValueError("Health should be from 0 to 100!")

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if not isinstance(value, int):
            raise TypeError("Health should be an integer")
        if value > 100:
            raise ValueError("Health should be from 0 to 100!")
        if not self.__alive:
            raise ValueError("Creature is dead")
        if value <= 0:
            self.__health = 0
            self.__alive = False
        else:
            self.__health = value

    @property
    def magic_level(self):
        return self._magic_level

    @magic_level.setter
    def magic_level(self, value):
        self.__validate_magic_level(value)
        if not self.__alive:
            raise ValueError("Creature is dead")
        self._magic_level = value

    @property
    def is_alive(self):
        return self.__alive

    @abstractmethod
    def use_ability(self):
        pass

    @abstractmethod
    def describe(self):
        pass

    @abstractmethod
    def weakness(self):
        pass

    def take_damage(self, amount):
        if not self.is_alive:
            return f"{self.name} has already defeated death... or has he?"
        self.health = self.health - amount

    def __str__(self):
        return f"{self.name} | Magic: {self.magic_level} | HP: {self.health} | Alive: {self.is_alive}"


class Molfar(MagicCreature):
    def __init__(self, name, element, spells, magic_level=5, health=10):
        super().__init__(name, magic_level, health)
        self.element = element
        self.spells = spells

    @property
    def spells(self):
        return self.__spells

    @spells.setter
    def spells(self, value):
        if not isinstance(value, int):
            raise TypeError("Spells count should be an integer")
        if value < 0:
            raise ValueError("Spells count cannot be negative")
        self.__spells = value

    def use_ability(self):
        if self.__spells == 0:
            return f"Molfar {self.name} is exhausted — the power of the elements has left him!"
        self.__spells -= 1
        return f"Molfar {self.name} calls upon {self.element}! Spells remaining: {self.__spells}"

    def describe(self):
        return f"Molfar {self.name}, master of the {self.element} element. Magic level: {self.magic_level}"

    def weakness(self):
        return "opposite element"


class Rusalka(MagicCreature):
    def __init__(self, name, river, charm_power, magic_level=5, health=10):
        super().__init__(name, magic_level, health)
        self.river = river
        self.charm_power = charm_power

    @property
    def charm_power(self):
        return self.__charm_power

    @charm_power.setter
    def charm_power(self, value):
        if not isinstance(value, int):
            raise TypeError("Charm power should be an integer")
        if not 1 <= value <= 5:
            raise ValueError("Charm power should be from 1 to 5")
        self.__charm_power = value

    def use_ability(self):
        message = f"Rusalka {self.name} from the {self.river} river charms a traveler! Charm power: {self.charm_power}"
        if self.charm_power == 5:
            message += " No one can resist!"
        return message

    def describe(self):
        return f"Rusalka {self.name}, dweller of the {self.river} river. Charm power: {self.charm_power}/5"

    def weakness(self):
        return "sunlight"


class Perelesnyk(MagicCreature):
    def __init__(self, name, speed, form, magic_level=5, health=10):
        super().__init__(name, magic_level, health)
        self.speed = speed
        self.form = form

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if not isinstance(value, int):
            raise TypeError("Speed should be an integer")
        if not 1 <= value <= 100:
            raise ValueError("Speed should be from 1 to 100")
        self.__speed = value

    def use_ability(self):
        message = f"Perelesnyk {self.name} races through the night at speed {self.speed}! Form: {self.form}"
        if self.form == "human":
            message += " No one will suspect a thing..."
        return message

    def describe(self):
        return f"Perelesnyk {self.name}. Speed: {self.speed}. Currently in form: {self.form}"

    def change_form(self):
        self.form = "human" if self.form == "fireball" else "fireball"
        return f"Perelesnyk turned into {self.form}!"

    def weakness(self):
        return "holy water"


class EnchantedForest:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.__creatures = []

    def add_creature(self, creature):
        if len(self.__creatures) >= self.capacity:
            return f"Enchanted forest {self.name} is full!"
        if not creature.is_alive:
            return "Dead creatures cannot settle in the forest!"
        if any(existing.name == creature.name for existing in self.__creatures):
            return f"{creature.name} already lives in this forest!"
        self.__creatures.append(creature)

    def remove_creature(self, name):
        for creature in self.__creatures:
            if creature.name == name:
                self.__creatures.remove(creature)
                return
        return f"Creature {name} was not found in the forest!"

    def most_powerful(self):
        if not self.__creatures:
            return "The forest is empty — no one to cast spells!"
        return max(self.__creatures, key=lambda creature: creature.magic_level)

    def attack_intruder(self, intruder_name):
        alive_creatures = [creature for creature in self.__creatures if creature.is_alive]
        if not alive_creatures:
            return f"The forest is defenseless before {intruder_name}!"
        return [
            f"{creature.use_ability()} (Weakness: {creature.weakness()})"
            for creature in alive_creatures
        ]

    def census(self):
        if not self.__creatures:
            return "The forest is empty"
        return [creature.describe() for creature in self.__creatures]

    @property
    def creatures_count(self):
        return len([creature for creature in self.__creatures if creature.is_alive])

    def heal_all(self, amount):
        for creature in self.__creatures:
            if creature.is_alive:
                creature.health = min(100, creature.health + amount)


if __name__ == "__main__":
    forest = EnchantedForest("Black Forest", capacity=5)

    molfar = Molfar("Yurii", magic_level=8, health=90, element="fire", spells=3)
    rusalka = Rusalka("Kalyna", magic_level=6, health=100, river="Dnipro", charm_power=5)
    perelesnyk = Perelesnyk("Iskra", magic_level=7, health=85, speed=95, form="fireball")

    forest.add_creature(molfar)
    forest.add_creature(rusalka)
    forest.add_creature(perelesnyk)

    print(forest.most_powerful())
    print(forest.attack_intruder("hunter"))

    molfar.take_damage(90)
    print(molfar.is_alive)

    print(forest.census())
