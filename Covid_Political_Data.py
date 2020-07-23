#!/usr/bin/env python
# coding: utf-8

# ## Outline for this notbook:
# * 1. Load data set
# * 2. Join data sets
# * 3. Create Republican and Democrat DF's 
# * 4. Graphics
#     * a. Mean NEW DAILY covid cases by Democratic/ Republican Counties
#     * b. Mean TOTAL DAILY covid cases by Democratic/ Republican Counties
#     * c. Mean cases per County (as a percent of the population) - ALL Dates
#     * d. Mean cases per County (as a percent of the population) - Dates after state reopening May 18th? **NOT FINISHED
#     
# * 5. Linear Regression Model for Republican Growth Rate and Democrat Growth Rate
# * 6. Correlation Matrix

# In[236]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




major_candidates_df = pd.read_csv('data/major_candidates_df.csv', index_col = 1)
covid_main_df = pd.read_csv('data/covid_main_df.csv', index_col = 1)
covid_main_df['date']= pd.to_datetime(covid_main_df['date'])
july_15_snapshot_df = pd.read_csv('data/july_15_snapshot_covid_df', index_col = 1)
july_15_snapshot_df['date']= pd.to_datetime(july_15_snapshot_df['date'])



try:
    major_candidates_df.drop(axis=1, columns='Unnamed: 0', inplace=True)
except:
    pass
major_candidates_df.head(1)



try:
    covid_main_df.drop(axis=1, columns='Unnamed: 0', inplace=True)
except:
    pass
covid_main_df.head()


try:
    july_15_snapshot_df.drop(axis=1, columns='Unnamed: 0', inplace=True)
except:
    pass
july_15_snapshot_df.head()


# ### 2. Join the data
# * BIG data set = covid_political_master
# * Day snapshot = covid_political_July15_df



covid_political_master_df = covid_main_df.join(major_candidates_df, how='inner')
covid_political_master_df.head(3)


covid_political_July15_df = july_15_snapshot_df.join(major_candidates_df, how='inner')
covid_political_July15_df.head(3)


# ### 3. Create Republican and Democrat DF's / Explore data



# create dem and rep dataframes
dems_df = covid_political_master_df[covid_political_master_df['Aff_Code'] == 1]
# dems_df.head()

repub_df = covid_political_master_df[covid_political_master_df['Aff_Code'] == 0]
repub_df.head(1)
dems_df.head(1)


fig, ax = plt.subplots()

ax.hist(repub_df['newcountconfirmed'], alpha = 0.2, label = 'Republicans New Cases ', density = None, bins = 12)
#ax.hist(dems_df['%_pop_new_cases'], alpha = 0.2, color = 'blue', label = 'Democrats New Cases', density = True, bins=12)
ax.set_title('Covid cases by Political Affiliation');
#ax.set_xlabel('% population new cases')
#ax.set_xlim(0, .1)
ax.legend();


fig, ax = plt.subplots(figsize = (20,10))

ax.scatter(repub_df['date'], repub_df['%_pop_new_cases'],  alpha = 0.2, color= 'red', label = 'Republican Counties ')
ax.scatter(dems_df['date'], dems_df['%_pop_new_cases'], alpha = 0.2, color = 'blue', label = 'Democratic Counties')
ax.set_title('Covid cases by Political Affiliation');
ax.set_xlabel('New Cases by County - % of Population')
plt.xticks(rotation=45)
#ax.set_xlim(0, .1)
ax.legend();


#### a. Mean NEW DAILY covid cases by Democratic/ Republican Counties



mean_daily_new_cases_dem = dems_df.groupby('date')['%_pop_new_cases'].mean().reset_index()
mean_daily_new_cases_dem.head(3)


mean_daily_new_cases_repub = repub_df.groupby('date')['%_pop_new_cases'].mean().reset_index()
mean_daily_new_cases_repub.head(3)


fig, ax = plt.subplots(figsize = (20,10))

