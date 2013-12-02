# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# The noisest zip codes in NYC

# <codecell>

import pandas as pd

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

pd.set_option('display.mpl_style', 'default')
figsize(15, 6)
pd.set_option('display.line_width', 4000)
pd.set_option('display.max_columns', 100)
orig_data = pd.read_csv('./311-service-requests.csv', nrows=100000, parse_dates=['Created Date'])
orig_data['Street Name'].fillna("", inplace=True) # This is replacing missing street names

# <headingcell level=2>

# Isolate the boroughs

# <codecell>

brooklyn = orig_data[orig_data['Borough'] == 'BROOKLYN']
queens = orig_data[orig_data['Borough'] == 'QUEENS']
manhattan = orig_data[orig_data['Borough'] == 'MANHATTAN']
bronx = orig_data[orig_data['Borough'] == 'BRONX']

# <headingcell level=2>

# A quick look at the type of complaints in Brooklyn

# <codecell>

brooklyn[['Complaint Type','Incident Zip']][:20]

# <codecell>

bk_noise = brooklyn[(brooklyn['Complaint Type'] == 'Noise - Street/Sidewalk') | (brooklyn['Complaint Type'] == 'Noise - Commercial')]
qn_noise = queens[(queens['Complaint Type'] == 'Noise - Street/Sidewalk') | (queens['Complaint Type'] == 'Noise - Commercial')]
man_noise = manhattan[(manhattan['Complaint Type'] == 'Noise - Street/Sidewalk') | (manhattan['Complaint Type'] == 'Noise - Commercial')]
bx_noise = bronx[(bronx['Complaint Type'] == 'Noise - Street/Sidewalk') | (bronx['Complaint Type'] == 'Noise - Commercial')]

# <headingcell level=1>

# Queens zips with the most complaints

# <codecell>

qn_noise['Incident Zip'].value_counts()[:10].plot(kind='bar')

# <headingcell level=1>

# Brooklyn zips with the most complaints

# <codecell>

bk_noise['Incident Zip'].value_counts()[:10].plot(kind='bar')

# <headingcell level=1>

# Manhattan zips with the most complaints

# <codecell>

man_noise['Incident Zip'].value_counts()[:10].plot(kind='bar')

# <headingcell level=1>

# Queens zips with the most complaints

# <codecell>

bx_noise['Incident Zip'].value_counts()[:10].plot(kind='bar')

