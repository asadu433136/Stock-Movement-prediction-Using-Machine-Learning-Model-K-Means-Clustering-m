# -*- coding: utf-8 -*-
"""Largecap Asia Pacific (F).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rur2IAzazumgjTXA5cOXIuejX-3jj-ID
"""

#Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime
from sklearn.cluster import KMeans
import matplotlib.cm as cm
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.metrics import adjusted_rand_score
from sklearn.pipeline import make_pipeline

#import Companies name with tickers
companies_dict = {'SoftBank Group Corp.':'SFTBY',
    'Dai-ichi Life Holdings, Inc':'DCNSF',
    'Familymart  holdings co. LtdR':'FYRTY'}

#Get the data From WEB
data_source = 'yahoo' # Source of data is yahoo finance.
start_date = '2016' 
end_date = '2021'
df = web.DataReader(list(companies_dict.values()),
 data_source,start_date,end_date)
df.head()

#identifying that is there any null value in dataset.
df.isnull().values.any()

#takes a variable (X) with open and close 
X=df[['Open','Close']]
X.head()

#numpy array of transpose of (X) variables.
stock_open = np.array(df['Open']).T# stock_open is numpy array of transpose of df['Open']
stock_close = np.array(df['Close']).T # stock_close is numpy array of transpose of df['Close']

#Movement 
movements = stock_close-stock_open

#Plot the chart of Movement
plt.figure(figsize = (20,8)) 
ax1 = plt.subplot(2,3,1)
plt.title('SFTBY',fontsize = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 20)
plt.xlabel('Date',fontsize = 20)
plt.ylabel('Movement',fontsize = 20)
plt.plot(movements[0]) 
plt.subplot(2,3,2,sharey = ax1)
plt.title('DCNSF',fontsize = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 20)
plt.xlabel('Date',fontsize = 20)
plt.ylabel('Movement',fontsize = 20)
plt.plot(movements[1]) 
plt.subplot(2,3,3,sharey = ax1)
plt.title('FYRTY',fontsize = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 20)
plt.xlabel('Date',fontsize = 20)
plt.ylabel('Movement',fontsize = 20)
plt.plot(movements[2])

#Calculate sum of movement
sum_of_movement = np.sum(movements,1)

#Print the Changes of three companies
for i in range(len(companies_dict)):
 print('company:{}, Change:{}'.format(df['Open'].columns[i],sum_of_movement[i]))

#plot open and close column
plt.figure(figsize = (40,20)) # Adjusting figure size
ax1 = plt.subplot(2,3,1)
plt.title('Company:SFTBY',fontsize = 20)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 20)
plt.xlabel('Date',fontsize = 20)
plt.ylabel('Price',fontsize = 20)
plt.plot(df.iloc[0:]['Open']['SFTBY'],color='red',label = 'Open') # Opening prices are plotted against date
plt.plot(df.iloc[0:]['Close']['SFTBY'],color='blue',label = 'Close') # Closing prices are plotted against date
plt.legend(loc='upper left', frameon=False,framealpha=1,prop={'size': 22})
ax1 = plt.subplot(2,3,2)
plt.title('Company:DCNSF',fontsize = 20)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 20)
plt.xlabel('Date',fontsize = 20)
plt.ylabel('Price',fontsize = 20)
plt.plot(df.iloc[0:]['Open']['DCNSF'],color='red',label = 'Open') # Opening prices are plotted against date
plt.plot(df.iloc[0:]['Close']['DCNSF'],color='blue',label = 'Close') # Closing prices are plotted against date
plt.legend(loc='upper left', frameon=False,framealpha=1,prop={'size': 22})
ax1 = plt.subplot(2,3,3)
plt.title('Company:FYRTY',fontsize = 20)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 20)
plt.xlabel('Date',fontsize = 20)
plt.ylabel('Price',fontsize = 20)
plt.plot(df.iloc[0:]['Open']['FYRTY'],color='red',label = 'Open') # Opening prices are plotted against date
plt.plot(df.iloc[0:]['Close']['FYRTY'],color='blue',label = 'Close') # Closing prices  are plotted against date
plt.legend(loc='upper left', frameon=False,framealpha=1,prop={'size': 22})

#normalizer
from sklearn.preprocessing import Normalizer
normalizer = Normalizer() # Define a Normalizer
norm_movements = normalizer.fit_transform(X) # Fit and transform

#Print Normalizer range and mean values
print(norm_movements.min())
print(norm_movements.max())
print(norm_movements.mean())

