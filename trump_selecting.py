import random
import os
import sys
from variables import *
import shuffling_cards
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




def user_trump():
    time.sleep(0.2)
    global trump_user,two_suits, suitable_trump
    print("User gets : ")
    print("-------------")
    for i in shuffling_cards.user_cards:
        print(i)
        time.sleep(0.4)
    print()

    print()
    user_card_split = shuffling_cards.user_card_suit.split()
    user_card_split_edit = ([s for s in user_card_split if s != '-'])  # Remove "-" from the list
    two_suits = []
    same_suits = []
    club_count = user_card_split.count("Club")
    diamond_count = user_card_split.count("Diamond")
    spade_count = user_card_split.count("Spade")
    heart_count = user_card_split.count("Heart")
    count_dict = {"Club": club_count, "Diamond": diamond_count, "Spade": spade_count, "Heart": heart_count}
    count_list = [club_count, diamond_count, spade_count, heart_count]

    change_numbers(user_card_split_edit)
    changed4 = withoutAll
    
    if 2 in count_list:
        if 1 in count_list:
            if 2 in count_dict.values():
                for suit, level in count_dict.items():
                    if level == 2:
                        suitable_trump = suit
                        copy_list = changed4.copy()
                        new = []
                        for i in copy_list:
                            if i == suitable_trump:
                                index = copy_list.index(suitable_trump)
                                card = copy_list[index + 1]
                                new.append(card)
                                copy_list.pop(index)

                        new = [int(i) for i in new]

                        test = [i for i in new if i < 5]
                        if len(test) == 2:
                            value = "done"
                        else:
                            value = "no_need"

                        new_dict = convert(user_card_split_edit)

                        if value == "done":
                            if 'Club' in new_dict and 'Diamond' in new_dict and 'Spade' in new_dict:
                                suitable_trump = 'Heart'
                     

                            if 'Heart' in new_dict and 'Spade' in new_dict and 'Diamond' in new_dict:
                                suitable_trump = 'Club'
                          

                            if 'Club' in new_dict and 'Diamond' in new_dict and 'Heart' in new_dict:
                                suitable_trump = 'Spade'
                           

                            if 'Club' in new_dict and 'Spade' in new_dict and 'Heart' in new_dict:
                                suitable_trump = 'Diamond'
                            

        else:
            for i in user_card_split_edit:
                if "A" == i:  # Remove ace
                    no = user_card_split_edit.index(i) - 1
                    user_card_split_edit.pop(no)
                    user_card_split_edit.remove(i)

            club_count_edit = user_card_split_edit.count("Club")
            diamond_count_edit = user_card_split_edit.count("Diamond")
            spade_count_edit = user_card_split_edit.count("Spade")
            heart_count_edit = user_card_split_edit.count("Heart")

            count_dict_edit = {"Club": club_count_edit, "Diamond": diamond_count_edit,
                               "Spade": spade_count_edit,
                               "Heart": heart_count_edit}

            if 2 in count_dict_edit.values():
                for suit, level in count_dict_edit.items():
                    if level == 2:

                        if len(user_card_split_edit) == 6:  # If ace removed
                            suitable_trump = max(count_dict_edit, key=count_dict_edit.get)



                        else:  # If there is not ace to get removed
                            two_suits = []  # Making list of suits
                            for i in changed4:
                                index = changed4.index(i)
                                if index % 2 == 0:
                                    two_suits.append(i)



    elif 1 in count_list:
        if 3 in count_list:
            if 3 in count_dict.values():
                for suit, level in count_dict.items():
                    if level == 3:
                        suitable_trump = suit


        else:
            new = []
            for i in changed4:
                index = changed4.index(i)
                if index % 2 == 1:
                    new.append(i)
                    new_list = [int(i) for i in new]  # Change all strings to int

            count = min(new_list)
            if count not in changed4:
                count = str(count)
                index_of_count = changed4.index(count)
                suitable_trump = changed4[index_of_count - 1]
        


            else:
                index_of_count = changed4.index(count)
                suitable_trump = changed4[index_of_count - 1]
               


    else:
        if 4 in count_list:
            if 4 in count_dict.values():
                for suit, level in count_dict.items():
                    if level == 4:
                        suitable_trump = suit
                        

    while True:
        try:
            trump_user = input("Enter the trump card: ")
            trump_user_split = trump_user.split()
            length = len(trump_user_split)
            if length != 1:
                raise WrongTrumpFormat
            if trump_user not in user_card_split_edit:
                raise CardNotFound
            if len(two_suits) == 2:
                if trump_user not in two_suits:
                    raise SelectSuitableTrump
            else :
                if trump_user != suitable_trump:
                    raise SelectSuitableTrump
                

            break
        except WrongTrumpFormat:
            print("Please enter trump card suit, For example 'Diamond'")
        except CardNotFound:
            print("You don't have this card, try again")
        except SelectSuitableTrump:
            print("Check your cards and select suitable trump")

