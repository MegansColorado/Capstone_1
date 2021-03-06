# COVID-19 and Political Affiliation in California by County
<img src="https://github.com/MegansColorado/Capstone_1/blob/master/images/politics_of_covid.jpg" alt="raw" width=100% height=100%/>
<br>

## **A. An Overview** 
With the presidential election heating up there is significant debate on social media around whether the Corona virus pandemic is being overblown by the media. It is suggested that Americans who believe that COVID-19 is a hoax and over blown in the media are less likely to take safety precautions to reduce the spread of the virus (ie. PPE like masks, social distancing, etc).  Many other Americans believe that we are truly in a global pandemic and are likely to follow the state mandates more consistently. While there are many debateable reasons for why this is the case, the 2 lines of thought can generally be bucketed into the 2 major political parties: Republican or Democrat.

MVP: The question I would like to answer is if there is a correlation between COVID infection rates and political affiliation for various counties in the state of California. MVP+ would be to see if there is any difference since the state started to reopen around May 18, 2020.  

## **B. The Raw Data** 

1. Voting Data for political affiliation was obtained from the State od California's official website: https://www.sos.ca.gov/elections/prior-elections/statewide-election-results/presidential-primary-election-june-7-2016/statement-vote/

    Format: 82KB .xls file

    *Original data (first image) needed some reformatting to be usable. Removed NaN and other extraneous rows during import (second image).*

    <img src="images/first_read_political_data.png" alt="raw" width=50% height=50%/><img src="images/political_clean_read_in.png" alt="raw" width=50% height=50%/>
<br>





2. COVID-19 Data by county for California was obtained from California Dept of Public Health: https://data.chhs.ca.gov/dataset/california-covid-19-hospital-data-and-case-statistics

    Format: 254 KB .csv file
    
    *This data was already pretty clean at download with very few to none formatiing issues or NaN values.* 

    <img src="images/covid_screenshot.png" alt="raw" width=50% height=50%/><img src="images/covid_info.png" alt="raw" width=50% height=50%/>
<br>

*Supplemental Data:*

3. Population by County: https://www.california-demographics.com/counties_by_population

    Format: .csv file

    <img src="images/pop_data_clean.png" alt="raw" width=50% height=50%/>



4. GeoJson Date(for maps): https://github.com/codeforamerica/click_that_hood/blob/master/public/data/california-counties.geojson 


    Format: 258KB .geojson file

    <img src="images/geojson_data_screenshot.png" alt="raw" width=50% height=50%/>


5. Coordinates for each county(for maps): http://www.ala.org/rt/magirt/publicationsab/ca

## **C. Data Visualization**
### 1. California Political Affiliation by County:
Maps, code, and data cleaning for this section can be found in notebook titled 'Cali_political_population_data_exploration.'

<img src="images/Dem_Rep_Map_1.png" alt="raw" width=50% height=50%/><img src="https://github.com/MegansColorado/Capstone_1/blob/master/images/%25_Political_Map_2.png" alt="raw" width=50% height=50%/> 

**First Political Image - Democrat v. Republican Map:**
Democratic counties tend to be along the coast and have cities with higher population densities, Republican Counties are further inland and more rural populations.

**Second Political Image - % Political Affiliation Map:**
This map goes beyond Democrat/Republican to show % of the counties political affiliation. You may notice that there are very few counties that are 'mostly' Democrat or Republican.


### 2. California COVID Rates by County
Maps, code, and data cleaning for this section can be found in notebook titled 'Cali_covid_data_exploration.'

<img src="https://github.com/MegansColorado/Capstone_1/blob/master/images/%25poptotalcases_july15_Map_3.png" alt="raw" width=50% height=50%/><img src="https://github.com/MegansColorado/Capstone_1/blob/master/images/%25popNEWcases_july15_Map_4.png" alt="raw" width=50% height=50%/>

**First COVID Image - TOTAL COVID cases as a % of population as of July 15, 2020:**
This shows total (cumulative) cases in each county and is normalized by population. 

