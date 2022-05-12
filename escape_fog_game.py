import time
import sys

#This is the intro to the game, giving players the theme and mission
def main ():
    print()
    print("An emergency boardcast has just went out")
    print("The planet you've been conduting research on has started to deteriorted")
    print("You must get to the spaceship before the planet evaporates or risk evaporating along with it")
    print()
    #time.sleep(2)


#askes the player if they want to play the game
def start_game ():
    start = input("Would you like to play the game? (yes or no) ")
    if start.lower().strip() == "yes":
        print("Game On")
        time.sleep(2)
    else:
        print("Goodbye")
        sys.exit()
        

#this is where all players start if they choose to play the game
def level_0_lab():
    print("You are working in the Laboratory")
    print("The evaction call sounds the alarm")
    print("The planet's suface is eating away by a mysterious FOG")
    print("The Space will be leaving very soon, You must make there is you wan to survive!")
    time.sleep(2)
    exit_lab = input("Leave Labtory? (yes or no):  ")
    if exit_lab == "yes":
        level_1_room()
    else:
        print("Game Over")
        sys.exit()
    #elif exit_lab == "no":
      #  level_0_lab()
    #else:
     #   level_0_lab
    #while exit_lab != "yes" and exit_lab != "no":
       # exit_lab = input("Leave Labtory? (yes or no):  ").lower().strip()
       # if exit_lab == "no":
       #     return exit_lab()
    #return exit_lab

def level_1_room():
    room_options = ["hallway" ,"office", "supplies", "locker room", "director office",  "stair way",]
    player_choice =""
    while player_choice not in room_options:  
        print("You are in the Hallway. There are several rooms for you to go")
        print("You must find a set of Keys and a Passcode in one or more of the rooms")
        time.sleep(2)
        print("office")
        print("supplies")
        print("hallway")
        print("locker room")
        print("director office")
        print("stair way")
        player_choice = input("Type in room choice: ").lower().strip()
        
        #return player_choice()
    #level_1_room

    #player_choice = input("You are in the: " + player_choice)
    if player_choice == room_options[0]:
        hallway_room()
    elif player_choice == room_options[1]:
        office_room()
    elif player_choice == room_options[2]:
        supply_room()
    elif player_choice == room_options[3]:
        locker_room()
    elif player_choice == room_options[4]:
        director_office()
    elif player_choice == room_options[5]:
        stair_way()
    
#inventory list of items player must pick up in rooms
inventory = []

def hallway_room():
    print("\n")
    level_1_room()

def stair_way():
    #roof_top_access = ["roof top"]
    print("\n")
    print("You are in the stair way")
    print("Red emergency lights illuminate the concrete steps and blue painted walls")
    print("There is a door at the top of the stairs")
    user = input("Go up steps? ")
    #user =""
    if user == "yes":
        roof_top()
    else:
        level_1_room()

def roof_top():
    print("\n")
    print("You have access the roof top")
    print("The sky is a light purple shade")
    print("As the planet is evaporting right before your eyes. You  are swept up in the air")
    time.sleep(2)
    print("Game over")
    sys.exit()

#Office Room, there is a set of keys the player must get
def office_room():
    print("\n")
    print("You are in the Office")
    print("Its dark. You stumble and bump into a desk")
    print("there is a set of keys on the desk.")
    #print("Do you want to pick up keys?")
    pickup = input("Do you want to pick up keys? (yes or no) ").lower().strip()
    if pickup == "yes":
        #add_to_inventory("keys")
        inventory.append("keys") 
        print("You have added the keys to your inventory")
        print(inventory)
        time.sleep(3)
        #asking player to leave, if not player gets kickout of room anyway
        print("theres is nothing else to do in this room. Return to hallway?")
        leave = input()
        if leave == "yes" or "hallway":
            level_1_room()
        else:
            leave = input("there is nothing else to do in this room")
            time.sleep(5)
            level_1_room()
    else:
        print("okay")
        time.sleep(3)
        level_1_room()

#this room has nothing in it that helps the player win the game
def supply_room():
    print("\n")
    print("You are in the Supply room. There is a mop and broom in the coner")
    print("Cleaning supplies are in a cabinet in front of you")
    print("There is nothing useful in this room")
    leave = input()
    if leave == "leave" or "hallway":
        level_1_room()
    else:
        supply_room()

 #the player must have both key and passcode to complete this room and win the game 
def locker_room():
    print("Door is lock you need keys to open the door")
    time.sleep(2)
    if "keys" in inventory:
        print("You are in the Locker Room")
    else:
        print("You need to find keys to open the door")
        time.sleep(2)
        level_1_room()
    print("It is derserted.")
    print("To your left you see that some of the lockers against the wall have been push aside")
    print("Behind them is a sercert elevator that will take you quickly to the space shuttle")
    time.sleep(2)
    print("Do you have the code")
    if "passcode" in inventory:
        print("You have access the sercret transport elevator")
        space_shuttle()
    else:
        ("You must find the passcaode")
        level_1_room()

#this room has the passcode the player needs to get to sercert elevator  
def director_office():
    print("You are in the director's office")
    print("Its a very large room, with a leather sofa and a big brown desk")
    print("The lights are on, the place has been trashed")
    print("You look around the piles of papers and folders and see a folder labeled passcodes")
    open_folder = input("Do you want to open the folder?")
    if open_folder == "yes":
        print("You have found the passcode to the Elevator")
        print("passcode")
    pickup = input("Add passcode to inventory?")
    if pickup == "yes":
        #add_to_inventory("passcode")
        inventory.append("passcode") 
        time.sleep(3)
        print("You have added the passcode to your inventory")
        print(inventory)
        time.sleep(3)
        print("There is nothing else to do in this room")
        print("Do you want to leave room? ")
        leave = input()
        if leave == "yes" or "hallway":
            level_1_room()
    else:
        print("okay")
        level_1_room()

#this is the last rooom, player wins the game
def space_shuttle():
    print("You have gotten to the Space Shuttle")
    time.sleep(2)
    print("Just in time")
    time.sleep(2)
    print("You Won")
    print("Game Over")
    sys.exit()
    
main()
start_game()
level_0_lab()
#level_1_room()
