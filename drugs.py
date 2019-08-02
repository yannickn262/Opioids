import pandas as pd
import dateutil.parser
import matplotlib.pyplot as plt
import numpy as np
from csv import reader
from numpy import *
from matplotlib.pyplot import *
from pylab import *
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import scipy.optimize as opt
import dateutil
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def f(x):
    # function to approximate by polynomial interpolation
    return x * np.sin(x)

#Work in Progress: Attempting to use sklearn to predict ages
def predict_ages():
    # generate points used to plot
    x_plot = np.linspace(0, 10, 100)

    # generate points and keep a subset of them
    x = np.linspace(0, 10, 100)
    rng = np.random.RandomState(0)
    rng.shuffle(x)
    x = np.sort(x[:20])
    y = f(x)

    # create matrix versions of these arrays
    X = x[:, np.newaxis]
    X_plot = x_plot[:, np.newaxis]

    colors = ['teal', 'yellowgreen', 'gold']
    lw = 2
    plt.plot(x_plot, f(x_plot), color='cornflowerblue', linewidth=lw,
         label="ground truth")
    plt.scatter(x, y, color='navy', s=30, marker='o', label="training points")

    for count, degree in enumerate([3, 4, 5]):
        model = make_pipeline(PolynomialFeatures(degree), Ridge())
        model.fit(X, y)
        y_plot = model.predict(X_plot)
        plt.plot(x_plot, y_plot, color=colors[count], linewidth=lw,
             label="degree %d" % degree)

    plt.legend(loc='lower left')
    plt.show()




#curve_fit paramaters
#scipy curve fitting techniques
#train model - split 50,000 and then 20,000
# Create Predictive model - scikit


data = pd.read_csv('CTDrugs.csv')
total_count = data.shape[0]


def displayGender():
    gender_counts = data["Sex"].value_counts(normalize = True)
    gender_counts = gender_counts * 100
    colors = ['turquoise', 'pink']
    gender_counts.plot(kind = 'bar', color = colors)
    num_cols = ["Male", "Female", "Other"]
    plt.title("Deaths by Gender")
    plt.xlabel("Sex")
    plt.ylabel("Percentage %")
    plt.show()

# This is the function we are trying to fit to the data. Used for Fitted Curve
def func(x, a, b, c):
     return a * np.exp(-b * x) + c

def displayAges():
    ages_counts = data['Age'].value_counts(normalize = True)
    ages_counts = ages_counts * 100
    ages_sort = sorted(ages_counts.items(), reverse = False)

    x, y = zip(*ages_sort) # unpack a list of pairs into two tuples
    matplotlib.pyplot.scatter(x,y, color = 'blue')

    plt.title("Deaths by Age")
    plt.xlabel("Age")
    plt.ylabel("Percentage %")
    xp = linspace(10,90, 100)
    # calculate polynomial for fitted curve
    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)

    p2 = np.polyfit(x, y, 11)
    plot(xp, polyval(p2, xp), 'b--')

    # calculate new x's and y's for fitted curve
    x_new = np.linspace(x[0], x[-1], 50)
    y_new = f(x_new)

    #plot fitted regression curve
    #plt.plot(x,y,'o', x_new, y_new)

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

def drug_percentage():
    heroin_log = {}
    count = 0
    heroin_y_count = 0
    cocaine_y_count = 0
    fentanyl_y_count = 0
    alcohol_y_count = 0

    for row in data:
        heroin_yes = data['Heroin']
        cocaine_yes = data['Cocaine']
        fentanyl_yes = data['Fentanyl']
        alcohol_yes = data['Ethanol']

    for row in heroin_yes:
        if (row == "Y"):
            heroin_y_count += 1
    for row in cocaine_yes:
        if (row == "Y"):
            cocaine_y_count += 1
    for row in fentanyl_yes:
        if (row == "Y"):
            fentanyl_y_count += 1
    for row in alcohol_yes:
        if (row == "Y"):
            alcohol_y_count += 1

    percentage_heroin = (heroin_y_count/total_count) * 100
    percentage_cocaine = (cocaine_y_count/total_count) * 100
    percentage_fentanyl = (fentanyl_y_count/total_count) * 100
    percentage_alcohol = (alcohol_y_count/total_count) * 100


    print("Proportion of Opioid Deaths caused by Heroin: ", percentage_heroin, "%")
    print("Proportion of Opioid Deaths caused by Cocaine: ", percentage_cocaine, "%")
    print("Proportion of Opioid Deaths caused by Fentanyl: ", percentage_fentanyl, "%")
    print("Proportion of Opioid Deaths caused by Alcohol: ", percentage_alcohol, "%")


#Future Implementation: Display Drug Percentages Visually

#Future Implementation: Want to calculate what seasons have the most overdoses
def displayMonth():
    date_count = data['Date'].value_counts(normalize = True)
    date_count = date_count * 100

    data['Date'] = pd.to_datetime(data['Date'])
    dg = data.groupby([data['Date'].dt.year.rename('year'), data['Date'].dt.month.rename('month')]).agg({'count'})
    #print(dg)

    # months = {}
    # for year in dg:
    #     month = dg[1]
    #     month_count = dg[2]
    #     if month in months:
    #         months[month] += month_count

    #print(months)

    #dg.plot(kind = 'barh', title = "Deaths by Season")

    # for day in data:
    #     datestring = data['Date']
    #     splitDate = datestring.str.split("/")
    #     month = splitDate
    #     print(month)



predict_ages()
displayGender()
displayAges()
displayRace()
displayMonth()
drug_percentage()


plt.show()
