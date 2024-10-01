from room import Room
from character import Ememy

kitchen = Room("kitchen")
ballroom = Room("ballroom")
dining_hall = Room("dining Room")

kitchen.set_description("a dank and dirty room with flies")
#print(kitchen.get_description())
#kitchen.describe()

ballroom.set_description("a large room with a dance floor")

dining_hall.set_description("a large room with a dining table")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

#dave = Character("Dave", )

#dining_hall.get_details()
dave = Ememy('dave', 'a smelly zombie')
dave.set_conversation('brrrlgh rghl brains')
dave.set_weakness('cheese')

kate = Ememy('kate', 'a witch')
kate.set_conversation('I will cast  spell on you')
kate.set_weakness('garlic')

kitchen.set_character(kate)
#dining_hall.set_character(dave)
current_room = kitchen
while True:
      print('\n')
      current_room.get_details()
      inhabitant = current_room.get_character()
      #talk = current_room.get_character()
      
      if inhabitant is not None:
          inhabitant.describe()
          print (f'do you want to speak to {inhabitant}? ')
          #talk.talk_to()
          #print ('enter y or n')
          reponse = input('enter y or n > ')
          if reponse == 'y':
            print("What do you want to say? >")
            talk = input('>')  # Trigger conversation with the character
            print(f'{inhabitant} says I will put a spell on you') #text from kate

          else:
            print("You chose not to speak.")



          #need to define self.conversation so th euser input is stored


      #command = input('>')
      #if command == 'y':
      # print ('what do you want to say?>')
        
      #else:
      command = input('where do you want to go enter a direction> ')
      current_room = current_room.move(command)
      
      
      #speak = self.conversation(command)
      
      










