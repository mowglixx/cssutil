
import os
import random

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Player:

    # construct a 'Player'
    def __init__(
        self, 
        name: str, 
        health: int = 100, 
        level: int = 0, 
        xp: int = 0, 
        class_name: str = 'Warrior', 
        inventory: list = []
        ):
            self.name = name
            self.health = health
            self.level = level
            self.xp = xp
            self.class_name = class_name
            self.inventory = inventory

    # set_health()
    def set_health(self, amount):
        self.health = amount

    # set_name()
    def set_name(self, name):
        self.name = name

    # set_level()
    def set_level(self, level):
        self.level = level

    # set_xp()
    def set_xp(self, xp):
        self.xp = xp

    # set_class_name()
    def set_class_name(self, class_name):
        self.class_name = class_name

    # set_inventory()
    def set_inventory(self, inventory):
        self.inventory = inventory

# def

def player_choice(prompt: str = 'Make a choice:', choices: list = ['Y', 'N', 'Run away']):
    
    print(f'{prompt}')
    choices_len = len(choices)
    counter = 0
    while counter < choices_len:
        print(f'  {counter}. {choices[counter]}')
        counter += 1
    choice = input(f'[0, {choices_len}]: ')

    try:
        int(choice)
        
        if choice == '0':
            choice = 0
        else:
            choice = int(choice)
        
        if choice > -1 and choice < choices_len:
            return choices[choice]
    except:
        player_choice(prompt, choices)


def game(player: Player = Player('Harry')):
    print(f'Hello, {player.name}, this is going to be a great adventure!')
    
    choices = ['Add Health', 'Lose Health', 'Game Over']
    compliments = [
        'Well done!',
        'Good Job',
        'Keep it up',
        'You\'re filled with determination',
    ]
    insults = [
        'you did this to yourself...', 
        'I can\'t believe you\'ve done this...',
        'you should learn from this...',
        'Try again.',
        'Basic Bitch!',
        'Hoe!',
        'I think you have daddy issues..',
        'grab another beer man..',
        ]
    player_input = player_choice('Gimme input, player!!!', choices)
    print(player_input)
    # add health
    if player_input == choices[0]:
        player.set_health(player.health+20)
        clear_screen()
        print(player.health, f'Health, {random.choice(compliments)}\n' )
    # lose health
    elif player_input == choices[1]:
        player.set_health(player.health-20)
        clear_screen()
        print(player.health, f'Health, {random.choice(insults)}\n' )
    else:
        player.set_health(0)


def game_over():
    print('Game over')

player_name = player_choice('Please choose a name:', ['Harry', 'Ron', 'Hermy'])

player = Player(player_name, class_name='Wizard')

while player.health > 0:
    game(player)
game_over()