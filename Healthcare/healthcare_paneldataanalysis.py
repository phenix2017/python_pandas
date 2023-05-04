import pandas as pd
import matplotlib.pyplot as plt
import os
# import sys
# print(os.path.dirname(sys.executable))
# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))
# List all files in the current directory
file_list = os.listdir(current_directory)
file_list_csv = [file for file in file_list if file.endswith('csv')]
# # Iterate through each file and read its content
for file in file_list:
    file_path = os.path.join(current_directory, file)
        
    # Check if it's a file (skip directories)
    # if os.path.isfile(file_path):
    #     with open(file_path, 'r') as f:
    #         content = f.read()
    #         print(f"Contents of {file}:\n{content}\n")
# Get the obsulute path of the files
file_tobeopened_directory = os.path.join(current_directory, file_list_csv[0])

data_first_health_camp_attended = pd.read_csv(file_tobeopened_directory)
# Get the general information of the datasets
data_first_health_camp_attended.info()
# Based on the info, clean up the data
data_first_health_camp_attended.head()
data_first_health_camp_attended.columns
data_first_health_camp_attended.info()
data_first_health_camp_attended.describe()
# Get the numerical collumns 
# Using visualization tools to get deeper understanding of the data
plt.figure
data_first_health_camp_attended.boxplot(column="Donation")
plt.yticks(np.arange(0, 300, 50))  # set y-axis grid interval from 0 to 2000, with a step of 200
plt.show()
# To better understand the plt
# Unique row check
data_first_health_camp_attended.value_counts()

file_tobeopened_directory = os.path.join(current_directory, file_list_csv[1])
# file_list_csv
data_Health_Camp_Detail = pd.read_csv(file_tobeopened_directory)

# file_list_csv
file_tobeopened_directory = os.path.join(current_directory, file_list_csv[2])
data = pd.read_csv(file_tobeopened_directory)
data_drop_na = data.dropna(inplace=False)
# print(data_Health_Camp_Detail.describe())
file_tobeopened_directory = os.path.join(current_directory, file_list_csv[3])
data = pd.read_csv(file_tobeopened_directory)
data.head()
file_tobeopened_directory = os.path.join(current_directory, file_list_csv[4])
data = pd.read_csv(file_tobeopened_directory)
data.head()

for col in data.columns:
    print(data[col].value_counts().info())