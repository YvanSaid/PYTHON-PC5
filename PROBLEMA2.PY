#JUPYTER
import nbformat

notebook_path = '/mnt/data/Problema2.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_content = nbformat.read(f, as_version=4)

notebook_content

import pandas as pd
import sqlite3

file_path = '/mnt/data/winemag-data-130k-v2.csv'
df = pd.read_csv(file_path)

exploration_info = df.info()

df.rename(columns={
    'country': 'Country',
    'description': 'Description',
    'points': 'Points',
    'price': 'Price'
}, inplace=True)

continent_mapping = {
    'US': 'North America', 'France': 'Europe', 'Italy': 'Europe', 'Spain': 'Europe',
    'Chile': 'South America', 'Argentina': 'South America', 'Australia': 'Oceania',
    'New Zealand': 'Oceania', 'South Africa': 'Africa', 'Portugal': 'Europe'
}
df['Continent'] = df['Country'].map(continent_mapping).fillna('Other')

df['Price_Category'] = df['Price'].apply(lambda x: 'High' if x > 30 else 'Low')

df['Description_Length'] = df['Description'].apply(len)

report1 = df.groupby('Continent')['Points'].mean().reset_index()
report1_path = '/mnt/data/report1_average_points_per_continent.csv'
report1.to_csv(report1_path, index=False)

report2 = df['Country'].value_counts().reset_index().rename(columns={'index': 'Country', 'Country': 'Count'})
report2_path = '/mnt/data/report2_wine_count_per_country.xlsx'
report2.to_excel(report2_path, index=False)

report3 = df.groupby('Country').agg({'Price': 'mean', 'Points': 'count'}).sort_values(by='Price', ascending=False).reset_index()
report3_path = '/mnt/data/report3_price_review_per_country.sqlite'
conn = sqlite3.connect(report3_path)
report3.to_sql('price_review', conn, if_exists='replace', index=False)
conn.close()

report4 = df.loc[df.groupby('Continent')['Points'].idxmax()][['Continent', 'Country', 'Points', 'Price']]
report4_path = '/mnt/data/report4_best_wines_per_continent.json'
report4.to_json(report4_path, orient='records')

exploration_info, report1_path, report2_path, report3_path, report4_path