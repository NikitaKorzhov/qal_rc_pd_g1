class Cossack:
    def __init__(self,name:str,kurin:str,weapons:list[str]=None):
        self.name=name
        self.kurin=kurin
        self.__weapons=weapons if weapons is not None else []
        self.__victories=0
        self.__rank = "Cossack"  

    @property
    def victories(self):
        return self.__victories
    @property
    def rank(self):
        return self.__rank

    def promote(self):
        if self.__victories >= 7:
            self.__rank = "Polkovnyk"
        elif self.__victories >= 3:
            self.__rank = "Osavul"
        else:
            self.__rank = "Cossack"
    
    def arm(self,wepon):
        if wepon in self.__weapons:
            print(f"{self.name} already has weapon {wepon}")
        else:
            self.__weapons.append(wepon)

    def win_battle(self, enemy:str):
        self.__victories+=1
        self.promote()
        return f"Cosack {self.name} wins {enemy}. Grory for Cosack"

    def __repr__(self):
        return f"Cosack {self.name} | Kurin: {self.kurin} | Victories: {self.__victories} | Weapons: {self.__weapons}"


class ZaporozhianSich:
    def __init__(self,name:str,capacity:int):
        self.name=name
        self.__capacity=capacity
        self.__cossacks=[] 

    @property 
    def cossacks(self):
        return self.__cossacks
    @property
    def capacity(self):
        return self.__capacity

    def enlist(self,cossack:Cossack):
        if self.capacity==len(self.cossacks):
            return "Sich perepovnena"
        else:
            if isinstance(cossack,Cossack):
                self.__cossacks.append(cossack)
                return f"Cosak {cossack.name} joined to Sich {self.name}"
            else:
                raise("You should enlint Cossack only object") 

    def desmis(self,cossack_name:str):
        for cossack in self.cossacks:
            if cossack.name==cossack_name:
                self.__cossacks.remove(cossack)
                return f"Cossack {cossack_name} was successfuly dismissed from Sich {self.name}"
        return f"Cossack with name {cossack_name} not found on Sich {self.name}"

    def call_to_battle(self,enemy):
        if len(self.cossacks) ==0:
            return "No Cossacks on Sich"
        else:
            return f"Zaporizka army stand up to {enemy}! There are {len(self.cossacks)} Cossacks!"

    def best_warrior(self):
        if len(self.__cossacks) == 0:
            return "Sich is empty"
        return max(self.__cossacks,key=lambda cossack: cossack.victories)

    def roster(self):
        if len(self.cossacks) == 0:
            return "Nobody on Sich"
        return self.cossacks

    def promote_all(self):
        if len(self.__cossacks) == 0:
            return "No Cossacks on Sich to promote."
        for cossack in self.__cossacks:
            cossack.promote()
        return "All cossacks on the Sich have been checked for rank promotions!"

# Створюємо козаків
cossack1 = Cossack("Іван Сірко", "Кальміуський")
cossack2 = Cossack("Петро Сагайдачний", "Канівський")
cossack3 = Cossack("Максим Залізняк", "Чигиринський")

# Демонстрація озброєння та перевірки наявності зброї
cossack1.arm("шабля")
cossack1.arm("мушкет")
cossack1.arm("шабля")  # Спроба додати вже наявну зброю

cossack2.arm("шабля")
cossack3.arm("пістоль")

# Проводимо битви для набору перемог та зміни звань
print(cossack1.win_battle("яничари"))
print(cossack1.win_battle("татари"))
print(cossack1.win_battle("москалі"))  # 3 перемоги — має стати осавулом

for _ in range(4):
    cossack1.win_battle("вороги")  # Ще 4 перемоги (всього 7) — має стати полковником

print(cossack2.win_battle("кацапи"))

# Створюємо Січ та зараховуємо козаків
sich = ZaporozhianSich("Чортомлицька Січ", capacity=3)

print(sich.enlist(cossack1))
print(sich.enlist(cossack2))
print(sich.enlist(cossack3))
print(sich.enlist(Cossack("Богдан", "Суботівський")))  # Перевірка на переповнення Січі

# Демонстрація інших методів Січі
print("\n--- Виклик до бою ---")
print(sich.call_to_battle("султана"))

print("\n--- Найкращий воїн ---")
print(sich.best_warrior())

print("\n--- Масове оновлення звань ---")
print(sich.promote_all())

print("\n--- Повний список козаків (Roster) ---")
print(sich.roster())

print("\n--- Звільнення козака ---")
print(sich.desmis("Петро Сагайдачний"))
print(sich.roster())