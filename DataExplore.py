## exploring dataset: - shape, info, description, %missining value, outliers, duplicated
## create a module for exploring data

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
class DataExplore():
    def __init__(self, data):
        self.data = data
    def data_info(self):
        return self.data.info()
    def data_shape(self):
        print("Number of rows: ", self.data.shape[0])
        print("Number of columns: ", self.data.shape[1])
    def data_missining(self):
        miss = pd.DataFrame({
    "Columns": self.data.columns,
    "Missing Count": self.data.isnull().sum().values,
    "% Missing Value": list((self.data.isnull().sum().values) / len(self.data) * 100)
})
        return miss
    def outliers(self):
        for i in self.data.select_dtypes(include = ["int64", "float64"]):
            sns.boxplot(self.data[i])
            plt.title(f"{i}")
            plt.show()
    def duplicated(self):
        print(self.data.duplicated().sum())
    def report(self):
        print("Information about data:\n", self.data.info())
        print("Shape of data: ", self.data.shape)
        miss = pd.DataFrame({
    "Columns": self.data.columns,
    "Missing Count": self.data.isnull().sum().values,
    "% Missing Value": list((self.data.isnull().sum().values) / len(self.data) * 100)
})
        print("Missing Values :\n", miss)
        print("Duplicated Value :\n", self.data.duplicated().sum())
        print("Outliers detection: ")
        for i in self.data.select_dtypes(include = ["int64", "float64"]):
            sns.boxplot(self.data[i])
            plt.title(f"{i}")
            plt.show()