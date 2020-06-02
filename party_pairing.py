import io
import pandas as pd
import numpy as np
import threading
import utils
import main

def pair_pnms(party, past_pairs, pnm_info, bump_groups):
    df = pd.DataFrame(utils.output_headers)

    # create dict of all actives 
    actives = bump_groups.set_index('GroupNum').T.to_dict('list')

    print("Pairing for party "+str(party))
    for index, row in pnm_info:
        active = 'N/A'
        df = df.append({'PNM': row['PNM'], 'Active': active}, ignore_index=True)

    # format and append to global pairs dataframe
    df['Party'] = party
    df['Day'] = day
    pairs = pairs.append(df, ignore_index=True)

def party_threads(past_pairs, pnm_info, bump_groups):
    global pairs
    print("Pairing PNMs with actives")
    # TODO: ask if we decide which party the pnm comes to or that is assigned for us
    pairs = pd.DataFrame(utils.output_headers)

    # if only want pairings for one party 
    if party_only > 0:
        pnms = pnm_info[pnm_info['party']==party_only]
        pair_pnms(party_only, past_pairs, pnms, bump_groups)
        print(pairs)
        return
    
    # if multiple parties, create thread for each party of the day
    threads = []
    for party in range(1, parties):
        pnms = pnm_info[pnm_info['party']==party]
        threads.append(threading.Thread(target=party_threads, args=(party,past_pairs,pnms,bump_groups)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()
        print("Finished pairing for party")
    
    create_output()    

# convert dataframe to CSV to output
def create_output():
    print("Creating CSV containing party pairings")

    pairs = pairs.sort_values(by='Party')
    output_pairs = 'day'+day+'_pairs.csv'
    pairs.to_csv(output_pairs)

if __name__ == "__main__":
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
    party_threads(past_pairings, pnm_info, bump_groups)
