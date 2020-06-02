import io
import string
import pandas as pd
import numpy as np
import threading
import utils

# calculate scholarship points based on gpa and college status
# https://scontent-sea1-1.xx.fbcdn.net/v/t1.15752-9/70275919_1092275450966326_4695819110586515456_n.jpg?_nc_cat=105&_nc_oc=AQnuz6-QsZPz6GAhklyF3G4t7pdEc4T9E6TX1b8MYZ5IS-QxfLzjgJJFDxVWd1AvJXM&_nc_ht=scontent-sea1-1.xx&oh=7483a2da0a3dd18435770d8e6c301414&oe=5E3DF954
def check_scholarship(pnm_info, output):
    for index, row in pnm_info.iterrows():
        # if PNM is a first year, use high school GPA for calculation
        if row['Year in College'] == 'First year':
            gpa = float(row['High School GPA'])
            if gpa >= 4.0:
                scholarship = 0.5
            elif gpa < 4.0 and gpa >= 3.7:
                scholarship = 0.35
            elif gpa < 3.7 and gpa >= 3.5:
                scholarship = 0.2
            else:
                scholarship = 0
        # if PNM has been in college more than 1 year, use college gpa for calculation
        else: 
            gpa = float(row['College GPA'])
            if gpa >= 3.8:
                scholarship = 0.5
            elif gpa < 3.8 and gpa >= 3.3:
                scholarship = 0.35
            else:
                scholarship = 0
        #print(gpa)
        output.set_value(index, 'Scholarship', scholarship)
        #row['Scholarship'] = scholarship 
        if index == 10:
            print(pnm_info.iloc[index])
            print(output.iloc[index]) 
    return output

# check if their answer contains any indications of multiple involvements
def check_involvements(x):
    # TODO: remove paranthetical data as multiple involvement examples
    if ',' in x or ';' in x or x.count('.') >= 2 or 'and' in x:
        return 0.25
    else: 
        return 0

# assign yardstick points according to decided yardstick values
def assign_yardstick_points(pnm_info):
    output = pd.DataFrame(columns=utils.yardstick_headers)

    output['First Name'] = pnm_info['Firstname']
    output['PNM ID (from council)'] = pnm_info['Council PNM ID']
    output['Service'] = pnm_info['Community Service Involvement'].astype(str).apply(lambda x: check_involvements(x))
    output['Legacy'] = 0    
    output['Letter of Rec'] = 0
    output['Athletics'] = pnm_info['Athletics'].astype(str).apply(lambda x: check_involvements(x))
    output['Leadership'] = pnm_info['Leadership Involvement'].astype(str).apply(lambda x: check_involvements(x))
    
    output = check_scholarship(pnm_info, output)

    print(output)
    output_yardstick_file(output)
    
# convert dataframe to CSV to import to MyVote
def output_yardstick_file(output):
    output.to_csv('yardstick_points.csv')

if __name__ == "__main__":
    # prompt for input files and day/party
    pnm_file = input("Enter file name containing PNM info: ")
    
    pnm_info = pd.read_csv(pnm_file, usecols=utils.yardstick_input)
    print(pnm_info)
    assign_yardstick_points(pnm_info)