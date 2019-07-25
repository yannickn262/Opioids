import pandas as pd
import dateutil.parser
import matplotlib.pyplot as plt
import numpy as np
from csv import reader
from numpy import *
from matplotlib.pyplot import *
from pylab import *
from scipy.optimize import curve_fit
import scipy.optimize as opt


data = pd.read_csv('CTDrugs.csv')
total_count = data.shape[0]

# This is the function we are trying to fit to the data. Used for Fitted Curve
def func(x, a, b, c):
     return a * np.exp(-b * x) + c


def displayGender():
    gender_counts = data["Sex"].value_counts(normalize = True)
    gender_counts = gender_counts * 100
    colors = ['turquoise', 'pink']
    gender_counts.plot(kind = 'bar', color = colors)
    num_cols = ["Male", "Female", "Other"]
    plt.title("Deaths by Sex")
    plt.xlabel("Sex")
    plt.ylabel("Percentage %")
    plt.show()

def displayAges():
    ages_counts = data['Age'].value_counts(normalize = True)
    ages_counts = ages_counts * 100
    ages_sort = sorted(ages_counts.items(), reverse = False)

    x, y = zip(*ages_sort) # unpack a list of pairs into two tuples
    matplotlib.pyplot.scatter(x,y, color = 'blue')

    plt.title("Deaths by Age")
    plt.xlabel("Age")
    plt.ylabel("Percentage %")

    # calculate polynomial for fitted curve
    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)

    # calculate new x's and y's for fitted curve
    x_new = np.linspace(x[0], x[-1], 50)
    y_new = f(x_new)
    #plot fitted regression curve
    plt.plot(x,y,'o', x_new, y_new)

    # Optional: calculate trendline - Uncomment if you want linear
    # z = np.polyfit(x, y, 1)
    # p = np.poly1d(z)
    # plt.plot(x,p(x),"r--")

    plt.show()

def displayRace():
    race_count = data['Race'].value_counts(normalize = True)
    race_count = race_count * 100
    print(race_count)
    race_count.plot(kind = 'barh', title = "Opioid Deaths by Ethnicity")
    plt.xlabel("Death Percentage %")


#Future Implementation: Want to calculate what seasons have the most overdoses
def displayMonth():
    date_count = data['Date'].value_counts(normalize = True)
    date_count = date_count * 100
    # for day in data:
    #     datestring = data['Date']
    #     splitDate = datestring.str.split("/")
    #     month = splitDate
    #     print(month)


def drug_percentage():
    heroin_log = {}
    count = 0
    heroin_y_count = 0
    cocaine_y_count = 0
    fentanyl_y_count = 0
    for row in data:
        heroin_yes = data['Heroin']
        cocaine_yes = data['Cocaine']
        fentanyl_yes = data['Fentanyl']

    for row in heroin_yes:
        if (row == "Y"):
            heroin_y_count += 1
    for row in cocaine_yes:
        if (row == "Y"):
            cocaine_y_count += 1
    for row in fentanyl_yes:
        if (row == "Y"):
            fentanyl_y_count += 1

    percentage_heroin = (heroin_y_count/total_count) * 100
    percentage_cocaine = (cocaine_y_count/total_count) * 100
    percentage_fentanyl = (fentanyl_y_count/total_count) * 100

    #update by implementing string formatting to make universal for various datasets
    print("Proportion of Opioid Deaths caused by Heroin: ", percentage_heroin, "%")
    print("Proportion of Opioid Deaths caused by Cocaine: ", percentage_cocaine, "%")
    print("Proportion of Opioid Deaths caused by Fentanyl: ", percentage_fentanyl, "%")

displayGender()
displayAges()
displayRace()
displayMonth()
drug_percentage()


plt.show()
