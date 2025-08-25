import copy


class Warrior:
    attack = 5
    health = 30
    magic = 0
    splash = 0

    def __init__(self):
        self.attack = Warrior.attack
        self.health = Warrior.health
        self.magic = Warrior.magic
        self.splash = Warrior.splash

    def reset(self):
        return self

    def __str__(self):
        mag = str(self.magic)
        splash = str(self.splash*100)+'%'
        return f"Тип: {self.__class__.__name__}\nЗдоровье: {self.health} \nАтака: {self.attack}\n" + \
               f"{(self.magic>0)*('Магия:'+mag)}" + f"{(self.splash>0)*('Сплеш:'+splash)}\n"

    def __add__(self, other):
        self.health += other
        self.attack += other
        return self

    def __mul__(self, other):
        self.health *= other
        self.attack *= other
        return self

    @property
    def is_alive(self):
        return self.health > 0


class Fighter(Warrior):
    attack = 7

    def __init__(self):
        Warrior.__init__(self)
        self.attack = Fighter.attack


class Mage(Warrior):
    health = 40
    attack = 3
    magic = 6

    def __init__(self):
        Warrior.__init__(self)
        self.health = Mage.health
        self.attack = Mage.attack
        self.magic = Mage.magic


class Paladin(Warrior):
    health = 50
    attack = 6
    splash = 0.5

    def __init__(self):
        Warrior.__init__(self)
        self.health = Paladin.health
        self.attack = Paladin.attack
        self.splash = Paladin.splash


class Army:
    def __init__(self):
        self.army_arr = []

    def __add__(self, other):
        if isinstance(other, Warrior):
            copya = copy.deepcopy(other)
            self.army_arr.append(copya)
            return self
        for i in self.army_arr:
            i.health += other
            i.attack += other
        return self

    def __mul__(self, other):
        for i in self.army_arr:
            i.health *= other
            i.attack *= other
        return self

    def add_members(self, type, number):
        new_arr = [type() for i in range(number)]
        self.army_arr.extend(new_arr)
        return


def fight(war1, war2):
    while True:
        damage1 = war1.attack + war1.magic if war2.attack < war1.magic else war1.attack
        damage1 = damage1 - war2.magic if damage1 - war2.magic > 0 else 0
        Battle.next_damage1 += damage1*war1.splash
        Battle.pal_hit1 = damage1*war1.splash
        war2.health -= damage1
        if war2.health <= 0:
            return True
        damage2 = war2.attack + war2.magic if war1.attack < war2.magic else war2.attack
        damage2 = damage2 - war1.magic if damage2 - war1.magic > 0 else 0
        war1.health -= damage2
        Battle.next_damage2 += damage2 * war2.splash
        Battle.pal_hit2 = damage2 * war2.splash
        if war1.health <= 0:
            return False


class Battle:
    next_damage1 = 0
    next_damage2 = 0
    pal_hit1 = 0
    pal_hit2 = 0
    queue = 1

    @staticmethod
    def fight(army1, army2):
        while True:
            Battle.next_damage1 = 0
            Battle.next_damage2 = 0
            Battle.pal_hit1 = 0
            Battle.pal_hit2 = 0
            if Battle.queue == 1:
                win_duel = fight(army1.army_arr[0], army2.army_arr[0])
            elif Battle.queue == 2:
                win_duel = fight(army2.army_arr[0], army1.army_arr[0])
                Battle.next_damage1, Battle.next_damage2 = Battle.next_damage2, Battle.next_damage1
                Battle.pal_hit1, Battle.pal_hit2 = Battle.pal_hit2, Battle.pal_hit1
            if Battle.next_damage1 > 0 and len(army2.army_arr) >= 2 and army2.army_arr[1].health > 0 and \
                    army2.army_arr[0].health < 0:
                army2.army_arr[1].health -= army2.army_arr[0].health/2
            while Battle.next_damage1 > 0 and len(army2.army_arr) >= 2 and army2.army_arr[1].health > 0:
                dam = Battle.pal_hit1 - army2.army_arr[1].magic if Battle.pal_hit1 - army2.army_arr[1].magic > 0 else 0
                army2.army_arr[1].health -= dam
                Battle.next_damage1 -= Battle.pal_hit1

            if Battle.next_damage2 > 0 and len(army1.army_arr) >= 2 and army1.army_arr[1].health > 0 and \
                    army1.army_arr[0].health < 0:
                army1.army_arr[1].health -= army1.army_arr[0].health/2
            while Battle.next_damage2 > 0 and len(army1.army_arr) >= 2 and army1.army_arr[1].health > 0:
                dam = Battle.pal_hit2 - army1.army_arr[1].magic if Battle.pal_hit2 - army1.army_arr[1].magic > 0 else 0
                army1.army_arr[1].health -= dam
                Battle.next_damage2 -= Battle.pal_hit2
            if len(army1.army_arr) >= 2 and not army1.army_arr[1].is_alive:
                army1.army_arr.pop(1)
            if len(army2.army_arr) >= 2 and not army2.army_arr[1].is_alive:
                army2.army_arr.pop(1)
            if not army1.army_arr[0].is_alive:
                army1.army_arr.pop(0)
                Battle.queue = 1
            if not army2.army_arr[0].is_alive:
                army2.army_arr.pop(0)
                Battle.queue = 2
            if len(army1.army_arr) == 0:
                return False
            elif len(army2.army_arr) == 0:
                return True

c = Mage() +3
d = Mage() +4
print(c)
print(d)
print(fight(c,d))
print(c)