def trump_robot():
    time.sleep(0.2)

    global robot_trump_split, robot_trump

    robot_card_split = shuffling_cards.robot_card_suit.split()
    robot_card_split_edit = ([s for s in robot_card_split if s != '-'])  # Remove "-" from the list

    club_count = robot_card_split.count("Club")
    diamond_count = robot_card_split.count("Diamond")
    spade_count = robot_card_split.count("Spade")
    heart_count = robot_card_split.count("Heart")
    count_dict = {"Club": club_count, "Diamond": diamond_count, "Spade": spade_count, "Heart": heart_count}
    count_list = [club_count, diamond_count, spade_count, heart_count]

    change_numbers(robot_card_split_edit)
    changed4 = withoutAll

    if 2 in count_list:
        if 1 in count_list:
            if 2 in count_dict.values():
                for suit, level in count_dict.items():
                    if level == 2:
                        robot_trump = suit
                        print("Robot's trump : ", robot_trump)
                        copy_list = changed4.copy()
                        new = []
                        for i in copy_list:
                            if i == robot_trump:
                                index = copy_list.index(robot_trump)
                                card = copy_list[index + 1]
                                new.append(card)
                                copy_list.pop(index)

                        new = [int(i) for i in new]

                        test = [i for i in new if i < 5]
                        if len(test) == 2:
                            value = "done"
                        else:
                            value = "no_need"

                        new_dict = convert(robot_card_split_edit)

                        if value == "done":
                            if 'Club' in new_dict and 'Diamond' in new_dict and 'Spade' in new_dict:
                                robot_trump = 'Heart'
                                print("Robot's trump : ", robot_trump)
       

                            if 'Heart' in new_dict and 'Spade' in new_dict and 'Diamond' in new_dict:
                                robot_trump = 'Club'
                                print("Robot's trump : ", robot_trump)
      

                            if 'Club' in new_dict and 'Diamond' in new_dict and 'Heart' in new_dict:
                                robot_trump = 'Spade'
                                print("Robot's trump : ", robot_trump)
                         

                            if 'Club' in new_dict and 'Spade' in new_dict and 'Heart' in new_dict:
                                robot_trump = 'Diamond'
                                print("Robot's trump : ", robot_trump)
                          


        else:
            for i in robot_card_split_edit:
                if "A" == i:
                    no = robot_card_split_edit.index(i) - 1
                    robot_card_split_edit.pop(no)
                    robot_card_split_edit.remove(i)

            club_count_edit = robot_card_split_edit.count("Club")
            diamond_count_edit = robot_card_split_edit.count("Diamond")
            spade_count_edit = robot_card_split_edit.count("Spade")
            heart_count_edit = robot_card_split_edit.count("Heart")

            count_dict_edit = {"Club": club_count_edit, "Diamond": diamond_count_edit,
                               "Spade": spade_count_edit,
                               "Heart": heart_count_edit}

            if 2 in count_dict_edit.values():
                for suit, level in count_dict_edit.items():
                    if level == 2:

                        if len(robot_card_split_edit) == 6:  # If ace removed
                            robot_trump = max(count_dict_edit, key=count_dict_edit.get)
                            print("Robot's trump : ", robot_trump)
            

                        else:  # If there is not ace
                            new = []
                            for i in changed4:
                                index = changed4.index(i)
                                if index % 2 == 1:
                                    new.append(i)
                                    new_list = [int(i) for i in new]  # Change all strings to int

                            count = min(new_list)
                            if count not in changed4:
                                count = str(count)
                                var = changed4.index(count)
                                robot_trump = changed4[var - 1]
                                print("Robot's trump : ", robot_trump)
               
                            else:
                                var = changed4.index(count)
                                robot_trump = changed4[var - 1]
                                print("Robot's trump : ", robot_trump)
               


    elif 1 in count_list:
        if 3 in count_list:
            if 3 in count_dict.values():
                for suit, level in count_dict.items():
                    if level == 3:
                        robot_trump = suit
                        print("Robot's trump : ", robot_trump)
            
        else:
            new = []
            for i in changed4:
                index = changed4.index(i)
                if index % 2 == 1:
                    new.append(i)
                    new_list = [int(i) for i in new]  # Change all strings to int

            count = min(new_list)
            if count not in changed4:
                count = str(count)
                index_of_count = changed4.index(count)
                robot_trump = changed4[index_of_count - 1]
                print("Robot's trump : ", robot_trump)

            else:
                index_of_count = changed4.index(count)
                robot_trump = changed4[index_of_count - 1]
                print("Robot's trump : ", robot_trump)
    else:
        if 4 in count_list:
            if 4 in count_dict.values():
                for suit, level in count_dict.items():
                    if level == 4:
                        robot_trump = suit
                        print("Robot's trump : ", robot_trump)
    robot_trump_split = robot_trump.split()
