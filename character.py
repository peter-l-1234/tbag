class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description

    def talk_to(self):
        print(self.name)

    def describe(self):
        print(self.name + " is here " )
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation is not None:
            print(f"{self.name} says {self.conversation}") 
        else:
            print(f"{self.name} does not want to speak to you")

    def fight(self, combat_item):
        self.item = combat_item
        print(self.name +"does not want ot fight with you")
        return True
    
class Ememy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.conversation = None

    def set_weakness(self, item_weakness):
         self.weakness = item_weakness
    def get_weakness(self):
         return self.weakness
    def set_combat_item(self, combat_item):
         self.combat_item = combat_item
    
    

            
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f'you fend {self.name} off with {combat_item}')
            return True
        else:
            print(f'{self.name} crushes yuo puny adventrurer')
            return False
        
    
            




        
