import matplotlib.pyplot as plt
import pandas as pd

def double_line_plot(repub_df, dem_df, title, x_label, y_label, repub_label, dem_label, filename=None):
    ''' creates a double line plot '''

    fig, ax = plt.subplots(figsize = (20,10))

    ax.plot(repub_df['date'], repub_df['%_pop_new_cases'],  alpha = 0.5, linewidth=3, color='red', label = repub_label)
    ax.plot(dem_df['date'], dem_df['%_pop_new_cases'], alpha = 0.2, linewidth=3, color = 'darkblue', label = dem_label)
    ax.set_title(title);
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.xticks(rotation=0)
    #ax.set_xticklabels(rotation=90)
    #ax.set_xlim(0, .1)
    ax.legend();

    if filename:
        plt.savefig("../images/"+ filename +'.png')


def repub_or_dem(df):

    ''' Categorizes Counties as either Republican or
    Democrat and adds new columns for sorting'''

    #add affiliation
    df['Affiliation'] = "Republican"
    df.loc[df['%_Democrat'] > 50, 'Affiliation'] = 'Democrat'
    #add code also
    df['Aff_Code'] = 0
    df.loc[df['%_Democrat'] > 50, 'Aff_Code'] = 1
    return df.head()


def import_databases(list_of_databases):
    for database in list_of_databases:
        database = pd.read_csv('../data/'+ 'database' + '.csv')
        try:
            database['date']=pd.to_datetime(database['date'])
            database.drop(axis=1, columns='Unnamed: 0', inplace=True)
        except:
            pass
        print(database.head(1))
        

