# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

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

# <headingcell level=1>

# Plotting all complaints by locations gives us a crude map of the city

# <codecell>

plot(orig_data['Longitude'], orig_data['Latitude'], '.', color='blue')

# <headingcell level=1>

# Have a quick look at what people complain about

# <codecell>

orig_data['Complaint Type'].value_counts()[:20].plot(kind='bar')
plt.title('Complaints')

# <headingcell level=1>

# Complaints by borough

# <codecell>

orig_data['Borough'].value_counts()[:20].plot(kind='bar')

# <headingcell level=1>

# Complaints by zip

# <codecell>

orig_data['Incident Zip'].value_counts()[:20].plot(kind='bar')

# <headingcell level=1>

# Ok Lets now look at rodent complaints by borough

# <codecell>

rodent_complaints = orig_data[orig_data['Complaint Type'] == 'Rodent']
rodent_complaints['Borough'].value_counts().plot(kind='bar')

# <headingcell level=1>

# Lets take a look at complaints at my neighborhood

# <codecell>

my_zip = orig_data[orig_data['Incident Zip'].str.contains('11220').fillna(False)]
my_zip['Complaint Type'].value_counts()[:20].plot(kind='bar')

# <headingcell level=1>

# Lets compare that to the worlds wealthiest zip code

# <codecell>

rich_people_zip = orig_data[orig_data['Incident Zip'].str.contains('10065').fillna(False)]
rich_people_zip['Complaint Type'].value_counts()[:20].plot(kind='bar')

# <codecell>

a = orig_data[orig_data['Incident Zip'].str.contains('10065').fillna(False)]

# <codecell>


