
party_num = { 1: 11,
              2: 9,
              3: 6
            }

# input file contains list of actives PNM talked to each day as comma separated string 
bumpgroup_headers = ['GroupNum', '1', '2', '3', '4', '5', '6']
input_headers = ['PNM', 'Day1_Actives', 'Day2_Actives', 'Day3_Actives']
output_headers = ['PNM', 'Active', 'Party', 'Day']

# headers to generate files for yardstick points
yardstick_input = ['Firstname','Council PNM ID', 'Year in College', 'College GPA',
                    'Leadership Involvement', 'Community Service Involvement', 
                    'High School GPA', 'Athletics']
yardstick_headers = ['PNM ID (from council)', 'Service', 'Legacy', 'Letter of Rec', 
                    'Athletics', 'Leadership', 'Scholarship']