# Decode a list of GPS coordinates to adresses 

## What you need 

* Python3 
* Jupyter notebook 
* Some very basic knowledge of Python


## Project specific 

For this test the CSV looks like this  

```
# Point,Latitude,Longitude,Contexte,Période,Saison,NORTAV,NORTNAV,NORTXAV,NORTRAV,NORTXQ90,NORTXQ10,NORTNQ10,NORTNQ90,NORTXND,NORTNND,NORTNHT,NORTXHWD,NORTNCWD,NORTNFD,NORTXFD,NORSD,NORTR,NORHDD,NORCDD,NORPAV,NORPINT,NORRR,NORPFL90,NORRR1MM,NORPXCWD,NORPN20MM,NORPXCDD,ATAV,ATNAV,ATXAV,ATRAV,ATXQ90,ATXQ10,ATNQ10,ATNQ90,ATXND,ATNND,ATNHT,ATXHWD,ATNCWD,ATNFD,ATXFD,ASD,ATR,AHDD,ACDD,APAV,APINT,ARR,APFL90,ARR1MM,APXCWD,APN20MM,APXCDD
282,41.4087,9.1577,RCP8.5,H1,1,10.54,7.15,13.93,6.79,16.63,10.83,3.1,11.21,3,3,9,0,0,1,0,0,0,582.82,0,3.17,9.07,285.72,82.67,30.83,6,3,14,1.06,0.89,1.22,0.34,1.19,1.17,1.17,0.95,2,-3,4,0,0,-2,0,0,0,-95.94,0,-0.07,0.29,-7.15,1.01,-1.84,0,0,0
282,41.4087,9.1577,RCP8.5,H1,3,24.15,20.23,28.07,7.84,31.81,23.82,17.05,22.77,10,0,6,2,0,0,0,76,54,0.54,567.22,0.64,6.98,58.97,68.32,7.97,2,0,38,1.8,1.77,1.84,0.07,1.7,1.94,1.98,1.44,7,-1,5,2,0,0,0,16,28,-2.02,161.45,0.26,1.53,23.6,17.22,1.6,0,0,-6
423,41.4925,8.9759,RCP8.5,H1,1,10.11,6.86,13.37,6.5,16.02,10.2,3.02,10.79,3,3,8,0,0,1,0,0,0,621.35,0,3.21,8.98,289.94,82.3,31.53,6,4,13,1.02,0.83,1.21,0.37,1.16,1.16,1.2,0.94,2,-2,3,0,0,-2,0,0,0,-92.32,0,-0.02,0.08,-1.59,1.54,-0.67,0,1,-2
423,41.4925,8.9759,RCP8.5,H1,3,23.38,19.67,27.09,7.42,31.02,22.83,16.55,22.24,11,0,5,2,0,0,0,68,42,0.67,497.04,0.46,5.58,42.09,51.27,6.7,2,0,44,1.61,1.66,1.55,-0.11,1.56,1.54,1.85,1.5,7,-1,4,2,0,0,0,15,24,-3.24,141.43,0.02,0.21,1.85,-3.1,-0.53,0,0,2
```
see : ``` Climat-2021-2051-8.5-ete-hiver-raw.csv ```


<hr>

### step 1 

Decode the GPS coordinates and create a database : see coments in ```app.py``` 

You will need the following packages : 
* requests 
    -  ```pip install requests```

* sqlite3 
    -  ```pip install sqlite3```

To visualize the databse : https://inloop.github.io/sqlite-viewer/# 

### step 2 

You will need the following packages : 
* jupyter 
    -  ```python3 -m pip install jupyter```

type : ```jupyter notebook``` and open the Adresses.ipynb

Attach the data form our database to our csv and save a new version : see coments in ```Adresses.ipynb``` 

