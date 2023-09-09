
# Address Geocoding with Google Maps API

This Python script allows you to geocode a list of addresses stored in an Excel file using the Google Maps API. It extracts latitude and longitude information from the addresses and saves the results in separate Excel files. This README provides an overview of the script and instructions for usage. The locations used are from the known places where GSSI members can use the lunch coupons.

This code outputs two files (`output_1.xlsx` and `output_2.xlsx`) that I used to create a map with all this locations, feel free to check it [here](https://www.google.com/maps/d/edit?mid=1-IRMtJksBr_xkyD0hQByjJsrim1D4Ds&usp=sharing)

>  DISCLAIMER: Given that anyone with access to the map can add new locations, I restricted the access so it only works if you access it using a GSSI account.

## Prerequisites

Before using this script, you need to ensure you have the following:

1. **Google Maps API Key:** You must obtain a Google Maps API key and replace the `key` variable with your API key in the script. Check [this](https://developers.google.com/maps/documentation/geocoding/overview) for details.

2. **Python and Required Libraries:** Make sure you have Python installed on your system. You'll also need to install the necessary libraries, which you can do using `pip`:

   ```bash
   pip install pandas googlemaps
   ```

3. **Excel File:** Prepare an Excel file (XLSX format) containing a list of addresses with specific column names (e.g., 'INDIRIZZO_LOCALE_COMPLETO', 'LOCALITA_DEL_LOCALE', 'CAP_LOCALE', 'REGIONE_LOCALE', 'PROVINCIA_LOCALE').

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd address-geocoding-google-maps
   ```

3. Edit the script to add your Google Maps API key:

   ```python
   # set your key here
   key = "YOUR_GOOGLE_MAPS_API_KEY"
   ```

4. Place your Excel file with the address data in the same directory and update the `xlsx_file_path` variable in the script with the file name.

5. Run the script:

   ```bash
   python geocode_addresses.py
   ```

6. The script will geocode the addresses and create two output XLSX files, `output_1.xlsx` and `output_2.xlsx`, including the latitude and longitude coordinates.

## Notes

- Google Maps API is not free, but for newly created accounts you get a credit that is more than enough for a few addresses like in this example.
- When importing the `output` files, Google Maps only imports 2000 rows per file. That's why you need to split the data into several files.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

Built with ❤️ by [Joaquín Amigó Vega](https://github.com/jamigov)
