import random
import time

board = [['  -  ' for n in range(10)] for n in range(10)]
board2 = [['  -  ' for n in range(10)] for n in range(10)]
board3 = [['  -  ' for n in range(10)] for n in range(10)]
board4 = [['  -  ' for n in range(10)] for n in range(10)]

ships_fleet = ['Man-O-War = 5','Frigate = 4','Brig = 3','Galleon = 3','Schooner = 2']
ships_fleet_2 = ['Man-O-War = 5','Frigate = 4','Brig = 3','Galleon = 3','Schooner = 2']

enemy_ships = '  '.join(str(n) for n in ships_fleet)
enemy_ships_2 = '  '.join(str(n) for n in ships_fleet_2)

ships = {'  #  ': 5, '  @  ': 4, '  *  ': 3, '  !  ': 3, '  &  ': 2}

numbers = {"A":1,"a":1,"B":2,'b':2, "C":3, 'c':3,
          "D":4,"d":4,"E":5,'e':5, "F":6, 'f':6,
          "G":7,"g":7, "H":8,'h':8, "I":9, 'i':9,
          "J":10,"j":10 }
hits = 0
attacks = 0
miss = 0

hits2 = 0
attacks2 = 0
miss2 = 0

ship1 = True
ship2 = True
ship3 = True
ship4 = True
ship5 = True
fleet = 5

ship1_2 = True
ship2_2 = True
ship3_2 = True
ship4_2 = True
ship5_2 = True
fleet_2 = 5

turn = True
turn2 = True

def make_board(board):
    print('                                                             ')
    print('                                                             ')
    print(' ',' '.join("   1 -  -2  - -3    -4-    5-    6-   -7    -8    -9   -10".split('-')))
    for n, i in zip(" A- B- C- D- E- F- G- H- I- J".split('-'), board):
        print(n,' '.join(i))
    print('_____________________________________________________________')
    print(f"   Attacks:{attacks}       Missed:{miss}       Hits:{hits}      Ships left: {fleet}                    ")
    print('_____________________________________________________________')
    print("")
    print(f"Enemy Fleet In Battle:  {enemy_ships}                                     ")
    print('')

def make_board_player2(board):
    print('                                                             ')
    print('                                                             ')
    print(' ',' '.join("   1 -  -2  - -3    -4-    5-    6-   -7    -8    -9   -10".split('-')))
    for n, i in zip(" A- B- C- D- E- F- G- H- I- J".split('-'), board):
        print(n,' '.join(i))
    print('_____________________________________________________________')
    print(f"   Attacks:{attacks2}       Missed:{miss2}       Hits:{hits2}      Ships left: {fleet_2}                    ")
    print('_____________________________________________________________')
    print("")
    print(f"Enemy Fleet In Battle:  {enemy_ships_2}                                     ")
    print('')

def in_bound(board, loc, loc2):
        while True:
            try:
                return board[loc - 1][loc2 - 1] == '  -  ' or board[loc - 1][loc2 - 1] in ships
            except IndexError :
                return False
            except TypeError :
                return False
            except ValueError :
                return False
            except NameError :
                return False

def input_move(message):
    global move1,move2
    while True:
        try:
            move1, move2 = [int(n) if n.isdigit() else n for n in input(message).split()]  
            for key, value in numbers.items():
                if move1 == key:
                    move1 = value

            if move2 != int(move2):
                print(" ")
            break
        except ValueError:
            print('                                                           ')
            print (f"Captain that's not even on the map can someone please teach the Captain how to read")
        else:
            return move1,move2

def player_attack(board, board2, loc, loc2):
        hit = board[loc - 1][loc2 - 1]
        if hit in ships:
            board[loc - 1][loc2 - 1] = '  X  '
            board2[loc - 1][loc2 - 1] = '  X  '
        elif hit == '  -  ':
            board[loc - 1][loc2 - 1] = '  O  '
            board2[loc - 1][loc2 - 1] = '  O  '

