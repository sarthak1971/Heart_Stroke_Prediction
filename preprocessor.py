## preprocessing

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
class Preprocessing():
    def __init__(self, data):
        self.data = data
    def num_imputer(self):
        num_col = self.data.select_dtypes(include=["int64", "float64"])
        for i in num_col.columns:
            if self.data[i].isnull().sum()/len(self.data) <= 0.25:
                self.data[i] = self.data[i].fillna(self.data[i].median())
            else:
                self.data.drop(i, axis = 1 , inplace = True)
        return self.data
    def cat_imputer(self):
        cat_col = self.data.select_dtypes(include = ["object"])
        for i in cat_col.columns:
            not_input = str.lower(input(f"Enter{i} columns imp --> yes or no: "))
            if not_input=="yes" and self.data[i].isnull().sum()<0.25:
                self.data[i] = self.data[i].fillna(self.data[i].mode()[0])
            elif not_input=="yes" and self.data[i].isnull().sum()>0.25:
                self.data[i] = self.data[i].fillna("No Data")
            elif not_input == "no" and self.data[i].isnull().sum()<0.25:
                self.data[i] = self.data[i].fillna(self.data[i].mode()[0])
            else:
                self.data.drop(i, axis = 1, inplace = True)
        return self.data
        