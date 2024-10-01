from character import Ememy

dave = Ememy('Dave', 'a smelly zombie')

dave.describe()

dave.set_conversation('hello there Im going to join your game soon')
                      
dave.talk()

dave.set_weakness('cheese')

print('what will you fight with?')
fight_with = input('enter item here')
dave.fight(fight_with)
