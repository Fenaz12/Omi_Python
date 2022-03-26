import random
import os
import sys
from variables import *



print()




def shuffling():
    global random_cards,user_cards,robot_cards,user_cards_all,user_card_all_str_split,user_card_split_all_edit,ordered_list,user_card_suit,robot_cards_all,robot_card_all_str,robot_card_all_str_split,robot_card_split_all_edit,robot_card_suit
    random_cards = random.sample(All_cards, 16)
    user_cards = random_cards[0:4]
    robot_cards = random_cards[8:12]

    user_cards_all = random_cards[0:8]
    user_card_all_str = ' '.join(map(str, user_cards_all))
    user_card_all_str_split = user_card_all_str.split()
    user_card_split_all_edit = ([s for s in user_card_all_str_split if s != '-'])
    myorder = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]
    ordered_list = [user_card_split_all_edit[i] for i in myorder]
    user_card_suit = ' '.join(map(str, user_cards))


    robot_cards_all = random_cards[8:16]
    robot_card_all_str = ' '.join(map(str, robot_cards_all))
    robot_card_all_str_split = robot_card_all_str.split()
    robot_card_split_all_edit = ([s for s in robot_card_all_str_split if s != '-'])
    robot_card_suit = ' '.join(map(str, robot_cards))

    
