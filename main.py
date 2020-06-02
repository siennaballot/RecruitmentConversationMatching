import io
import pandas as pd
import numpy as np
import threading
import utils
import party_pairing
import yardstick_votes

day = 1
party_only = 0
parties = 10
pairs = None       # dataframe containing all final party pairs

if __name__ == "__main__":
    # prompt for type of calculation action
    action = input("What can I do for you today?\n1. Create conversation pairings\n2. Calculate yardstick points\nEnter your number choice: ")
    if (action == '1'):
        # prompt for input files and day/party
        infile = input("Enter the file name containing past pairings: ")
        pnm_file = input("Enter file name containing PNM info: ")
        bg_file = input("Enter file name containing bump group info: ")
        day = input("What day am I planning for? (Enter as a number) ")
        party_only = input('What party am I planning for? (Enter 0 for all parties) ')

        parties = utils.party_num[day]
        past_pairings = pd.read_csv(infile)
        pnm_info = pd.read_csv(pnm_file)
        bump_groups = pd.read_csv(bg_file)
        party_pairing.party_threads(past_pairings, pnm_info, bump_groups)
    elif (action == '2'):
        # prompt for input files and day/party
        pnm_file = input("Enter file name containing PNM info: ")
        
        pnm_info = pd.read_csv(pnm_file, usecols=utils.yardstick_input)
        yardstick_votes.assign_yardstick_points(pnm_info)