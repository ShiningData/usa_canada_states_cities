# The US.txt/CA.txt files from the Geonames dataset typically contain the following columns:
# country code: ISO country code
# postal code: Postal code format of the place. Note that in the US, postal codes are ZIP codes.
# place name: Name of the place (usually a city or town)
# admin name1: Name of the first-level administrative division (state)
# admin code1: ISO code for the first-level administrative division (state)
# admin name2: Name of the second-level administrative division (county)
# admin code2: ISO code for the second-level administrative division (county)
# admin name3: Name of the third-level administrative division
# admin code3: ISO code for the third-level administrative division
# latitude: Latitude of the place
# longitude: Longitude of the place
# accuracy: Accuracy of the location coordinates

import requests
import zipfile
import pandas as pd

def get_canada_provinces_cities():
    # Download and extract the dataset
    url = "http://download.geonames.org/export/zip/CA.zip"
    r = requests.get(url)
    with open("CA.zip", "wb") as f:
        f.write(r.content)

    with zipfile.ZipFile("CA.zip", "r") as zip_ref:
        zip_ref.extractall("CA")

        
def get_usa_states_cities():
    # Download and extract the dataset
    url = "http://download.geonames.org/export/zip/US.zip"
    r = requests.get(url)
    with open("US.zip", "wb") as f:
        f.write(r.content)

    with zipfile.ZipFile("US.zip", "r") as zip_ref:
        zip_ref.extractall("US")
        

def country_state_city_table():      
    column_names = [
                   "country_code",
                   "postal_code",
                   "city",
                   "state",
                   "state_code",
                   "county",
                   "county_code",
                   "admin_name3",
                   "admin_code3",
                   "latitude",
                   "longitude",
                   "accuracy"
    ]
    
    usa_df = pd.read_csv("US/US.txt", 
                         delimiter="\t", 
                         names=column_names, 
                         usecols=["country_code", 
                                  "state", 
                                  "state_code", 
                                  "city"
                                 ]
                        )
    
    ca_df = pd.read_csv("CA/CA.txt", 
                        delimiter="\t", 
                        names=column_names, 
                        usecols=["country_code", 
                                 "state", 
                                 "state_code", 
                                 "city"
                                ]
                       )
    
    result_df = pd.concat([usa_df, ca_df], axis=0)
    
    result_df.to_csv("country_state_city.csv", index=False)

    return result_df


def main():
    
    get_canada_provinces_cities()
    
    get_usa_states_cities()
    
    result_df = country_state_city_table()
    
    
if __name__ == "__main__":
    main()