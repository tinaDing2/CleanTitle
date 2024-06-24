import pandas as pd

df = pd.read_excel('data_title.xlsx')

def clean_title(title):
    if '/' in title:
        return title.split('/')[0].strip()
    return title

df['Book Title'] = df['Book Title'].apply(clean_title)

df.to_excel('cleaned_spreadsheet.xlsx', index=False)

print("Book titles cleaned and saved to 'cleaned_spreadsheet.xlsx'")