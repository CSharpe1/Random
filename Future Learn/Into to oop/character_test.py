from character import Character
from character  import  Enemy

dave    =   Enemy("Dave", "A smelly Zombie!", "Talk to ME")
dave.describe()
person  =   Character("User", "just a person", "...")
dave.talk()
dave.set_conversation("I don't smell THAT Bad do I...?")
dave.talk()
person.talk()
dave.set_conversation("...[glare]")
dave.talk()
person.set_conversation("Not That... Bad... But yeah not good :(")
person.talk()
dave.set_conversation("[Cries], leave me alone now")
dave.talk()
person.set_conversation("Sorry but I think its time to FIGHT!!!!")
person.talk()

dave.set_weakness("silver knife")

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)



