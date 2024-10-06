from room import Room
from character import Ememy
from character import Character

kitchen = Room("kitchen")
ballroom = Room("ballroom")
dining_hall = Room("dining Room")

kitchen.set_description("a dank and dirty room with flies")

ballroom.set_description("a large room with a dance floor")

dining_hall.set_description("a large room with a dining table")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

#dining_hall.get_details()
dave = Ememy('dave', 'a smelly zombie')
dave.set_conversation('brrrlgh rghl brains')
dave.set_weakness('cheese')
dave.set_combat_item('cheese')

kate = Ememy('kate', 'a witch')
kate.set_conversation('I will cast  spell on you')
kate.set_weakness('garlic')
kate.set_combat_item('garlic')

aaron = Character('aaron', 'a friend')
aaron.set_conversation('To defeat Dave use cheese, and to defeat kate use garlic')

kitchen.set_character(kate)
dining_hall.set_character(dave)
ballroom.set_character(aaron)

current_room = kitchen
while True:
      print('\n')
      current_room.get_details()
      inhabitant = current_room.get_character()
      
      if inhabitant is not None:
          inhabitant.describe()
          print (f'do you want to speak to {inhabitant.name}? ')

          reponse = input('enter y or n > ')
          if reponse == 'y':
            print("What do you want to say? >")
            talk = input('>')  # Trigger conversation with the character
            inhabitant.talk()
          elif reponse == 'n':
            print("You chose not to speak.")

      if inhabitant is not None and inhabitant != aaron:
      #if inhabitant is not None:
          print (f'do you want fight {inhabitant.name}? ')
          reponse = input('enter y or n > ')
          if reponse == 'y':
             combat_item = input('what will you fight with?>')
             if inhabitant.fight(combat_item):
                current_room.set_character(None)
                print(f'{inhabitant.name} has been defeated.')
             else:
                print('Game over! You lost the fight.')
                break
             
          elif reponse == 'n':
            print("You chose not to fight.")
          elif inhabitant == aaron:
            print('Good luck)') 
    

      command = input('where do you want to go enter a direction> ')
      current_room = current_room.move(command)
      
    
      
      










