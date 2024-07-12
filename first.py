import pandas as pd


def convert_gross(value):
    if isinstance(value, str):
        # Remove dollar sign and convert 'M' to millions
        value = value.replace('$', '').replace(
            'M', '').replace(',', '').strip()
        return float(value) * 1e6  # Assuming 'M' means million
    return value


# Load the data
movies = pd.read_csv('D:/vphrase/movies.csv')

# Inspect the data
print(movies.info())
print(movies.head())

# Handle missing values
# movies.fillna({
#     'VOTES': 0,
#     'RunTime': movies['RunTime'].mean(),  # or another default value
#     'Gross': 0
# }, inplace=True)
movies['VOTES'] = movies['VOTES'].fillna('0').str.replace(',', '').astype(int)
movies['RunTime'] = movies['RunTime'].fillna(movies['RunTime'].mean())
movies['Gross'] = movies['Gross'].fillna('0').apply(convert_gross)
movies['RATING'] = movies['RATING'].fillna(0)
# Ensure consistency
movies['MOVIES'] = movies['MOVIES'].str.lower()
movies['GENRE'] = movies['GENRE'].str.lower()

# Remove duplicates
movies.drop_duplicates(inplace=True)

# Save the cleaned data to a new CSV file
movies.to_csv('D:/vphrase/new_movies.csv', index=False)

print("Data preprocessing completed successfully.")