**Second COVID Image - NEW COVID cases as a % of population as of July 15,2020:**
This is a snapshot of only new cases as of the last day data was pulled for this project. Notice the overlap from the counties in the previous map. 



### 3. Political and COVID 
Maps, code, and data cleaning for this section (and the remaining sections) can be found in the notebook titled 'Covid_Political_Data.'

*....Now that we have explored each data set individually we can set out to better understand if political affiliation is correlated to COVID cases. Its not easy to tell if they are correlated just using the above maps.  (joined data sets for the following visualizations)* 

<img src="images/dem_repub_meandailyNEWcases_Map_5.png" alt="raw" width=100% height=100%/> 

**Mean New Daily Cases for Republican vs. Democratic Counties (above):**
While not identical, it does appear that new daily cases seem to loosely mimic trends for both political affiliations.

 <img src="images/dem_repub_meandailyTOTALcases_Map_8.png" alt="raw" width=50% height=50%/><img src="images/dem_repub_meandailyTOTALcases_Map_6.png" alt="raw" width=50% height=50%/>  

**Mean TOTAL Daily Cases for Republican vs. Democratic Counties (First image above) and LOG version (Second image above):** These graphs seem to underscore that while Democratic counties have a higher % of covid cases per population, both types of counties have generally the same trajectory. There is an interesting narrowing of the lines around late June, early July where it appears Republican counties are increasing faster than Democratic counties. 

 <img src="images/dem_repub_meanTOTALcases_sliding_scale_7.png" alt="raw" width=75% height=75%/>

 **Mean TOTAL cases (all counties and all days) vs. % Republican <==> % Democrat (sliding scale):** While an interesting excersize this graph doesnt tell us much other than making it obvious that there are more Democrat Counties (36 Counties) than Republican (22 Counties)


## **D. Hypothesis Testing**
In the state of California, is political affiliation and COVID cases correlated?

**H null: there is no difference between COVID rates from Republican and Democratic Counties**

**H alt: there is a significant difference between COVID rates in Republican and Democratic Counties**
### **1. T-Test**
* Sample 1: Democratic Counties: mean county total cases by % of population   
* Sample 2: Republican Counties: mean county total cases by % of population
* alpha = .05

<img src="images/ttest.png" alt="raw" width=100% height=100%/>

*Based on the ttest returning a p-value of .046 we would fail to reject the null hypothesis.*

<img src="images/ttest_dems.png" alt="raw" width=50% height=50%/><img src="images/ttest_repubs.png" alt="raw" width=50% height=50%/>

*When we plot the samples above we see that they do not have a normal distribution... so this may not be all that helpful.*

### **2. Mann Whitney U Test**

The Mann-Whitney U test is used to compare differences between two independent groups when the dependent variable is either ordinal or continuous, but not normally distributed.

* Sample_3: July 15th (last day) snapshot - Democrats
* Sample_4: July 15 (last day) snapshot - Republicans
* alpha = .05

<img src="images/mannwhitneyu_test.png" alt="raw" width=100% height=100%/>

*Based on the Mann Whitney U test returning a P-Value of .0213 we would reject the null hypothesis.*

<img src="images/mwU_dems.png" alt="raw" width=50% height=50%/><img src="images/mwU_repubs.png" alt="raw" width=50% height=50%/>

* Histograms of Sample 3 and Sample 4 (above) showing non-normal distributions. 

### E. Linear Regression

<img src="images/linear_regression_covid_cali.png" alt="raw" width=100% height=100%/>

* Republican Counties show a growth rate for the virus is 4.5%  per day 
* Democratic Counties show a growth rate of 3.7% per day 

### **Based on the hypothesis tests and the growth rates above, we can conclude that there is a significant difference in COVID rates between Democratic and Republican Counties in California.**

### F. Future Actions

Moving forward we could do the same for each state in the US and consider how political messaging differs to each group from their respective parties. Would also like to adjust for difference in population densities. 

<img src="https://github.com/MegansColorado/Capstone_1/blob/master/images/covidpolitics.jpg" alt="raw" width=50% height=50%/>
