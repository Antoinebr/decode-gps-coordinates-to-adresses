from db import db

import datetime, requests, time, csv


# We create a sqlite3 db 
myDB = db.DB("./mydb33.db")

# We create a table in sqlite3
# The table contains 3 collumn :  point | address | codepostal | data 
# data contains the a json object saved as text
# 
myDB.createTable("CREATE TABLE IF NOT EXISTS address (point TEXT, address TEXT, codepostal TEXT, data TEXT)")

dt = datetime.datetime

# We open the csv file to loop over 
with open('Climat-2021-2051-8.5-ete-hiver-raw.csv') as csvfile:

    # we transform the CSV file to a Python dictionary
    rows = csv.DictReader(csvfile)

    # We loop over the rows
    for row in rows:
        
        # We check if the point is not already decoded in the DB 
        result = myDB.get("SELECT count('point') as result FROM address WHERE point = "+str(row['# Point'])+" ")

        # If 0 result is found for the given point we continue
        print(type(result[0][0]))

        if result[0][0] == 0 :      
            
            print("Let's decode"+"https://nominatim.openstreetmap.org/reverse?format=json&lat="+str(row['Latitude'])+"&lon="+str(row['Longitude'])+"&zoom=18&addressdetails=1")
            
            # We request the openstreetmap.org API to decode the GPS coordinates 
            # @example : https://nominatim.openstreetmap.org/reverse?format=json&lat=41.4087&lon=9.1577&zoom=18&addressdetails=1
            # 
            r = requests.get("https://nominatim.openstreetmap.org/reverse?format=json&lat="+str(row['Latitude'])+"&lon="+str(row['Longitude'])+"&zoom=18&addressdetails=1")

            
            print(r.text)
            # If the request succeed
            if r.ok :

                # we conver the json data from the API to a dictionary 
                data = r.json()

                print(data)

                try: 
                    # We insert the value into our DB
                    myDB.insert("INSERT INTO address VALUES (?,?,?,?)",( str(row['# Point']), data['display_name'], data['address']['postcode'], r.text))
                
            
                except Exception as e:
                    print("An exception occurred : " + str(e))

                # We check the API every 1.2sec to not hit the limits
                time.sleep(1.2) 

            else: 

                print('error during the fetch')

        else:
            print(str(row['# Point'])+" alredy exists in our DB")
   