ax.plot(mean_daily_new_cases_repub['date'], mean_daily_new_cases_repub['%_pop_new_cases'],  alpha = 0.5, linewidth=3, color='red', label = 'Republicans Mean New Daily Cases ')
ax.plot(mean_daily_new_cases_dem['date'], mean_daily_new_cases_dem['%_pop_new_cases'], alpha = 0.2, linewidth=3, color = 'darkblue', label = 'Democrats Mean New Daily Cases')
ax.set_title('Mean NEW Daily Cases by Political Affiliation');
ax.set_xlabel('3/18/2020 - 07/15/2020')
plt.xticks(rotation=90)
#ax.set_xticklabels(rotation=90)
#ax.set_xlim(0, .1)
ax.legend();

plt.savefig('images/dem_repub_meandailyNEWcases_Map_5.png')


# ## b. Mean TOTAL DAILY covid cases by Democratic/ Republican Counties


mean_daily_total_cases_dem = dems_df.groupby('date')['%_pop_total_cases'].mean().reset_index()
mean_daily_total_cases_dem.tail(3)

mean_daily_total_cases_repub = repub_df.groupby('date')['%_pop_total_cases'].mean().reset_index()
mean_daily_total_cases_repub.head(3)



fig, ax = plt.subplots(figsize = (20,10))

ax.plot(mean_daily_total_cases_repub['date'], mean_daily_total_cases_repub['%_pop_total_cases'],  alpha = 0.5, linewidth=3, color='red', label = 'Republicans Mean TOTAL Daily Cases ')
ax.plot(mean_daily_total_cases_dem['date'], mean_daily_total_cases_dem['%_pop_total_cases'], alpha = 0.2, linewidth=3, color = 'darkblue', label = 'Democrats Mean TOTAL Daily Cases')
ax.set_title('Mean TOTAL Daily Cases by Political Affiliation over time');
#ax.set_xlabel('3/18/2020 - 07/15/2020')
plt.xticks(mean_daily_total_cases_dem['date'][0::7], rotation=90)
#ax.set_xticklabels(rotation=90)
# ax.set_xlim(0, .1)
ax.set_yscale('log')
ax.legend();


plt.savefig('images/dem_repub_meandailyTOTALcases_Map_6.png')



# ### c. Mean cases per County (as a percent of the population) - ALL Dates


# currently for all days, WOULD BE INTERESTING ro do it after reopening.
mean_COUNTY_total_cases_dem = dems_df.groupby(['County','%_Republican'] )['%_pop_total_cases'].mean().reset_index()
mean_COUNTY_total_cases_dem.sort_values('%_pop_total_cases', inplace=True)
mean_COUNTY_total_cases_dem.head(3)


mean_COUNTY_total_cases_repub = repub_df.groupby(['County','%_Republican'])['%_pop_total_cases'].mean().reset_index()
mean_COUNTY_total_cases_repub.sort_values('%_pop_total_cases', inplace=True)
mean_COUNTY_total_cases_repub.head(3)

#scatter plot

fig, ax = plt.subplots(figsize = (20,10))

ax.scatter(mean_COUNTY_total_cases_dem['%_Republican'], mean_COUNTY_total_cases_dem['%_pop_total_cases'],  alpha = 0.5, linewidth=3, color='darkblue', label = 'Mean TOTAL Cases by COUNTY - Democrat')
ax.scatter(mean_COUNTY_total_cases_repub['%_Republican'], mean_COUNTY_total_cases_repub['%_pop_total_cases'], alpha = 0.2, linewidth=3, color = 'red', label = 'Mean TOTAL Cases by COUNTY - Republican')
ax.set_title('Mean Total per capita Cases by COUNTY');
ax.set_xlabel('DEMOCRAT <============sliding scale============> REPUBLICAN')
#plt.xticks(mean_COUNTY_total_cases_dem['date'][0::7], rotation=90)
#ax.set_xticklabels(rotation=90)
#ax.set_xlim(0, .1)
ax.legend();

plt.savefig('images/dem_repub_meanTOTALcases_sliding_scale_7.png')


# ### d. Mean cases per County (as a percent of the population) - Dates after state reopening May 18th? 


after_reopen_dems_df = dems_df.loc[dems_df['date'] >= '2020-05-18']
after_reopen_dems_df.head(3)


mean_COUNTY_total_cases_dem_after_reopen = after_reopen_dems_df.groupby(['County','%_Republican'] )['%_pop_total_cases'].mean().reset_index()
mean_COUNTY_total_cases_dem_after_reopen.sort_values('%_pop_total_cases', inplace=True)
mean_COUNTY_total_cases_dem_after_reopen.head(3)


