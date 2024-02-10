# Author: Vam 24060828
# Date: 12/01/2024

'''
Sci-fic Python Text Based Game
___CYBER ESCAPE___
'''

import os.path

class Scenario(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

# Create Items
    # Detain Room Items
surrounding = Item("Surrounding", "\nThe room is a remnant of the past. Dim neon lights flicker, revealing worn-out walls adorned with faded murals. The air is heavy with a mixture of metallic and aged odours.\nA run-down likely computer in the corner.\n")
escape_door = Item("Door","\nThe only exit is a sturdy metallic door, adding an extra layer of mystery to your predicament.")
    # Computer Items
screen = Item("Computer Screen", "\nYou log in as <guest>, discovering an internal network.\n")
network = Item("Network", "\nThis ancient computer surprisingly connected to the internet, which might be the old WAP setting in the first days of this building. It could have gone unnoticed by The Collective due to its outdated appearance.")
admin = Item("Admin", "\nYou now are able to disable the cameras temporarily, giving you an hour to navigate the facility without being under surveillance.")

# Create Scenarios
    # Detain Room
detain_room = Scenario("Detain Room", "\nYou woke up in a dimly lit room, surrounded by the low buzz of fluorescent lights.\n")
detain_room.items.append(surrounding)
detain_room.items.append(escape_door)   
    # Computer
computer = Scenario("Computer", "\nA run-down likely computer in the corner seems to be your only hope.")
computer.items.append(screen)
computer.items.append(network)
computer.items.append(admin)  

# Create Player
player = Player("CipherBunnie", detain_room)

# Introduction
def introduction():
    print("_____Welcome to CYBER ESCAPE_____")
    print("\nIn the year 2111, amidst a world dominated by powerful conglomerates, you are CipherBunnie - ")
    print("\na mysterious hacker with a reputation that inspires both respect and fear.")
    print("\nOne day, an elusive organisation known as The Collective approached you with an audacious offer - a million-dollar deal to breach the Government impenetrable system.")
    print("\nFirm in your principles, you rejected the proposal.")
    print("\nHowever, The Collective would never give up on their purpose...\n")
    print("\nType > enter to start the game.")
introduction()

# Command List
cmd_lst = ['enter', 'wq', 'help', 'move', 'look', 'examine computer', 'examine camera', 'admin login', 'sql injection', 'inventory', 'escape']

# Gameplay Dictionary Function
def game_play():
    print("\nenter: Start the game.")
    print("\nwq: Save your progress and exit.")
    print("\nhelp: Open the gameplay dictionary.")
    print("\nlook: Scrutinize your surroundings.")
    print("\nmove: Explore and reveal hidden secrets.")
    print("\nexamine + computer/camera: Investigate for hidden clues.")
    print("\nadmin login/sql injection: Use your hacking skills to overcome obstacles and manipulate security systems.")
    print("\ninventory: Open your inventory to view found tools.")
    print("\nescape: Attempt to escape using your gathered materials.")

# Save and Load Game Progress Functions
def save(scenario):
    with open("loadfile.txt", "w") as file:
        file.write(scenario)

def load():
    if os.path.isfile("loadfile.txt"):
        with open("loadfile.txt", "r") as file:
            return file.read().strip()

# Load Scenarios Function
def load_scenario():
    scenario_name = load()
    if scenario_name == "Detain Room":
        player.location = detain_room
        print("You come back in the Detain room.")
    elif scenario_name == "Computer":
        player.location = computer
        print("You comeback in front of the Computer.")


while True:
    # Get Player Input
    player_input = input("\n> ")
    
    # Validate Player Input Function
    def validate_input(cmd_lst):
        valid_player_input = player_input.lower()
        if valid_player_input in cmd_lst:
            return valid_player_input
        else:
            print("Invalid command. Try again.\nEnter > help to open Gameplay.")

    # Use Validate Input Function to Return Valid Player Command
    player_command = validate_input(cmd_lst)

    # help
    if player_command == 'help':
        game_play()
        
    # enter
    if player_command == 'enter':
        load_scenario()
        print("\nThe strange surroundings trigger panic - you realise you might've been kidnapped.")  

    # move
    if player_command == 'move':
        if player.location == detain_room:
            player.location = computer
            print("You are now sitting in front of the computer.")
        elif player.location == computer:
            player.location = detain_room
            print("You are now standing in the middle of the detain room.")
        
    # look
    if player_command == 'look' and player.location == detain_room:
        print(detain_room.description)
        for item in detain_room.items:
            print(f"{item.description}\n") 

    # examine
    if player_command == 'examine camera' and player.location == computer:
        if 'admin' in player.inventory:
            player.inventory.append('camera')
            print("A blank lobby filled with cameras, guards patrol tirelessly.")
    if player_command == 'examine computer' and player.location == computer:
        for item in computer.items:
            if item.name in ["Computer Screen", "Network"]:
                print(f"{item.name}: {item.description}\n") 

    # admin login
    if player_command == 'admin login' and player.location == computer:
        for item in computer.items:
            if item.name in ["Admin"]:
                print(item.description)
        player.inventory.append('admin')
        
    # sql injection
    if player_command == 'sql injection' and player.location == computer:
        if 'camera' in player.inventory:
            for item in computer.items:
                if item.name in ["Database"]:
                    print(item.description)
            player.inventory.append('blueprint')
            print("You just did a SQL Injection attack into The Collective database system and found out this building's blueprint.\nIt revealed a secret path outside - offers a potential escape out without being noticed.")

    # inventory
    if player_command == 'inventory':
        print(player.inventory)
    
    # escape
    if player_command == 'escape':
        if len(player.inventory) == 3:
            print("WINNER!!! enteYou successfully evade The Collective and emerge as a free hacker.")
            exit()
        else:
            print("The guards found you. Without saying a word, they pull their laser guns. Game over.")
            exit()
    
    # wq
    if player_command == 'wq':
        print("Saving game...")
        save(player.location.name)
        exit()





        


