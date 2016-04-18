import csv
import json

import pandas   as pd
import numpy    as np
import seaborn  as sns
# from sklearn.svm                        import LinearSVC
# from sklearn.feature_extraction.text    import CountVectorizer

FILENAME = 'messages.json'
CSV_FILENAME = 'output.csv'


def convert_json_file():
    data = []
    reader = csv.reader(open(FILENAME))

    for raw_line in reader:
        line = json.loads(raw_line[0])

        if line['text'] != 'ping':
            data.append([
                line['date'],
                line['from']['username'],
                line['text'],
            ])

    df = pd.DataFrame(data)
    df.columns = ['time', 'username', 'text']
    df.to_csv('output.csv', encoding='utf-8')
    print df.describe

def csv_load_file():
    df = pd.read_csv('output.csv', parse_dates=1)

    fook = df[df.text.str.contains('fck|fuck')]
    http = df[df.text.str.contains('http|https')]

    print df.head()
    times = pd.to_datetime(df.time)
    # print df['time'].groupby([times.hour]).value_col.sum()

    # sns.heatmap(df['username'])
    # ax = sns.heatmap(df['username'])

    print df.head()
    print "\n"
    print "Message frequency"
    print "----------------------------"
    print df[['username', 'text']].groupby('username').count()
    print "\n"
    print "HTTP/HTTPS frequency"
    print "----------------------------"
    print http[['username', 'text']].groupby('username').count()

def train_model():
    train_data = pd.read_csv("data/kaggle_insult/train.csv")
    test_data = pd.read_csv("data/kaggle_insult/test_with_solutions.csv")

    # Insult column -> Target
    # Comment column -> contains text
    y_train = np.array(train_data.Insult)
    comments_train = np.array(train_data.Comment)

    cv = CountVectorizer()
    cv.fit(comments_train)

    X_train = cv.transform(comments_train).tocsr()

    svm = LinearSVC()
    svm.fit(X_train, y_train)

    comments_test = np.array(test_data.Comment)
    y_test = np.array(test_data.Insult)
    X_test = cv.transform(comments_test)
    print svm.score(X_test, y_test)

if __name__ == "__main__":
    convert_json_file()
    # csv_load_file()
    # train_model()
