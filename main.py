#importanting python stuff
import random

#Importanting arrays aka lists
from perks import survivorPerks
from perks import killerPerks

from characters import survivorsName
from characters import killersName

from KillerAddon import Trapper
from KillerAddon import Wraith
from KillerAddon import Hillbilly
from KillerAddon import Nurse
from KillerAddon import Shape
from KillerAddon import Hag
from KillerAddon import Doctor
from KillerAddon import Huntress
from KillerAddon import Cannibal
from KillerAddon import Nightmare
from KillerAddon import Pig
from KillerAddon import Clown
from KillerAddon import Spirit
from KillerAddon import Legion
from KillerAddon import Plague
from KillerAddon import Ghost_Face
from KillerAddon import Demogorgon
from KillerAddon import Oni
from KillerAddon import Deathslinger
from KillerAddon import Executioner

from Allitems import items
from ItemAddons import Toolbox
from ItemAddons import Map
from ItemAddons import Flashlight
from ItemAddons import Key
from ItemAddons import Medkit

#Saying who made it
print("Original creator - LonlyGamerX - twitch.tv/LonlyGamerX")
print("")

#Asking if the person wants survivor or killer randomizer
Question1 = None
while Question1 not in ("survivor", "killer"):
    Question1 = input('Which randomizer do you want, survivor or killer?: ')
    if Question1.lower() == 'survivor':
        print(
            "Alright you picked Survivor. Have fun hiding from the killer uwu."
        )
    elif Question1.lower() == 'killer':
        print(
            "Alright you picked killer. Have fun murdering the survivors uwu.")
    else:
        print("Please type survivor or killer. Note its not case sensitive!")

#Randomizing character to play depending on if which is picked survivor or killer
if Question1.lower() == 'survivor':
    CharacterName = random.choice(survivorsName)
elif Question1.lower() == 'killer':
    CharacterName = random.choice(killersName)

#Randomizing Killer addon if you picked killerPerks part 1
if CharacterName == "Trapper":
    Addon1 = random.choice(Trapper)
    Addon2 = random.choice(Trapper)
elif CharacterName == "Wraith":
    Addon1 = random.choice(Wraith)
    Addon2 = random.choice(Wraith)
elif CharacterName == "Hillbilly":
    Addon1 = random.choice(Hillbilly)
    Addon2 = random.choice(Hillbilly)
elif CharacterName == "Nurse":
    Addon1 = random.choice(Nurse)
    Addon2 = random.choice(Nurse)   
elif CharacterName == "Shape":
    Addon1 = random.choice(Shape)
    Addon2 = random.choice(Shape)   
elif CharacterName == "Hag":
    Addon1 = random.choice(Hag)
    Addon2 = random.choice(Hag)  
elif CharacterName == "Doctor":
    Addon1 = random.choice(Doctor)
    Addon2 = random.choice(Doctor) 
elif CharacterName == "Huntress":
    Addon1 = random.choice(Huntress)
    Addon2 = random.choice(Huntress)  
elif CharacterName == "Cannibal":
    Addon1 = random.choice(Cannibal)
    Addon2 = random.choice(Cannibal) 
elif CharacterName == "Nightmare":
    Addon1 = random.choice(Nightmare)
    Addon2 = random.choice(Nightmare)

#Randomizing addons and item
PickedItem = random.choice(items)

#Flashlight addons
if PickedItem == 'Flashlight':
  ItemAddon1 = random.choice(Flashlight)
  ItemAddon2 = random.choice(Flashlight)
elif PickedItem == 'Sport Flashlight':
  ItemAddon1 = random.choice(Flashlight)
  ItemAddon2 = random.choice(Flashlight)
elif PickedItem == 'Utility Flashlight':
  ItemAddon1 = random.choice(Flashlight)
  ItemAddon2 = random.choice(Flashlight)

#Key addons
if PickedItem == 'Broken Key':
  ItemAddon1 = random.choice(Key)
  ItemAddon2 = random.choice(Key)
elif PickedItem == 'Dull Key':
  ItemAddon1 = random.choice(Key)
  ItemAddon2 = random.choice(Key)
elif PickedItem == 'Skeleton Key':
  ItemAddon1 = random.choice(Key)
  ItemAddon2 = random.choice(Key)

#Map addons
if PickedItem == 'Map':
  ItemAddon1 = random.choice(Map)
  ItemAddon2 = random.choice(Map)
