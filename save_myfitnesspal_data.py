import os
import json
import datetime

import myfitnesspal

DATA_FILE = 'data/food_data.json'


def build_entry(day):
    data    = {}
    meals   = day.meals

    for meal in meals:
        data[meal.name] = meal.get_as_list()

    return data


def save_data(day, entry):
    if os.stat(DATA_FILE).st_size == 0:
        data = {}
    else:
        with open(DATA_FILE) as f:
            data = json.load(f)

    with open(DATA_FILE, 'w') as f:
        data[day.date.strftime('%x')] = entry
        print data
        json.dump(data, f)


def get_data():
    user        = os.environ['USER']
    password    = os.environ['PASSWORD']

    print "Getting {} , using {}".format(user, password)
    client  = myfitnesspal.Client(user, password)
    # day     = client.get_date(datetime.date.today())
    day     = client.get_date(2015, 11, 13)
    entry   = build_entry(day)

    save_data(day, entry)


def get_drink_data():
    with open(DATA_FILE) as f:
        data = json.load(f)

    for date, meals in data.iteritems():
        print date, meals['snacks']


if __name__=='__main__':
    # get_data()
    get_drink_data()

