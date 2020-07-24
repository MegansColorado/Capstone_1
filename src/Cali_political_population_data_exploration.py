#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ## 1. Bring in population data by County in CA: 
# * reformat and clean data to prep for merge on 'County'

# In[278]:


#need population of counties to see cases as a % of population
population_df = pd.read_html('https://www.california-demographics.com/counties_by_population', index_col = 0)[0].iloc[:-1,:]

#remove the word 'county' in column county, and save to folder
population_df['County'] = population_df['County'].str.replace(' County','')
population_df.to_csv('data/population_df.csv')
population_df.head()


# ## 2. Bring in votes by County in CA:
# * remove NaN values
# * remove extra formatted rows not needed ie. "percentage"
# * remove all candidates except for major: Hilary Clinton, Bernie Sanders, Donald Trump

# In[277]:


#read in data excluding Percent, NaN, and last row
political_df = pd.read_excel('data/California_president_county.xls', index_col = 0).iloc[1::3].iloc[:-1,:]

political_df.head()


# In[240]:


#drop NaNs
political_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
political_df.head(3)


# In[241]:


# rename columns to clean up names for candidates we want to keep
political_df = political_df.rename(columns={'Ted \nCruz': 'Ted Cruz', 'Ben\nCarson': 'Ben Carson'})
political_df['Ben Carson'].head(1)


# In[242]:


# new columns check
political_df.columns


# ### 3. Create New DF with candidates that make up 99% of the votes for each political party

# In[243]:


major_candidates_df = political_df[['Hillary Clinton', 'Bernie Sanders', 'Donald Trump', 'John R. Kasich', 'Ted Cruz', 'Ben Carson']].copy()
major_candidates_df.head(5)


# In[ ]:





# In[244]:


# add total vote categories by Democrats and Republicans
major_candidates_df['Republican Votes'] = major_candidates_df['Donald Trump'] + major_candidates_df['John R. Kasich'] + major_candidates_df['Ted Cruz'] + major_candidates_df['Ben Carson']
major_candidates_df['Democratic Votes'] = major_candidates_df['Hillary Clinton'] + major_candidates_df['Bernie Sanders']


major_candidates_df.head(3)


# In[246]:


#change the index, name the County Column

# major_candidates_df.reset_index(inplace=True)
# major_candidates_df.rename(columns = {'index': 'County'}, inplace=True)


# In[248]:


# add political affiliation by % of population
major_candidates_df['%_Republican'] = major_candidates_df['Republican Votes']/(major_candidates_df['Democratic Votes'] + major_candidates_df['Republican Votes']) *100
major_candidates_df['%_Democrat'] = major_candidates_df['Democratic Votes']/(major_candidates_df['Democratic Votes'] + major_candidates_df['Republican Votes']) *100
major_candidates_df.head(3)


# In[249]:


#categorize political affiliation 
def repub_or_dem(df):
    df['Affiliation'] = "Republican"
    df.loc[df['%_Democrat'] > 50, 'Affiliation'] = 'Democrat'
    
    return df.head()
    

repub_or_dem(major_candidates_df)


# In[258]:


#categorize political affiliation code
def repub_or_dem(df):
    df['Aff_Code'] = 0
    df.loc[df['%_Democrat'] > 50, 'Aff_Code'] = 1
    
    return df.head()
    

repub_or_dem(major_candidates_df)
#major_candidates_df.drop(axis=1, columns='Affiliation_Code', inplace=True)


# In[264]:


#save here
# major_candidates_df.to_csv('data/major_candidates_df.csv')


# ### 4. Map the counties by % Political Affiliation

# In[138]:


import folium


# In[268]:


# Political Affiliation

choroMap = folium.Map(location=(36.78,-119.42), zoom_start=6, control_scale = True) #instantiate blank map, chose 'california coord' to start


choroMap.choropleth(geo_data='data/california_counties.geojson',
                    data = major_candidates_df,
                    columns = ['County', '%_Democrat'],
                    key_on = 'feature.properties.name',
                    fill_color = 'RdYlBu', #'YlOrRd',
                    fill_opacity = 0.8,
                    line_opacity = 0.8,
                    legend_name = 'Political Affiliation by County')

choroMap.save('images/%_Political_Map_2.png')
choroMap


# In[ ]:





# In[270]:


Dem_Rep_Map = folium.Map(location=(36.78,-119.42), zoom_start=6, control_scale = True) #instantiate blank map, chose 'california coord' to start


Dem_Rep_Map.choropleth(geo_data='data/california_counties.geojson',
                    data = major_candidates_df,
                    columns = ['County', "Aff_Code"],
                    key_on = 'feature.properties.name',
                    fill_color = 'RdBu', #'YlOrRd',
                    fill_opacity = 0.8,
                    line_opacity = 0.8,
                    legend_name = 'Political Affiliation by County')
Dem_Rep_Map.save('images/Dem_Rep_Map_1.png') #can also save as PNG
#Dem_Rep_Map.savefig('images/Dem_Rep_Map_1.png', dpi=300)
Dem_Rep_Map


# In[ ]:





# ## everything below this cell is no longer used

# In[83]:


political_df.info()


# In[137]:


get_ipython().system('pip install folium')