def is_game_over(board,loc,loc2):
    global hits
    global attacks
    global miss
    hit = '  X  '
    if hit in board[loc - 1][loc2 - 1] :
            hits +=1
            attacks +=1
            print("We've hit a ship Captain")
            print(" ")
    else:
        miss +=1
        attacks +=1
        print(' We missed Captain')
        print(" ")

def is_game_over2(board,loc,loc2):
    global hits2
    global attacks2
    global miss2
    hit = '  X  '
    if hit in board[loc - 1][loc2 - 1] :
            hits2 +=1
            attacks2 +=1
            print("We've hit a ship Captain")
            print(" ")
    else:
        miss2 +=1
        attacks2 +=1
        print(' We missed Captain')
        print(" ")

def announce_ship(board):
    global ship1
    global ship2
    global ship3
    global ship4
    global ship5
    global fleet
    global ships_fleet
    global enemy_ships
    if ship1:
        if any("  #  " in ships for ships in board):
            None
        else:
            fleet -= 1
            ship1 = False
            ships_fleet.remove('Man-O-War = 5')
            enemy_ships = '  '.join(str(n) for n in ships_fleet)
            print('We have sunken the Man-O-War Captain ')
            
    if ship2:
        if any("  @  " in ships for ships in board):
            None
        else:
            fleet -= 1
            ship2 = False
            ships_fleet.remove('Frigate = 4')
            enemy_ships = '  '.join(str(n) for n in ships_fleet)
            print('We have sunken the Frigate Captain ')
    if ship3:
        if any("  *  " in ships for ships in board):
            None
        else:
            fleet -= 1
            ship3 = False
            ships_fleet.remove('Brig = 3')
            enemy_ships = '  '.join(str(n) for n in ships_fleet)
            print('We have sunken the Brig Captain ')
    if ship4:
        if any("  !  " in ships for ships in board):
            None
        else:
            fleet -= 1
            ship4 = False
            ships_fleet.remove('Galleon = 3')
            enemy_ships = '  '.join(str(n) for n in ships_fleet)
            print('We have sunken the Galleon Captain')
    if ship5:
        if any("  &  " in ships for ships in board):
            None
        else:
            fleet -= 1
            ship5 = False
            ships_fleet.remove('Schooner = 2')
            enemy_ships = '  '.join(str(n) for n in ships_fleet)
            print('We have sunken the Schooner Captain')

def announce_ship_player2(board):
    global ship1_2
    global ship2_2
    global ship3_2
    global ship4_2
    global ship5_2
    global fleet_2
    global ships_fleet_2
    global enemy_ships_2
    if ship1_2:
        if any("  #  " in ships for ships in board):
            None
        else:
            fleet_2 -= 1
            ship1_2 = False
            ships_fleet_2.remove('Man-O-War = 5')
            enemy_ships_2 = '  '.join(str(n) for n in ships_fleet_2)
            print('We have sunken the Man-O-War Captain ')
            
    if ship2_2:
        if any("  @  " in ships for ships in board):
            None
        else:
            fleet_2 -= 1
            ship2_2 = False
            ships_fleet_2.remove('Frigate = 4')
            enemy_ships_2 = '  '.join(str(n) for n in ships_fleet_2)
            print('We have sunken the Frigate Captain ')
    if ship3_2:
        if any("  *  " in ships for ships in board):
            None
        else:
            fleet_2 -= 1
            ship3_2 = False
            ships_fleet_2.remove('Brig = 3')
            enemy_ships_2 = '  '.join(str(n) for n in ships_fleet_2)
            print('We have sunken the Brig Captain ')
    if ship4_2:
        if any("  !  " in ships for ships in board):
            None
        else:
            fleet_2 -= 1
            ship4_2 = False
            ships_fleet_2.remove('Galleon = 3')
            enemy_ships_2 = '  '.join(str(n) for n in ships_fleet_2)
            print('We have sunken the Galleon Captain')
    if ship5_2:
        if any("  &  " in ships for ships in board):
            None
        else:
            fleet_2 -= 1
            ship5_2 = False
            ships_fleet_2.remove('Schooner = 2')
            enemy_ships_2 = '  '.join(str(n) for n in ships_fleet_2)
            print('We have sunken the Schooner Captain')