#Plot the chart of Movement after normalize.
plt.figure(figsize = (20,8)) 
ax1 = plt.subplot(2,3,1)
plt.title('SFTBY',fontsize = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 20)
plt.xlabel('Date',fontsize = 20)
plt.ylabel('Movement',fontsize = 20)
plt.plot(norm_movements [0]) 
plt.subplot(2,3,2,sharey = ax1)
plt.title('DCNSF',fontsize = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 20)
plt.xlabel('Date',fontsize = 20)
plt.ylabel('Movement',fontsize = 20)
plt.plot(norm_movements [1]) 
plt.subplot(2,3,3,sharey = ax1)
plt.title('FYRTY',fontsize = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 20)
plt.xlabel('Date',fontsize = 20)
plt.ylabel('Movement',fontsize = 20)
plt.plot(norm_movements [2])

#Create KMeans algorithm 
model= KMeans(init = "k-means++", n_clusters = 2, n_init = 12,max_iter=1000)
model.fit(norm_movements)

#Create position in dataframe and predict the normalize movements
df['pos_clus'] = model.predict(norm_movements)

#searching in position which point have 1 and -1
df['pos_clus'] = np.where(df['pos_clus'] == 1,-1, 1)

#show the position values
df['pos_clus'].values

#Plotting the cluster
plt.figure(figsize=(30,15))
ax1 = plt.subplot(2,3,1)
plt.scatter(norm_movements[:, 0], norm_movements[:, 3],
c=df['pos_clus'], cmap='coolwarm',)
plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:, 3], s = 200, c = 'orange', label = 'Centroids')
plt.title('SFTBY')
plt.legend()
ax1 = plt.subplot(2,3,2)
plt.scatter(norm_movements[:, 1],norm_movements[:, 4],
c=df['pos_clus'], cmap='coolwarm')
plt.scatter(model.cluster_centers_[:,1],model.cluster_centers_[:, 4], s = 200, c = 'orange', label = 'Centroids')
plt.title('DCNSF')
plt.legend()
ax1 = plt.subplot(2,3,3)
plt.scatter(norm_movements[:, 2],norm_movements[:, 5],
c=df['pos_clus'], cmap='coolwarm')
plt.scatter(model.cluster_centers_[:,2],model.cluster_centers_[:, 5], s = 200, c = 'orange', label = 'Centroids')
plt.title('FYRTY')
plt.legend()
plt.show()

#Apply silhouette scoring method for cluster valuation
kmeans_silhouette = silhouette_score(norm_movements, model.labels_).round(2)
kmeans_silhouette

#plot silhouette score
fig, ax = plt.subplots(1, figsize=(15,8))
for i in [2]:
    model= KMeans(n_clusters=2, init='k-means++', random_state=0)
    kmeans_silhouette
    visualizer = SilhouetteVisualizer(model, colors='yellowbrick')
    visualizer.fit(norm_movements)

#Without trading Cost initialize Backtesiting trading strategy
Y= df['Adj Close']
Y

df1=Y.shift(1)
df1.dropna

#without Trading Cost Return
df['returns_SFTBY']= np.log(Y['SFTBY']/df1['SFTBY'])
df['returns_DCNSF']= np.log(Y['DCNSF']/df1['DCNSF'])
df['returns_FYRTY']= np.log(Y['FYRTY']/df1['FYRTY'])
df.head()

#Company SFTBY
np.sign(df['returns_SFTBY']).head()

df['returns_SFTBY']= df['returns_SFTBY'].fillna(0)
df['returns_SFTBY']

df['direction_SFTBY'] = np.sign(df['returns_SFTBY']).astype(int)
df['direction_SFTBY']

df['strat_clus_SFTBY'] = df['pos_clus'] * df['returns_SFTBY']
df[['returns_SFTBY', 'strat_clus_SFTBY']].sum().apply(np.exp)

(df['direction_SFTBY'] == df['pos_clus']).value_counts()

#Company AIG
np.sign(df['returns_DCNSF']).head()

df['returns_DCNSF']= df['returns_DCNSF'].fillna(0)
df['returns_DCNSF']

df['direction_DCNSF'] = np.sign(df['returns_DCNSF']).astype(int)
df['direction_DCNSF']

df['strat_clus_DCNSF'] = df['pos_clus'] * df['returns_DCNSF']
df[['returns_DCNSF', 'strat_clus_DCNSF']].sum().apply(np.exp)

(df['direction_DCNSF'] == df['pos_clus']).value_counts()

#Comapny FYRTY
np.sign(df['returns_FYRTY']).head()

df['returns_FYRTY']= df['returns_FYRTY'].fillna(0)
df['returns_FYRTY']

df['direction_FYRTY'] = np.sign(df['returns_FYRTY']).astype(int)
df['direction_FYRTY']

