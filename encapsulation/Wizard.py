class Wizard:
    def get_fireballed(self):
        self.__health -=   30
        print(f"{self.name} is hit")
        if self.__health <= 0:
            print(f"{self.name} is dead")
    
    def drink_mana_potion(self):
        print(f"{self.name} drinks a portion")
        self.__mana += 40



    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health


def main():
    merlin = Wizard("Merlin")
    print_status(merlin)
    merlin.drink_mana_potion()
    print_status(merlin)

    madame_mim = Wizard("Madame Mim")
    print_status(madame_mim)
    madame_mim.get_fireballed()
    print_status(madame_mim)
    madame_mim.get_fireballed()
    print_status(madame_mim)
    madame_mim.get_fireballed()


def print_status(wizard):
    print(
        f"{wizard.name} has {wizard.get_health()} health and {wizard.get_mana()} mana"
    )


main()
