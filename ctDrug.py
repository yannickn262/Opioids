import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from csv import reader
from numpy import *
from matplotlib import *

open_file = open('CTDrugs.csv', encoding='utf8')
read_file = reader(open_file)
drug_data = list(read_file)


fields = ['Age', 'Sex', 'Race']
df = pd.read_csv("CTDrugs.csv", skipinitialspace = True, usecols = fields)

#ignores columns that have more than 10% of its values as null
df2 = df[[column for column in df if df[column].count() / len(df) >= 0.1]]
df = df2

# min age
#print(df['Age'].min())
#print(df['Age'].describe())

col_count = 0

def freq_table_ages():
    #attempting to find number of deaths per each age group
    ages = {}
    ages_percent = {}
    count = 0

    for row in drug_data:
        count += 1
        age = row[3]
        if (age in ages) and (age != ""):
            ages[age] += 1
        else:
            ages[age] = 1

    for row in ages:
        percentage = (ages[row] / count) * 100
        ages_percent[row] = percentage

    col_count = count
    return ages_percent


# def freq_table_race():
#     races = {}
#     races_percent = {}
#     count = 0
#
#     for row in drug_data:
#         count += 1
#         race = row[5]
#         #filters for multiple races
#         if("," in race):
#             #need to split string into list of words with , delimiter
#
#         if(race in races) and (race != ""):
#             races[race] += 1
#         else:
#             races[race] = 1

def freq_table_gender():
    count = 0
    gender_count = {}
    gender_percent = {}

    for row in drug_data:
        count += 1
        gender = row[4]
        if (gender in gender_count) and (gender != ""):
            gender_count[gender] += 1
        else:
            gender_count[gender] = 1

    for row in gender_count:
        percentage = (gender_count[row]/count) * 100
        gender_percent[row] = percentage

    return gender_percent

fig, ax = plt.subplots()

def display_table_gender():
    gender_deaths = freq_table_gender()
    gender_display = {}
    for key in gender_deaths:
        gender_display[gender_deaths[key]] = key

    gender_sort = {}
    gender_sort = sorted(gender_display, reverse = True)
    #print(gender_sort)

    # for item in gender_sort[:2]:
    #     print("Gender: ", item[1], ' Frequency:', item[0], '%')

    colors = ['pink', 'turquoise']

    plt.bar(gender_display.values(), list(gender_display.keys()), 1, color = colors, edgecolor = 'black')

    plt.title("Gender Frequency Histogram")
    plt.xlabel("Gender")
    plt.ylabel("Frequency %")
    plt.show()



def display_table_ages():
    ages_deaths = freq_table_ages()
    ages_dict = {}
    ages_display = []
    for key in ages_deaths:
        ages_dict[ages_deaths[key]] = key
        key_val_tuple = (ages_deaths[key], key)
        ages_display.append(key_val_tuple)

    
    ages_sort = sorted(ages_display, reverse = False)
    print(ages_sort)
    #ax.hist(df['Age'].value_counts(), bins = 73, range = (14,87),  edgecolor = 'black')
    #ax.set_xticks()
    ax.scatter(ages_dict.values(), list(ages_dict.keys()), color = 'r', edgecolor = 'black')
    #ax.set_xticklabels(bins, rotation = 90)
    #ax.set_xticks(ages_sort, list(ages_dict.keys()))
    #ax.set_xticklabels(73, rotation = 90)
    #ax.set_xlim(0,87)
    ax.set_title("Opioid Deaths by Age")
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency %")
    plt.show()

    print("Top 10 Ages with Most Deaths: ")
    for item in ages_sort[:10]:
        print("Age: ",item[1], ' Frequency:', item[0], "%")

    #
    # num_cols = ['Age', 'Frequency']
    # bar_heights = ages_sort[num_cols].iloc[0].values
    # bar_positions = arange(5) + 0.75
    # fig, ax = plt.subplots()
    #ax.bar(bar_positions, bar_heights, 0.5)
    #drug_data['Age'].value_counts().plot(ax = ax, kind = 'bar')


    #plt.show()

display_table_ages()
display_table_gender()

def drug_percentage():
    heroin_log = {}
    count = 0
    heroin_y_count = 0
    cocaine_y_count = 0
    fentanyl_y_count = 0
    for row in drug_data:
        count += 1
        heroin_yes = row[20]
        cocaine_yes = row[21]
        fentanyl_yes = row[22]
        if (heroin_yes == "Y") or (heroin_yes == "y"):
            heroin_y_count += 1
        if (cocaine_yes == "Y") or (cocaine_yes == "y"):
            cocaine_y_count += 1
        if (fentanyl_yes == "Y") or (fentanyl_yes == "y"):
            fentanyl_y_count += 1



    percentage_heroin = (heroin_y_count/count) * 100
    percentage_cocaine = (cocaine_y_count/count) * 100
    percentage_fentanyl = (fentanyl_y_count/count) * 100

    #update by implementing string formatting to make universal for various datasets
    print("Proportion of Opioid Deaths caused by Heroin: ", percentage_heroin, "%")
    print("Proportion of Opioid Deaths caused by Cocaine: ", percentage_cocaine, "%")
    print("Proportion of Opioid Deaths caused by Fentanyl: ", percentage_fentanyl, "%")



drug_percentage()




#attempts to print out number of deaths per each group




#vis = sns.lmplot(data = df, x = 'Age', y = 'Race')
plt.figure(figsize = (8,4))
b = plt.bar(df['Age'],len(df['Age']), width = 1)
plt.title("CT Drug Mortality by Age", fontsize = 20)
#plt.show()

#### THINS TO LEARN IN PYTHON  ######

# take any python basics course and try and complete the exercies - (DONE)
# data structures, loops  -- by wednesday  (DONE)
# pandas - grouping, indexing, subsetting  -- by friday (Done)
# Exploratory Data Visualization - by friday (6/28)
# for pandas - go to the documentation - 2.4

####  THINGS TO LEARN IN SQL   #######

# Next - WRITE more SQL
# go to leetcode - work on easy problems
# most commonly used things - grouping , joins - inner, left
# work on create table as statements
# learn how to update the data - ususally done by 'set' commands
# create temp tables and load into them
# case statements
# lean what coalesce operation is
# learn how to select or unselect NULL values
