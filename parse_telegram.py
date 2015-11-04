import csv
import json

import pandas as pd

FILENAME = 'data/messages.json'
CSV_FILENAME = 'output.csv'


def convert_json_file():
    reader =  csv.reader(open(FILENAME))
    # header = line.keys()
    data = []
    for raw_line in reader:
        line = json.loads(raw_line[0])

        if line['text'] != 'ping':
            data.append([
                line['date'],
                line['from']['username'],
                line['text'],
            ])

    df = pd.DataFrame(data)
    print df.head()

    df.to_csv('output.csv', encoding='utf-8')

def csv_load_file():
    df = pd.read_csv('output.csv')
    df.drop('index', 1)

    fook = df[df.text.str.contains('fck|fuck')]
    http = df[df.text.str.contains('http|https')]

    # print df.head()
    print "\n"
    print "Message frequency"
    print "----------------------------"
    print df[['username', 'text']].groupby('username').count()
    print "\n"
    print "HTTP/HTTPS frequency"
    print "----------------------------"
    print http[['username', 'text']].groupby('username').count()


def main():
    csv_load_file()


if __name__ == "__main__":
    main()
