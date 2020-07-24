#!/usr/bin/env python
# coding: utf-8

# In[116]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### 1. Bring in COVID data by county
# * clean

# In[117]:


covid_df = pd.read_csv('data/california_covid_cases.csv',index_col = 0)
covid_df.head()


# In[25]:


# 60 counties
covid_df.index.nunique()


# In[29]:


covid_df.head(3)


# In[39]:


covid_df.index.unique()


# In[40]:


population_df.County.unique()


# In[ ]:





# ### 2. Bring in *cleaned* population data by County

# In[53]:


population_df = pd.read_csv('data/population_df.csv')
population_df.head(5)


# In[51]:


population_df.corr(method='pearson').round(3) # shouldnt this have a much higher correlation? Look up how this works!


# ### 3. Join Population and COVID databases
# * needed so we can get # of covid cases per capita

# In[55]:



#covid_main_df = covid_df.join(population_df.set_index('County'), how='inner')

covid_main_df.head(3)


# ### 4.  Find covid data as a % of county population

# In[58]:


covid_main_df['%_pop_new_cases'] = covid_main_df['newcountconfirmed']/covid_main_df['Population'] * 100
covid_main_df['%_pop_total_cases'] = covid_main_df['totalcountconfirmed']/covid_main_df['Population'] * 100
covid_main_df.tail()


# In[107]:


#prep for mapping - add County as column
# covid_main_df.reset_index(inplace=True) # so can plot as a column
# covid_main_df.rename(columns = {'index': 'County'}, inplace=True) #rename column to County

#save it
#covid_main_df.to_csv('data/covid_main_df.csv')


# In[109]:


july_15_snapshot_df = covid_main_df.loc[covid_main_df['date'] == '2020-07-15']
july_15_snapshot_df.head(60)

#save it
#july_15_snapshot_df.to_csv('data/july_15_snapshot_covid_df')


# ### 4. Create Maps: 
# #### For latest data - 1 day - July 15th, 2020
# 1. Total cases % of population
# 2. New cases as % of population

# In[113]:


import folium
from folium.plugins import HeatMap

Map = folium.Map(location = (36.78,-119.42), zoom_start=6, tiles='OpenStreetMap')
Map.choropleth(geo_data='data/california_counties.geojson',
                    data = july_15_snapshot_df,
                    columns = ['County', '%_pop_total_cases'],
                    key_on = 'feature.properties.name',
                    fill_color = 'YlOrBr',
                    fill_opacity = 0.9,
                    line_opacity = 0.2,
                    legend_name = 'Total Cases Percent Population')

Map.save('images/%poptotalcases_july15_Map_3.html')
#HeatMap(data=(collection of coords you want to use), radius=4, blur=2).add_to(Map)

Map


# In[ ]:





# In[114]:


# % of population new cases

Map = folium.Map(location = (36.78,-119.42), zoom_start=6, tiles='OpenStreetMap')
Map.choropleth(geo_data='data/california_counties.geojson',
                    data = july_15_snapshot_df,
                    columns = ['County', '%_pop_new_cases'],
                    key_on = 'feature.properties.name',
                    fill_color = 'YlOrBr',
                    fill_opacity = 0.9,
                    line_opacity = 0.2,
                    legend_name = 'Total NEW Cases Percent Population')

Map.save('images/%popNEWcases_july15_Map_4.html')
#HeatMap(data=(collection of coords you want to use), radius=4, blur=2).add_to(Map)

Map


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Items below this line not in use - exploratory

# In[21]:


covid_df.sort_values('date', ascending=True).head(5) 


# In[15]:


covid_df.groupby('county').agg({'newcountconfirmed':'mean','newcountdeaths':'mean'}) 

