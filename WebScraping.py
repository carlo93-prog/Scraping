# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 13:09:47 2022

@author: CarloNicolai

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd 
import datetime 
import os
import glob

#%%

website ='https://www.football-data.co.uk/italym.php'
path = r'C:\Users\CarloNicolai\OneDrive - Lobra S.r.l\Desktop\chromedriver.exe'
service =Service(executable_path=path)

#%%

driver=webdriver.Chrome(service=service)


#%%

driver.get(website)

#%%

links=[]
serie_a = []
currentDate =str(datetime.date.today())
getlastcsv=currentDate[2:4]

#%%

elems = driver.find_elements(by="xpath",value="//a[contains(@href,'.csv')]['Text']")
for elem in elems:
    links.append(elem.get_attribute("href"))
    for link in links:
        if 'I1' in link:
                serie_a.append(link)
files =list(set(serie_a))
for item in files:
   if getlastcsv == item[42:44]:
    current_season= item
print(current_season)

#%%
def function (path1,path2):
    stagione_1=path1[40:44]
    stagione_2=path2[40:44]
    df1= pd.read_csv(path1,error_bad_lines=False)
    df1['Stagione']=stagione_1
    df2= pd.read_csv(path2,error_bad_lines=False)
    df2['Stagione']='SS' +''+ str(stagione_2)
    lista1=list(df1.columns)
    lista2=list(df2.columns)
    check=[]
    for item in lista1 :
        if item in lista2:
            check.append(True)
        else:
            check.append(False)

    for position,item in enumerate(check):
        if item ==False:
            df2.insert(loc = position,
              column = df1.columns[position],
              value=None)
    df2.drop(columns=df2.iloc[:,105:len(df2.columns)-1].columns.tolist(), inplace=True)
    file_name=path2[40:44]
    return df2.to_csv(r'C:\Users\CarloNicolai\OneDrive - Lobra S.r.l\Desktop\data\Serie_A{}.csv'.format(file_name))

#%%
for file in files :
    function(current_season,file)
print('done')
#%%

folder = r'C:\Users\CarloNicolai\OneDrive - Lobra S.r.l\Desktop\data'
path = folder+"/**/*.csv"


df = pd.concat(map(pd.read_csv, glob.iglob(path, recursive=True)))

df.to_csv(r'C:\Users\CarloNicolai\OneDrive - Lobra S.r.l\Desktop\data\Serie_a.csv')
