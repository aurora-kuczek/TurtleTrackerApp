#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Aurora Kuczek (aurora.kuczek@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = 'data/raw/sara.txt'

#Create a file object from the filename
file_object = open(file=file_name,mode='r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file object
file_object.close()

#Extract one data line into a variable
lineString = line_list[200]

#Split lineString into a list of items
lineData = lineString.split()

#Assign variables to items in the lineData list
record_id = lineData[0]  # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[4]       # Observation Location Class
obs_lat = lineData[6]     # Observation Latitude
obs_lon = lineData[7]     # Observation Longitude

#Print information to the user
print(f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}.")