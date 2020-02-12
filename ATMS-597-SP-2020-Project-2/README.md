# ATMS 597 Spring 2020 - Project 2

### Group F: Xinchang Li, Yang Lu, Sarah Szymborski

This code will allow users to produce "climate stripes" (originally created [by Ed Hawkins at the University of Reading] (https://showyourstripes.info/)) with a time period of their choosing and an option to add a overlapping quantitative line plot. 

#### Data source:
- Global Historical Climatology Network (GHCN) - Daily data, from [NCEI API version 2](https://www.ncdc.noaa.gov/cdo-web/webservices/v2)

#### Required inputs:
- GHCN location and station IDs
- Start and end dates (in python.datetime format) of the query period
- Averaging frequency: weekly ('W'), monthly ('M') or yearly ('Y').
- A flag for whether to include the quantitative line plot (Boolean)

#### Outputs:
- Reduced dataset with user-specified frequency of the temperature anomaly (temperature departure from the average of the reference period)
- climate stripes (with the optional line plot if called for) in PNG.

#### Assumptions
- 

#### Caveats:
- User needs to have prior knowledge of the location and station IDs of their interest 
- Program will terminate if missing record is present in the user-specified time period
- 

------
Last updated: 02/12/2020