df['strat_clus_FYRTY'] = df['pos_clus'] * df['returns_FYRTY']
df[['returns_FYRTY', 'strat_clus_FYRTY']].sum().apply(np.exp)

(df['direction_FYRTY'] == df['pos_clus']).value_counts()

#Plot the chart without trading cost performence
plt.figure(figsize = (30,15)) # Adjusting figure size
ax1 = plt.subplot(2,3,1)
plt.title('Company:SFTBY',fontsize = 20)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 20)
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['returns_SFTBY'], color='red',label= 'return') 
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['strat_clus_SFTBY'],color='blue',label= 'strat_clus') 
plt.legend()
ax1 = plt.subplot(2,3,2)
plt.title('Company:DCNSF',fontsize = 20)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 20)
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['returns_DCNSF'],color='red',label= 'return')
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['strat_clus_DCNSF'],color='blue',label= 'strat_clus') 
plt.legend()
ax1 = plt.subplot(2,3,3)
plt.title('Company:FYRTY',fontsize = 20)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 20)
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['returns_FYRTY'],color='red',label= 'return') 
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['strat_clus_FYRTY'],color='blue',label= 'strat_clus') 
plt.legend()
plt.show()

#with trading cost initialize Backtesiting trading strategy
Z= df['Adj Close']+10
Z

df2=Z.shift(1)
df2.dropna

#with Trading Cost Return
df['returns_SFTBY_T']= np.log(Z['SFTBY']/df2['SFTBY'])
df['returns_DCNSF_T']= np.log(Z['DCNSF']/df2['DCNSF'])
df['returns_FYRTY_T']= np.log(Z['FYRTY']/df2['FYRTY'])
df.head()

#Comapany SFTBY with trading Cost
np.sign(df['returns_SFTBY_T']).head()

df['returns_SFTBY_T']= df['returns_SFTBY_T'].fillna(0)
df['returns_SFTBY_T']

df['direction_SFTBY_T'] = np.sign(df['returns_SFTBY_T']).astype(int)
df['direction_SFTBY_T']

df['strat_clus_SFTBY_T'] = df['pos_clus'] * df['returns_SFTBY_T']
df[['returns_SFTBY_T', 'strat_clus_SFTBY_T']].sum().apply(np.exp)

(df['direction_SFTBY_T'] == df['pos_clus']).value_counts()

#Company AIG with trading cost
np.sign(df['returns_DCNSF_T']).head()

df['returns_DCNSF_T']= df['returns_DCNSF_T'].fillna(0)
df['returns_DCNSF_T']

df['direction_DCNSF_T'] = np.sign(df['returns_DCNSF_T']).astype(int)
df['direction_DCNSF_T']

df['strat_clus_DCNSF_T'] = df['pos_clus'] * df['returns_DCNSF_T']
df[['returns_DCNSF_T', 'strat_clus_DCNSF_T']].sum().apply(np.exp)

(df['direction_DCNSF_T'] == df['pos_clus']).value_counts()

#Comapny FYRTY With Trading 
np.sign(df['returns_FYRTY_T']).head()

df['returns_FYRTY_T']= df['returns_FYRTY_T'].fillna(0)
df['returns_FYRTY_T']

df['direction_FYRTY_T'] = np.sign(df['returns_FYRTY_T']).astype(int)
df['direction_FYRTY_T']

df['strat_clus_FYRTY_T'] = df['pos_clus'] * df['returns_FYRTY_T']
df[['returns_FYRTY_T', 'strat_clus_FYRTY_T']].sum().apply(np.exp)

(df['direction_FYRTY_T'] == df['pos_clus']).value_counts()

#Plot the chart without trading cost performence
plt.figure(figsize = (30,15)) # Adjusting figure size
ax1 = plt.subplot(2,3,1)
plt.title('Company:SFTBY_Trading',fontsize = 20)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 20)
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['returns_SFTBY_T'], color='red',label= 'return') 
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['strat_clus_SFTBY_T'],color='blue',label= 'strat_clus') 
plt.legend()
ax1 = plt.subplot(2,3,2)
plt.title('Company:DCNSF_Trading',fontsize = 20)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 20)
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['returns_DCNSF_T'],color='red',label= 'return')
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['strat_clus_DCNSF_T'],color='blue',label= 'strat_clus') 
plt.legend()
ax1 = plt.subplot(2,3,3)
plt.title('Company:FYRTY_Trading',fontsize = 20)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 20)
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['returns_FYRTY_T'],color='red',label= 'return') 
plt.plot(df.cumsum().apply(np.exp).iloc[0:]['strat_clus_FYRTY_T'],color='blue',label= 'strat_clus') 
plt.legend()
plt.show()

