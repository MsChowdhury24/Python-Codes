print("Welcome to Treasure Island.Your mission is to find the treasure.")
choice1 = input('Choose which diection you wanna go.\n'
      'Type "R" to go right and Type "L" to go left.\n')
      
if choice1 == "L":
    print("Yay!! You found the river.")
    choice2 = input('How do you wanna cross the river?\n' 
                     'type "swim" to swim across the river.\n' 
                     'Type "arrive" to summon a boat.\n')
    if choice2 == "arrive":
        print("YOUR BOAT HAS ARRIVED\n.")
        choice3 = input('YAY! YOU REACHED THE ISLAND UNHARMED.\n'
               'there are three cristals, one "yellow", one "red" and one "blue",one of them will take you to the treasure.\n'
               'which cristal do you choose?\n')
        if choice3 == "yellow":
            print("CONGRATULATIONS!! YOU FOUND THE TREASURE.")
        elif choice3 == "red":
            print("YOU FELL INTO FIRE.GAME OVER")
        elif choice3== "blue":
            print("YOU WERE BITTEN BY SNAKES.GAME OVER.")
        else:
            print("OH NO!! THE ISLAND GOT SUBMERGED. GAME OVER. ")
    else:
        print('OH NO!! YOU WERE EATEN BY THE THREE TAILED BEAST "ISOBU".GAME OVER')
        
        
else:
    print("OH NO!! YOU FELL OFF THE CLIFF. GAME OVER")
      
******************************************************OUTPUT*************************************************************************************

Welcome to Treasure Island.Your mission is to find the treasure.
Choose which diection you wanna go.
Type "R" to go right and Type "L" to go left.
L
Yay!! You found the river.
How do you wanna cross the river?
type "swim" to swim across the river.
Type "arrive" to summon a boat.
arrive
YOUR BOAT HAS ARRIVED
.
YAY! YOU REACHED THE ISLAND UNHARMED.
there are three cristals, one "yellow", one "red" and one "blue",one of them will take you to the treasure.
which cristal do you choose?
yellow
CONGRATULATIONS!! YOU FOUND THE TREASURE.

=== Code Execution Successful ===
        
