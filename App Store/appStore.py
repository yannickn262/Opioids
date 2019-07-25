#Download both datasets, and update open to absolute path of file
from csv import reader

apple_store = open('AppleStore.csv', encoding='utf8')
read_apple = reader(apple_store)
apple = list(read_apple)
apple_header = apple[0]
apple_content = apple[1:]


google_store = open('googleplaystore.csv', encoding = 'utf8')
read_google = reader(google_store)
google = list(read_google)
google_header = google[0]
google_content = google[1:]


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


#deletes content with rating of 19 as google play ratings go from 1-5 (i.e. low quality data)
del google_content[10472]

duplicates_goog = []
duplicates_apple = []
uniques_goog = []
uniques_apple = []

# Counts the # of duplicates and organizes into a list
for app in google_content:
    name = app[0]
    if(name in uniques_goog):
        duplicates_goog.append(name)
    else:
        uniques_goog.append(name)

for app in apple_content:
    name = app[0]
    if(name in uniques_apple):
        duplicates_apple.append(name)
    else:
        uniques_apple.append(name)

#print("Number of Google Play Duplicates: ", len(duplicates_goog))
#print("Number of Apple Store Duplicates: ", len(duplicates_apple))

#Creates Dictionary where key is unique app name, and value is highest # of reviews of that app
#Ex: Insta has 2.1 million ratings in one entry in the list and 2.2 million ratings in another in same list
#Ex: Keep the one with more as it's more recent data and ignore other entry

reviews_max = {}
for app in google_content:
    name = app[0]
    n_reviews = float(app[3])
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

reviews_max_apple = {}
for app in apple_content:
    name = app[1]
    n_reviews = float(app[5])
    if name in reviews_max_apple and reviews_max_apple[name] < n_reviews:
        reviews_max_apple[name] = n_reviews
    elif name not in reviews_max:
        reviews_max_apple[name] = n_reviews

google_clean = []
apple_clean = []
already_added = []
already_added_apple = []

#removes duplicates in google play store
for app in google_content:
    name = app[0]
    n_reviews = float(app[3])
    if n_reviews == reviews_max[name] and name not in already_added:
        google_clean.append(app)
        already_added.append(name)

#removes duplicates in apple app store
for item in apple_content:
    name = item[1]
    n_reviews = float(item[5])
    if n_reviews == reviews_max_apple[name] and name not in already_added_apple:
        apple_clean.append(item)
        already_added_apple.append(name)


#attempts to remove non-English App's from list (Demographic: English Speaking Consumers)
#if english return true else false
def checkLang(string):
    nonAscii_count = 0
    for letter in string:
        num = ord(letter)
        if num > 127:
           nonAscii_count += 1

        #more than 3 special characters means it's probably not english
        if nonAscii_count > 3:
            return False
        else:
            return True

nonEnglish_goog = []
nonEnglish_apple = []

def removeNonEng():
    for app in google_clean:
        name = app[0]
        if checkLang(name):
            nonEnglish_goog.append(app)

    for app in apple_clean:
        name = app[1]
        if checkLang(name):
           nonEnglish_apple.append(app)


#explore_data(nonEnglish_goog, 0, 3, True)

removeNonEng()
#isolates free apps
free_apple = []
free_google = []

def findFree():
    for app in nonEnglish_goog:
        price = app[7]
        if price == '0':
            free_google.append(app)

    for app in nonEnglish_apple:
        price = app[5]
        if price == '0':
            free_apple.append(app)

findFree()
#print("Number of Free Apps in Google Play Store: ", len(free_google))
#print("Number of Free Apps in Apple App Store: ",  len(free_apple))

#Generates Frequency Table with percentages
def freq_table(dataset, index):
    table = {}
    count = 0

    for item in dataset:
        count += 1
        val = item[index]
        if val in table:
            table[val] += 1
        else:
            table[val] = 1

    table_percent = {}
    for item in table:
        percentage = 0
        percentage = (table[item]/count) * 100
        table_percent[item] = percentage

    return table_percent

def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_tuple = (table[key], key)
        table_display.append(key_val_tuple)

    #sorts in descending order
    table_sort = sorted(table_display, reverse = True)
    for item in table_sort:
        print(item[1], ':', item[0])

#display_table(free_apple, -5)

#Finding most popular apps (in the apple app store)
popular_genres = freq_table(nonEnglish_goog, 1)
for genre in popular_genres:
    total = 0
    len_genre = 0
    catagory_app = app[1]
    for app in nonEnglish_goog:
        num_install = app[5]
        num_install = num_install.replace(',' , '')
        num_install = num_install.replace('+' , '')
        total += float(num_install)
        len_genre += 1

    avg_install = total / len_genre
    #print(Category, ':', avg_install)

#find most popular health apps in google play store

for app in nonEnglish_goog:
    if app[1] == 'HEALTH_AND_FITNESS' and (app[5] == '100,000+' or app[5] == '1,000,000+' or app[5] == '10,000,000+'):
        print(app[0], ':', app[5])
