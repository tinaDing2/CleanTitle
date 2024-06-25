import pandas as pd
import re

# The spreadsheet is read into a dataframe
df = pd.read_excel('data_title.xlsx')

# Function: clean the book titles by removing authorships 
def clean_title(title):
    patterns = {
        r"\.\s*s", #"." at the end of the string
        r"/by.*", #"/by" and everything after it
        r"\bby\b.*", #  "by" as a whole word and everything after it
        r"...by.*", #"… by" and everything after it
        r"/.*", # "/"
    }
    for pattern in patterns:
        title = re.sub(pattern, '', title)
    return title.strip()

# Application: to the column with book titles 
df['Book Title'] = df['Book Title'].apply(clean_title)

# Save: the cleaned dataframe is now to a new spreadsheet 
df.to_excel('cleaned_spreadsheet.xlsx', index=False)

print("Book titles cleaned and saved to 'cleaned_spreadsheet.xlsx'")
