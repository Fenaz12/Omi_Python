import random
from variables import *
import shuffling_cards
import trump_selecting
import time

def convert(a):
    convreted = {a[conv]: a[conv + 1] for conv in range(0, len(a), 2)}
    return convreted


def change_numbers(list_to_change):
    global withoutAll
    withoutK = [13 if x == 'K' else x for x in list_to_change]
    withoutQ = [12 if x == 'Q' else x for x in withoutK]
    withoutJ = [11 if x == 'J' else x for x in withoutQ]
    withoutAll = [14 if x == 'A' else x for x in withoutJ]


def change_numbers_to_letter(list_to_change):
    global without4
    without1 = ['K' if x == 13 else x for x in list_to_change]
    without2 = ['Q' if x == 12 else x for x in without1]
    without3 = ['J' if x == 11 else x for x in without2]
    without4 = ['A' if x == 14 else x for x in without3]


def change_suits(list_to_change):
    global withoutSuits
    withoutClub = ['♠' if x == 'Club' else x for x in list_to_change]
    withoutSpade = ['♣' if x == 'Spade' else x for x in withoutClub]
    withoutHeart = ['♥' if x == 'Heart' else x for x in withoutSpade]
    withoutSuits = ['♦' if x == 'Diamond' else x for x in withoutHeart]






class WrongTrumpFormat(Exception):
    pass


class WrongCardFormat(Exception):
    pass


class CardNotFound(Exception):
    pass


class SelectSuitableTrump(Exception):
    pass


class UseSameCard(Exception):
    pass


class UseYourTrump(Exception):
    pass


def placing_robot ():
    
    global robot_withoutsuit, points_robot, points_user, same_suits ,robot_withoutnum , card_maximum_level

    same_suits = []
    robot_withoutsuit = []
    robot_withoutnum = []
    card_maximum_level = []
    comparing_number1 = 0
    comparing_number2 = 0
    
    robot_card_all_withouttrump = [s for s in shuffling_cards.robot_cards_all if trump_selecting.trump_user not in s]  #Remove the user selected trump 
    robot_card_all_withouttrump_str = ' '.join(map(str, robot_card_all_withouttrump))
    robot_card_all_withouttrump_str_split = robot_card_all_withouttrump_str.split()
    robot_card_all_withouttrump_str_split_edit = ([s for s in robot_card_all_withouttrump_str_split if s != '-'])
    change_numbers(robot_card_all_withouttrump_str_split_edit)

    robot_card_all_withouttrump = withoutAll

    for i in robot_card_all_withouttrump:  # Making new list without suit
        if robot_card_all_withouttrump.index(i) % 2 == 1:
            robot_withoutsuit.append(i)
    robot_withoutsuit = [int(i) for i in robot_withoutsuit]

    for i in robot_card_all_withouttrump:  # Making new list without numbers
        if robot_card_all_withouttrump.index(i) % 2 == 0:
            robot_withoutnum.append(i)

    maximum_robot_withoutsuit = robot_withoutsuit.index(max(robot_withoutsuit))
    maximum_robot_robot_withoutnum = robot_withoutnum[maximum_robot_withoutsuit]
    robot_withoutsuit[maximum_robot_withoutsuit] = str(robot_withoutsuit[maximum_robot_withoutsuit])

    robot_card = maximum_robot_robot_withoutnum + ' - ' + robot_withoutsuit[maximum_robot_withoutsuit]

    robot_selected_card = robot_card.split()
    robot_selected_card_edit = ([s for s in robot_selected_card if s != '-'])  # Remove "-" from the list
    robot_selected_card_edit[1] = int(robot_selected_card_edit[1])  # Level is in str, change it to int
    change_numbers_to_letter(robot_selected_card_edit)
    print_robot_card = robot_selected_card_edit[0] + ' - ' + str(without4[1])
    time.sleep(1)
    print("Robot's call : ", print_robot_card)
    print()
    print("Your hand : ", ', '.join(shuffling_cards.user_cards_all))
    print()
    
    

    if robot_selected_card[0] in shuffling_cards.user_card_split_all_edit:  # Checking whether the user has the same suit
        comparing_number1 = withoutAll[1]
        comparing_number1 = int(comparing_number1)
        while True:
            try:
                card_user = input("Your call : ")
                card_user_check_suit = card_user.split()
                if len(card_user_check_suit) != 3:
                    raise WrongCardFormat
                if card_user not in shuffling_cards.user_cards_all :
                    raise CardNotFound
                if robot_selected_card[0] != card_user_check_suit[0]:
                    raise UseSameCard   
                break
            except UseSameCard:
                print("You have to select the same suit as robot")
            except WrongCardFormat:
                print("Type your card properly, for example \'Club - 9'")
            except CardNotFound:
                print("You don't have that card in your hand")

        user_selected_card = card_user.split()
        user_selected_card_edit = ([s for s in user_selected_card if s != '-'])
        change_numbers(user_selected_card_edit)
        comparing_number2 = withoutAll[1]
        comparing_number2 = int(comparing_number2)

        if comparing_number1 > comparing_number2:
            points_robot += 2
            time.sleep(0.2)
            print("Robot get two points, Total points of Robot - ", points_robot)
        else:
            points_user += 2
            time.sleep(0.2)
            print("User get two points, Total points of User - ", points_user)



    else:  # If there is no same spade as robot, user hast to place the trump
        card_user = trump_selecting.trump_user
        robot_selected_card = robot_card.split()
        robot_selected_card_edit = ([s for s in robot_selected_card if s != '-'])  # Remove "-" from the list
        robot_selected_card_edit[1] = int(robot_selected_card_edit[1]) # Level is in str, change it to int
        change_numbers_to_letter(robot_selected_card_edit)
        print_robot_card = robot_selected_card_edit[0] + ' - ' + str(without4[1])
        time.sleep(0.3)
        print("Robot's call : ", print_robot_card)
        time.sleep(0.3)
        print()
        #print("User has placed the trump card : ", trump_selecting.trump_user)
        while True:
            try:
                card_user = input("Your call : ")
                card_user_check_suit = card_user.split()
                if card_user_check_suit[0] != trump_selecting.trump_user :
                    raise UseYourTrump
                break
            except UseYourTrump:
                print("Hint : You can place your trump card")
        points_user += 2
        time.sleep(0.2)
        print("User get two points, Total points of User - ", points_user)

