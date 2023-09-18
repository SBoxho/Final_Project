#%%
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('C:/Users/vanes/Desktop/BSE/Term 1/Brush-up/Python/Final project/COVID19_state.csv')
data.head()
# %%
data_time = pd.read_csv('C:/Users/vanes/Desktop/BSE/Term 1/Brush-up/Python/Final project/us_states_covid19_daily.csv')
data_time.head()

# %%
#evolution of number of cases over time
positive_over_time = pd.DataFrame(data_time.groupby('date')['positive'].sum())
positive_over_time = positive_over_time.reset_index()
positive_over_time

#%%
#positive_over_time['date'] = pd.to_datetime(positive_over_time['date'], format='%Y%m%d')
positive_over_time
# %%
plt.figure(figsize=(10, 6))  
plt.plot(positive_over_time['date'], positive_over_time['positive'], linestyle='-')

plt.xlabel('Date')
plt.ylabel('Positive')
plt.title('Line Chart of Positives Over Time')
plt.yscale('linear')
# %%
positive_over_time['date'].max()
#%%
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC"
}
    
# invert the dictionary
abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))
data['State'].replace(us_state_to_abbrev, inplace=True)
# %%
#effects of tests based on infections
data['Percentage tested'] = data['Tested'] / data['Population'].astype(float)
data['Percentage infected'] = data['Infected'] / data['Population'].astype(float)
plt.scatter(data['Percentage tested'], data['Percentage infected'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Percentage tested'], row['Percentage infected']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

plt.xlabel('Percentage tested')
plt.ylabel('Percentage infected')
# -> the more tested the more are infected because it's diagnosted

# %%
#effects of tests based on deaths
data['Percentage deaths'] = data['Deaths'] /data['Population'].astype(float)
plt.scatter(data['Percentage tested'], data['Percentage deaths'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Percentage tested'], row['Percentage deaths']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Percentage tested')
plt.ylabel('Percentage death')

# %%
#subgroups that suffered most
data_sorted_deaths= data.sort_values(by='Percentage deaths', ascending=False)
data_sorted_deaths

# %%
plt.scatter(data['Income'], data['Percentage deaths'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Income'], row['Percentage deaths']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Income')
plt.ylabel('Percentage deaths')
# -> states with higher income had more deaths compared to their population size

#%%
#A sex ratio is the ratio of female to males in a population.
plt.scatter(data['Sex Ratio'], data['Percentage deaths'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Sex Ratio'], row['Percentage deaths']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Sex Ratio')
plt.ylabel('Percentage deaths')
# -> Men suffered more from Covid19
#%%
plt.scatter(data['Pop Density'], data['Percentage deaths'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Pop Density'], row['Percentage deaths']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Pop Density')
plt.ylabel('Percentage deaths')

# -> no clear statement because DC is a outlier
plt.xlim(0, 1270)
# -> States with high Population Density had more deaths -> People in overcrowded areas suffered more


#%%
plt.scatter(data['Unemployment'], data['Percentage deaths'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Unemployment'], row['Percentage deaths']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Unemployment')
plt.ylabel('Percentage deaths')
# -> no clear statement

# %%
plt.scatter(data['Smoking Rate'], data['Percentage deaths'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Smoking Rate'], row['Percentage deaths']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Smoking Rate')
plt.ylabel('Percentage deaths')
# -> no clear statement
# %%
plt.scatter(data['Age 55+'], data['Percentage deaths'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Age 55+'], row['Percentage deaths']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Age 55+')
plt.ylabel('Percentage deaths')
# -> no clear statement
# %%
plt.scatter(data['Age 0-25'], data['Percentage infected'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Age 0-25'], row['Percentage infected']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Age 0-25')
plt.ylabel('Percentage infected')
# -> the stated with more younger people had higher percentage of people infected 
# -> confinement measures
# %%
plt.scatter(data['Age 26-54'], data['Percentage infected'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Age 26-54'], row['Percentage infected']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Age 26-54')
plt.ylabel('Percentage infected')
# %%
#%%
plt.scatter(data['Urban'], data['Percentage infected'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Urban'], row['Percentage infected']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Urban')
plt.ylabel('Percentage infected')
# -> urbanisation doesn't have much of an impact on spreading
# -> no confinement measures
# %%
#%%
plt.scatter(data['Temperature'], data['Percentage infected'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Temperature'], row['Percentage infected']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Temperature')
plt.ylabel('Percentage infected')
# -> higher infection rates in warmer states
# -> important to set confinement measures first / fast
# %%
#IMPORTANT FOT THE ARGUMENTATION / REPORT
data['Persons per ICU Bed'] = data['Population'] / data['ICU Beds'].astype(float)
plt.scatter(data['Persons per ICU Bed'], data['Percentage deaths'])
for i, row in data.iterrows():
    plt.annotate(row['State'], (row['Persons per ICU Bed'], row['Percentage deaths']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
plt.xlabel('Persons per ICU Bed')
plt.ylabel('Percentage deaths')
# -> NUmber of ICU Beds has no impact on the death percentage
# %%
