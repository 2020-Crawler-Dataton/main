import glob

import pandas as pd

all_data = pd.DataFrame(columns=['Title', 'Artist', 'Image', 'Tagging'])
for f in glob.glob('../Selenium/Bugs/data/genre/*.xlsx'):
    df = pd.read_excel(f)
    temp = f.index('\\') + 1
    tag = "#" + f[temp:]
    tag = tag[:-5]
    df['Tagging'] = tag
    all_data = all_data.append(df, ignore_index=True)

for f in glob.glob('../Selenium/Bugs/data/style/*.xlsx'):
    df = pd.read_excel(f)
    temp = f.index('\\') + 1
    tag = "#" + f[temp:]
    tag = tag[:-5]
    df['Tagging'] = tag
    all_data = all_data.append(df, ignore_index=True)

del all_data['Unnamed: 0']

all_data = all_data.groupby(['Title', 'Artist'], as_index=False).agg({'Tagging': ', '.join})

all_data.to_excel('music_tagging.xlsx')
