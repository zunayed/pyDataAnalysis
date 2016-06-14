import requests
import pandas as pd
from bs4 import BeautifulSoup


df = pd.read_csv('poly_data.csv', index_col='chart_date', parse_dates=[0])
years = range(1989, 2016)
all_data = set()

for year in years:
    yr_data = df[str(year)][['title', 'artist']]
    data = set()

    for row in yr_data.iterrows():
        # song name, artist
        data.add((row[1][0], row[1][1]))

    all_data = all_data.union(data)

# BASED_GOD_SEARCH_URL = 'https://www.google.com/#q=%s site:genius.com'
BASED_GOD_SEARCH_URL = 'https://www.google.com/search?hl=en&as_q=%s&as_epq=&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=&as_qdr=all&as_sitesearch=genius.com&as_occt=any&safe=images&as_filetype=&as_rights='

# Search for songs with google cause rap genius search is doo doo sometimes
link_df         = pd.read_csv('genius_links.csv')
google_urls     = []
rap_genius_urls = []

for song in list(all_data)[:2]:
    song_str    = '+'.join(str(x) for x in song)
    url         = BASED_GOD_SEARCH_URL % song_str
    google_urls.append(url)

    res = requests.get(url)
    if res.status_code == 200:
        # get rap genus links from google page
        bs          = BeautifulSoup(res.content, 'lxml')
        href_val    = bs.find_all("h3", {"class":"r"})[0].find('a',{'href':True})['href']
        rap_genius_urls.append(href_val[7:])

        # csv writer song, genius link
        # load data on script start and only ping google if link isn't saved

print rap_genius_urls
