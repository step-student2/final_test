# Варіант 1
import random


class Wizard:
    spells = [
        {
            'name': 'fireball',
            'damage': 10,
            'heal': 0
        },
             {
            'name': 'metabolism',
            'damage': 0,
            'heal': 8
        }
    ]

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_damage = 50

    def attack(self, enemy, spell_id):
        damage = __class__.spells[spell_id]['damage']
        print(f"{self.name} використовує заклинання та наносить {damage} урону {enemy.name}")
        enemy.health -= damage

    def is_dead(self):
        return self.health <= 0


class WizardDuel:
    def __init__(self, wizard_player, wizard_bot):
        self.wizard_player = wizard_player
        self.wizard_bot = wizard_bot

    def play(self):
        print(f"Чарівник {self.wizard_player.name} змагається проти чарівника {self.wizard_bot.name}")
        print("Гра почалась!")

        while True:
            if self.wizard_player.is_dead():
                print(f"Чарівник {self.wizard_player.name} програв")
                break

            if self.wizard_bot.is_dead():
                print(f"Чарівник {self.wizard_bot.name} програв")
                break

            print('''Виберіть заклинання: 
            -----------------------------
            ''')
            # вивести циклом перелік

            choice = int(input()) - 1

            self.wizard_player.attack(self.wizard_bot, choice)
            self.wizard_bot.attack(self.wizard_player, 0)



if __name__ == '__main__':
    wizard1 = Wizard('Гаррі')
    wizard2 = Wizard('Дамблдор')
    game = WizardDuel(wizard1, wizard2)
    game.play()
