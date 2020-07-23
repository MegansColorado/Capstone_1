# Capstone 1: COVID-19 v. Political Affiliation in California by County

## Overview: 
With the presidential election heating up there is significant debate on social media around whether the Corona virus pandemic is being overblown by the media. It is suggested that people that believe that it is a hoax and over blown are less likely to take safty precautions to reduce the spread of the virus (ie. PPE like masks, social distancing, etc)  Others believe that we are truly in a global pandemic. These 2 groups generally fall into distinct political parties: Republicans and Democrats.

My idea is to see if there is a correlation between COVID infection rates and political leanings for various counties in the state of California and their COVID infection rate as the state started to reopen May 12, 2020. 

## The Raw Data: 

Voting Data for political affiliation was obtained from the State od California's official website: https://www.sos.ca.gov/elections/prior-elections/statewide-election-results/presidential-primary-election-june-7-2016/statement-vote/
Format: 82KB .xls file

COVID-19 Data by county for California was obtained from California Dept of Public Health: https://data.chhs.ca.gov/dataset/california-covid-19-hospital-data-and-case-statistics
Format: 254 KB .csv file

Supplemental Data:
Population by county: https://www.california-demographics.com/counties_by_population
Format: .csv file

GeoJson Date(for maps): https://github.com/codeforamerica/click_that_hood/blob/master/public/data/california-counties.geojson
Format: 258KB .geojson file

Coordinates for each county(for maps): http://www.ala.org/rt/magirt/publicationsab/ca

#### California: presidential votes by county
Create map of counties by majority population political vote

![title](images/image1.png)

<img src="/images/Dem_Rep_Map_1.png"/>
<img src="/images/hash_bar.png" width=50% height=50%>


#### California COVID rates by county
Create map of which counties have highest rate of infections since restrictions lifted

Are the two maps correlated - is the correlations statistically significant?
Null Hypothesis: political affiliation of majority of the county is not correlated to increased COVID infections
Alt Hypothesis: political affiliation of majority of the county is correlated to increased COVID infections