after_reopen_repub_df = repub_df.loc[repub_df['date'] >= '2020-05-18']
after_reopen_repub_df.head(3)


# ### 5. Linear Regression Model for Republican Growth Rate and Democrat Growth Rate
# 



from sklearn.linear_model import LinearRegression as LR
X = (mean_daily_total_cases_repub['date'] - mean_daily_total_cases_repub['date'].min()).values.reshape(-1,1)/86400000000000
repub_model = LR().fit(X,  
    np.log(mean_daily_total_cases_repub['%_pop_total_cases']))
repub_growth_rate = np.exp(repub_model.coef_)
repub_growth_rate



X = (mean_daily_total_cases_dem['date'] - mean_daily_total_cases_dem['date'].min()).values.reshape(-1,1)/86400000000000
dem_model = LR().fit(X,  
    np.log(mean_daily_total_cases_dem['%_pop_total_cases']))
dem_growth_rate = np.exp(dem_model.coef_)
dem_growth_rate




#what does the intercept mean?
repub_model.intercept_, dem_model.intercept_







# ### 6. Correlation Matrix 

covid_political_July15_df.corr(method='pearson').round(3)






# ### 7. Hypothesis Testing
# 
# **H null: there is no difference between COVID rates from Republican and Democratic Counties**
# 
# **H alt: there is a difference between COVID rates in Republican and Democratic Counties**
# 
# * Sample 1: Democratic Counties: mean county total cases by % of population
# 
# * Sample 2: Republican Counties: mean county total cases by % of population
# 
# alpha = .05



from scipy.stats import ttest_ind
sample_1 = mean_COUNTY_total_cases_dem['%_pop_total_cases']
sample_2 = mean_COUNTY_total_cases_repub['%_pop_total_cases']



t_statistic, p_value = ttest_ind(sample_1, sample_2, equal_var=False)

f't_statistic: {t_statistic}, p_value: {p_value}'


# **Conclusion of TTEST: Reject the Null Hypothesis. Accept the Alt Hypothesis** 


len(sample_1), len(sample_2)

plt.hist(sample_1, bins=36)

plt.hist(sample_2, bins=22)


#Personr test (results= correlation, p-value) COULDNT GET THIS TO WORK _ COME BEACK IF TIME

# from scipy.stats import pearsonr
#pearsonr(covid_political_master_df['%_Republican'], covid_political_master_df['%_pop_total_cases'])
#covid_political_master_df['%_Republican']
#covid_political_master_df['%_pop_total_cases']




# ### Mann Whitney U Test
# 
# * After looking at the distributions of Sample1 and Sample2 we noticed that they do not look normal. Kin-Yip suggested running a MW test
# 
# * Sample_3: July 15th (last day) snapshot - Democrats
# * Sample_4: July 15 (last day) snapshot - Republicans


# use the covid snapshot data,ie last date  

from scipy.stats import mannwhitneyu

#create dem and repub DF
dems_covid_political_July15_df = covid_political_July15_df.loc[covid_political_July15_df['Aff_Code'] == 1]
repub_covid_political_July15_df = covid_political_July15_df.loc[covid_political_July15_df['Aff_Code'] == 0]

#create samples
sample_3 = dems_covid_political_July15_df['%_pop_total_cases']
sample_4 = repub_covid_political_July15_df['%_pop_total_cases']

#run test
stats_value, p_value = mannwhitneyu(sample_3, sample_4, use_continuity=True, alternative=None)
print(f'Mann-Whitney U statistic: {stats_value}, p-Value: {p_value}')


# **Conclusion of Mann-Whitney U: Reject the Null Hypothesis. Accept the Alt Hypothesis**

len(sample_3), len(sample_4)

plt.hist(sample_3, bins=36)

plt.hist(sample_4, bins=22)


# from pandas.plotting import scatter_matrix
# scatter_cols = ['tot_lpss', 'lpss_per_1000', 'tot_hpss',
#        'hpss_per_1000', 'pct_hpss',
#        'pct_vehicle_avail', 'pct_poverty']
# df_sub = df[scatter_cols]
# scatter_matrix(df_sub, alpha = 0.2, figsize = (20, 20), diagonal = 'kde');

