# set your Google Maps API key here
key = ""

import pandas as pd
import googlemaps 

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key=key)

# Specify the path to your XLSX file
xlsx_file_path = 'tab_b_lotto_8.xlsx'

# Read the XLSX file into a DataFrame
df = pd.read_excel(xlsx_file_path)

# Create two new columns, 'LATITUDE' and 'LONGITUDE', in the dataframe and initialize them to empty strings
df['LATITUDE'] = ''
df['LONGITUDE'] = ''

# Iterate through each row in the dataframe
for index, row in df.iterrows():
    # Construct a query string for geocoding using address-related columns in the dataframe
    result = '{}, {}, {}, {}, {}'.format(row['INDIRIZZO_LOCALE_COMPLETO'], row['LOCALITA_DEL_LOCALE'], row['CAP_LOCALE'], row['REGIONE_LOCALE'], row['PROVINCIA_LOCALE'])

    # Use the Google Maps API to geocode the address query and get the result
    geocode_result = gmaps.geocode(result)

    # Extract and store the latitude and longitude from the geocode result
    df.at[index, 'LATITUDE'] = geocode_result[0].get('geometry').get('location').get('lat')
    df.at[index, 'LONGITUDE'] = geocode_result[0].get('geometry').get('location').get('lng')

# Save the DataFrame to two different XLSX files because Google Maps only accepts 2000 rows when importing the file
# The first file contains the first 1800 rows
df.iloc[0:1800].to_excel('output_1.xlsx', index=False)

# The second file contains the remaining rows
df.iloc[1800:-1].to_excel('output_2.xlsx', index=False)
