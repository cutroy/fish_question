import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split  
import random
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
seed = random.randint(1,100000)
pd.set_option("future.no_silent_downcasting", True)
data=pd.read_csv("fish_data.csv")
data.fillna(-1,inplace=True)
fish_names = data["species"].unique()
for i in range(len(fish_names)):
    data['species']=data['species'].replace(fish_names[i],i+1)
print(data.head())