elif PickedItem == 'Rainbow Map':
  ItemAddon1 = random.choice(Map)
  ItemAddon2 = random.choice(Map)

#Medkit addons
if PickedItem == 'Camping Aid Kit':
  ItemAddon1 = random.choice(Medkit)
  ItemAddon2 = random.choice(Medkit)
elif PickedItem == 'First Aid Kit':
  ItemAddon1 = random.choice(Medkit)
  ItemAddon2 = random.choice(Medkit)
elif PickedItem == 'Emergency Med-Kit':
  ItemAddon1 = random.choice(Medkit)
  ItemAddon2 = random.choice(Medkit)
elif PickedItem == 'Ranger Med-Kit':
  ItemAddon1 = random.choice(Medkit)
  ItemAddon2 = random.choice(Medkit)

#ToolBox addons
if PickedItem == 'Worn-Out Tools':
  ItemAddon1 = random.choice(Toolbox)
  ItemAddon2 = random.choice(Toolbox)
elif PickedItem == 'Toolbox':
  ItemAddon1 = random.choice(Toolbox)
  ItemAddon2 = random.choice(Toolbox)
elif PickedItem == 'Mechanic\'s Toolbox':
  ItemAddon1 = random.choice(Toolbox)
  ItemAddon2 = random.choice(Toolbox)
elif PickedItem == 'Commodious Toolbox':
  ItemAddon1 = random.choice(Toolbox)
  ItemAddon2 = random.choice(Toolbox)
elif PickedItem == 'Engineer\'s Toolbox':
  ItemAddon1 = random.choice(Toolbox)
  ItemAddon2 = random.choice(Toolbox)
elif PickedItem == 'Alex\'s Toolbox':
  ItemAddon1 = random.choice(Toolbox)
  ItemAddon2 = random.choice(Toolbox)

#Randomizing Killer addon if you picked killerPerks part 2
if CharacterName == "Pig":
    Addon1 = random.choice(Pig)
    Addon2 = random.choice(Pig)  
elif CharacterName == "Clown":
    Addon1 = random.choice(Clown)
    Addon2 = random.choice(Clown)
elif CharacterName == "Spirit":
    Addon1 = random.choice(Spirit)
    Addon2 = random.choice(Spirit)   
elif CharacterName == "Legion":
    Addon1 = random.choice(Legion)
    Addon2 = random.choice(Legion)  
elif CharacterName == "Plague":
    Addon1 = random.choice(Plague)
    Addon2 = random.choice(Plague)  
elif CharacterName == "Ghost Face":
    Addon1 = random.choice(Ghost_Face)
    Addon2 = random.choice(Ghost_Face)  
elif CharacterName == "Demogorgon":
    Addon1 = random.choice(Demogorgon)
    Addon2 = random.choice(Demogorgon)
elif CharacterName == "Oni":
    Addon1 = random.choice(Oni)
    Addon2 = random.choice(Oni)    
elif CharacterName == "Deathslinger":
    Addon1 = random.choice(Deathslinger)
    Addon2 = random.choice(Deathslinger)
elif CharacterName == "Executioner":
    Addon1 = random.choice(Executioner)
    Addon2 = random.choice(Executioner)

#Randomizing perks 1 to 4 for survivor if picked survivor
if Question1.lower() == 'survivor':
    Perk1 = random.choice(survivorPerks)
    Perk2 = random.choice(survivorPerks)
    Perk3 = random.choice(survivorPerks)
    Perk4 = random.choice(survivorPerks)
elif Question1.lower() == 'killer':
    Perk1 = random.choice(killerPerks)
    Perk2 = random.choice(killerPerks)
    Perk3 = random.choice(killerPerks)
    Perk4 = random.choice(killerPerks)

#Printing the msg to the compile
print("")
if Question1.lower() == 'survivor':
    print("Survivor: " + CharacterName)
elif Question1.lower() == 'killer':
    print("Killer: " + CharacterName)
print("")
if Question1.lower() == 'killer':
  print("Addon 1: " + Addon1)
  print("Addon 2: " + Addon2)
  print("")
elif Question1.lower() == 'survivor':
  print("Item: " + PickedItem)
  print("Addon 1: " + ItemAddon1)
  print("Addon 2: " + ItemAddon2)
  print("")
print("Perk 1: " + Perk1)
print("Perk 2: " + Perk2)
print("Perk 3: " + Perk3)
print("Perk 4: " + Perk4)