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

    #plt.plot(x,y)
    plt.title("Deaths by Age")
    plt.xlabel("Age")
    plt.ylabel("Percentage %")
    # calculate polynomial
    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)

    # calculate new x's and y's
    x_new = np.linspace(x[0], x[-1], 50)
    y_new = f(x_new)

    plt.plot(x,y,'o', x_new, y_new)

    # optimizedParameters, pcov = opt.curve_fit(func, x, y)
    # plt.plot(x, func(x, *optimizedParameters), label="fit");


    # calc the trendline - WORKS
    # z = np.polyfit(x, y, 1)
    # p = np.poly1d(z)
    # plt.plot(x,p(x),"r--")

    plt.show()

def displayRace():
    race_count = data['Race'].value_counts(normalize = True)
    race_count = race_count * 100
    print(race_count)
    race_count.plot(x = "Death Percentage", y = "Ethnicity", kind = 'barh', title = "Opioid Deaths by Ethnicity")

def displayMonth():

    # for day in data:
    #     datestring = data['Date']
    #     splitDate = datestring.str.split("/")
    #     month = splitDate
    #     print(month)

    #


    date_count = data['Date'].value_counts(normalize = True)
    date_count = date_count * 100

    #print(date_count)

    #print(b)




displayGender()
displayAges()
displayRace()
displayMonth()


plt.show()