def placing_user ():

    global points_robot, points_user, same_suits, card_maximum_level
    comparing_number1 = 0
    comparing_number2 = 0
    same_suits = []
    card_maximum_level = []
    print("Your hand : ", ', '.join(shuffling_cards.user_cards_all))
    print()
    time.sleep(1)
    while True:
        try:
            card_user = input("Your call : ")
            user_selected_card = card_user.split()
            user_selected_card_edit = ([s for s in user_selected_card if s != '-'])  # Remove "-" from the list
            change_numbers(user_selected_card_edit)
            card_user_check_suit = card_user.split()
            if len(card_user_check_suit) != 3:
                raise WrongCardFormat
            if card_user not in shuffling_cards.user_cards_all:
                raise UseSameCard
            break

        except WrongCardFormat:
            print("Type your card properly, for example \'Club - 9'")
        except UseSameCard:
            print("You can only select card that you own")

    user_selected_card = card_user.split()
    user_selected_card_edit = ([s for s in user_selected_card if s != '-'])  # Remove "-" from the list
    change_numbers(user_selected_card_edit)  # User placed card without '-' and with only numbers

    if withoutAll[0] in trump_selecting.robot_trump_split:
        suit = withoutAll[0]
        copy_of_robots = shuffling_cards.robot_card_split_all_edit.copy()
        change_numbers(copy_of_robots)
        copy_of_robots = withoutAll
        list_to_tuple = list(zip(copy_of_robots, copy_of_robots[1:] + copy_of_robots[:1]))
        copy_of_robots = [i for i in list_to_tuple if list_to_tuple.index(i) % 2 == 0]

        tuples_of_robot = [item for item in copy_of_robots if item[0] == suit]

        for i in tuples_of_robot:
            i = int(i[1])
            same_suits.append(suit)
            same_suits.append(i)



        for i in same_suits:
            if same_suits.index(i) % 2 == 1:
                card_maximum_level.append(i)
        maximum = max(card_maximum_level)
        robot_card_list = [suit, maximum]
        change_numbers_to_letter(robot_card_list)
        robot_card = robot_card_list[0] + ' - ' + str(without4[1])
        time.sleep(1)
        print('Robot call : ', robot_card, '(Trump card)')
        points_robot += 2
        print("Robot get one points, Total points of Robot - ", points_robot)

    elif withoutAll[0] in shuffling_cards.robot_card_split_all_edit:  # Checking whether the robot has the same suit
        suit = withoutAll[0]
        copy_of_robots = shuffling_cards.robot_card_split_all_edit.copy()
        change_numbers(copy_of_robots)
        copy_of_robots = withoutAll
        list_to_tuple = list(zip(copy_of_robots, copy_of_robots[1:] + copy_of_robots[:1]))
        copy_of_robots = [i for i in list_to_tuple if list_to_tuple.index(i) % 2 == 0]

        tuples_of_robot = [item for item in copy_of_robots if item[0] == suit]

        for i in tuples_of_robot:
            i = int(i[1])
            same_suits.append(suit)
            same_suits.append(i)

        # print(same_suits)

        for i in same_suits:
            if same_suits.index(i) % 2 == 1:
                card_maximum_level.append(i)
        maximum = max(card_maximum_level)
        robot_card_list = [suit, maximum]
        change_numbers_to_letter(robot_card_list)
        # print('withoutall', withoutAll)
        robot_card = robot_card_list[0] + ' - ' + str(without4[1])
        time.sleep(1)
        print('Robot call : ', robot_card)
        print()
        time.sleep(2.5)

        user_selected_card = card_user.split()
        user_selected_card_edit = ([s for s in user_selected_card if s != '-'])
        change_numbers(user_selected_card_edit)
        comparing_number2 = withoutAll[1]
        comparing_number2 = int(comparing_number2)

        if maximum > comparing_number2:
            points_robot += 2
            print("Robot get one points, Total points of Robot - ", points_robot)
        else:
            points_user += 2
            print("User get one points, Total points of User - ", points_user)

    else:  # If there is no same spade as robot, user hast to place the trump
        robot_card = trump_selecting.robot_trump
        print("User call : ", card_user)
        time.sleep(0.2)
        print("Robot has placed the trump card : ", trump_selecting.robot_trump)
        points_robot += 2
        time.sleep(0.2)
        print("Robot get two points, Total points of Robot - ", points_robot)
