import random
import os
import sys
import time
import trump_selecting
import shuffling_cards
import placing_card
import rules

class OptionNotFound(Exception):
    pass
    

def menu():
    global option
    print("1. Start the game ")
    time.sleep(0.1)
    print("2. Rules ")
    time.sleep(0.1)
    print("3. Quit")
    time.sleep(0.1)
    print()
    while True :
        try :
            option = int(input("Type the number of the option : "))
            print()
        except:
            print("Check your option")
        else:
            try :
                if option not in [1,2,3]:
                    raise OptionNotFound
                break
            except OptionNotFound:
                print("Select a suitable option")

menu()

if option == 1 :
    
    while True:
        players = ['user', 'robot']
        first = random.choice(players)
        print(first, 'placing the trump first')

        player_list = []
        rounds = 1
        index_of_list = 0


        while len(player_list) < 8:
            if first == 'user':
                player_list.append('user')
                player_list.append('robot')
            else:
                player_list.append('robot')
                player_list.append('user')



        while rounds != 9:
            time.sleep(0.1)
            print( 'Trick number - ' , rounds)
            #print(color.RED + 'Trick number - ' + color.END, rounds )
            print()
            shuffling_cards.shuffling()

            if player_list[index_of_list] == 'user':
                trump_selecting.user_trump()

            if player_list[index_of_list] == 'robot':
                trump_selecting.trump_robot()

            if player_list[index_of_list] == 'user':
                placing_card.placing_robot()

            if player_list[index_of_list] == 'robot':
                placing_card.placing_user()

            if rounds == 8:
                time.sleep(0.2)
                print('Robot gets ', placing_card.points_robot, '-- User gets', placing_card.points_user)
                time.sleep(1)
                if placing_card.points_robot > placing_card.points_user:
                    print("Robot wins")
                elif placing_card.points_robot < placing_card.points_user:
                    print("User wins")
                elif placing_card.points_robot == placing_card.points_user:
                    print("Match tied")
                
            rounds += 1
            index_of_list += 1
            print()

        while True :
            time.sleep(3)
            after_game = input("Do you want to play again? (y/n): ")
            if after_game in ('y' , 'n'):
                break
            print("Invalid input")
        if after_game == 'y':
            continue
        else :
            sys.exit("Quitting the game")

if option == 2 :
    rules.rules()
    print()
    print("Going to menu")
    menu()
        

if option == 3 :
    sys.exit()


