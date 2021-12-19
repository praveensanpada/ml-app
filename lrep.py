import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR

#from sklearn.externals import joblib


def ans(pre):
    df = pd.read_csv("Salary_DataSet.csv")

    lr=LR()
    lr.fit(df[['Experences']],df['Salary'])
    y=lr.predict([[pre]])

    return y

