import numpy as np
import pandas as pd

class OutlierRemoval():
    def __init__(self, data):
        self.data = data
        

    
       
    def iqr(self):
        binary_cols = [col for col in self.data.select_dtypes(include = ["int64", "float64"]) if self.data[col].nunique() <= 2]
        for i in self.data.select_dtypes(include = ["int64", "float64"]):
            if i not in binary_cols:
                q1 = self.data[i].quantile(0.25)
                q3 = self.data[i].quantile(0.75)
                iqr = q3-q1
                ub = q3+1.5*iqr
                lb = q1-1.5*iqr
                self.data[i] = np.where(self.data[i]>ub,ub,
                                           np.where(self.data[i]<lb,lb,
                                                   self.data[i]))
            else:
                pass
        return self.data
        
    def z_score(self):
    
        columns = self.data.select_dtypes(include=[np.number]).columns
        
        for col in columns:
            mean = self.data[col].mean()
            std = self.data[col].std()
                
            z_score = (self.data[col] - mean) / std
                
                # Keep only rows within threshold
            threshold = 3
            self.data = self.data[np.abs(z_score) <= threshold]
        
        return self.data