def valid_move(board, dict_value, x_position, y_position, choice):
    for b in range(dict_value):
        if choice:
            if board[x_position + b][y_position] != '  -  ':
                return False
        else:
            if board[x_position][y_position + b] != '  -  ':
                return False
    return True

def place_ships(board):
    for key, value in ships.items():
        valid = False
        while not valid:
            x, y = random.randint(0, 10 - value), random.randint(0, 10 - value)
            choice = random.choice([True, False])
            valid = valid_move(board, value, x, y, choice)

        for n in range(value):
            if choice:
                board[x + n][y] = key
            else:
                board[x][y + n] = key

time.sleep(1.0)
print(""" Welcome to Battleship a 2 player game or at least my version of it. 

The rules are simple:

1- Each captain has 5 ships in total 

2- Each captain has Man-O-War = 5  Frigate = 4  Brig = 3  Galleon = 3  Schooner = 2

3- The captain whos able to hit and sink all ships win 

4- If you hit or miss then it should be announced to the captain, if it doesnt announce then my code didnt work oooopps. 
Just kidding I tested until I started to pull my hair out of frustration it works ;)

5- Once you destroy a ship then it also should be announced to the captain

6- For now the ships are placed randomly, but I plan to make a second option for the player to place it themselves.


""")

time.sleep(5.0)

print('With that said and done the most important rule is for you to enjoy and have fun, so lets begin ')
print('')

place_ships(board)
place_ships(board3)
player1 = input('player 1 whats your Captain name ')
player2 = input('player 2 whats your Captain name ')

while turn or turn2  :
    while turn :
        time.sleep(3.0)
        print(f"                          {player1}'s  Map                         ")
        make_board(board2)
        print("Crew preparing the cannon's Captain ")
        
        time.sleep(2.3)
        
        input_move(f"The crew is ready to attack where should we hit captain {player1} : ")
        if in_bound(board, move1,move2):
            turn = False
            player_attack(board,board2, move1, move2)
            print('                                                             ')
            print(f"                          {player1}'s  Map                         ")
            make_board(board2)
            is_game_over(board, move1, move2)
            announce_ship(board)
            
            if hits== 17:
                turn2 = False
                print(f"We've sunken all the enemy ship's Captain {player1} we've won,  Captain's {player2} fleet is destroyed")
                print('')
                time.sleep(3.0)
                print(' Overall Satistics')
                time.sleep(2.0)
                print(f"                          {player1}'s  Map                         ")
                make_board(board)
                time.sleep(2.0)
                print(f"                          {player2}'s  Map                         ")
                make_board_player2(board3)
            else:
                      turn2 = True
        else:
            print(f"There's nothing there Captain {player1}, on Captain's' new order's redirect cannon's to another position  ")
            print(f'                                                                                ')
    while turn2 :
        time.sleep(3.0)
        print(f"                          {player2}'s  Map                         ")
        make_board_player2(board4)
        print("Crew preparing the cannon's Captain ")
        
        time.sleep(2.3)
        
        input_move(f"The crew is ready to attack where should we hit captain {player2} : ")
        if in_bound(board3, move1,move2):
            turn2 = False
            player_attack(board3,board4, move1, move2)
            print('                                                             ')
            print(f"                          {player2}'s  Map                         ")
            make_board_player2(board4)
            is_game_over2(board3,move1,move2)
            announce_ship_player2(board3)
            
            if hits2== 17:
                turn = False
                print(f"We've sunken all the enemy ship's Captain {player2} we've won,  Captain's {player1} fleet is destroyed")
                print('')
                time.sleep(3.0)
                print(' Overall Satistics')
                time.sleep(2.0)
                print(f"                          {player2}'s  Map                         ")
                make_board_player2(board3)
                time.sleep(2.0)
                print(f"                          {player1}'s  Map                         ")
                make_board(board)
                
            else:
                      turn = True
            
        else:
            print(f"There's nothing there Captain {player2}, on Captain's' new order's redirect cannon's to another position  ") 
            print(f'                                                                              ')