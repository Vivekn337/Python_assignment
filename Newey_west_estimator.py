# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:06:56 2020

@author: hp
"""
import numpy as np
import pandas as pd
df=pd.read_csv('BWGHT.csv')

class linear_model:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.b = np.linalg.solve(x.T@x,x.T@y)
        e = y-x@self.b
        self.vb = self.vcov_b(e)
        self.se = np.sqrt(np.diagonal(self.vb))
        self.t = self.b/self.se
    def vcov_b(self,e):
        x = self.x
        return e.var()*np.linalg.inv(x.T@x)
class newey_west(linear_model):
    def vcov_b(self,e):
        x = self.x
        meat = np.diagflat(np.repeat(e.var(),np.size(e)))
        lag_d=[]
        for i in range(len(e)-1):
            lag_d.append(e[i+1])
        cov_e=np.diagonal(np.fliplr(np.cov(lag_d,e[:len(e)-1])))
        print("Variance of error term:", np.var(e))
        print("Co-variance of error termand its lag:",cov_e[0])
        cov_e =np.repeat(cov_e[0],np.size(e)-1)
        for i in range(len(cov_e)):
            meat[i,i+1]= cov_e[i]
            meat[i+1,i]=cov_e[i]
        bread = np.linalg.inv(x.T@x)@x.T
        sandwich = bread@meat@bread.T
        print("Variance of beta:",sandwich)
        return sandwich

df['(intercept)'] = 1
x = df[['(intercept)','cigs','faminc']]
y = df['bwght']
print(linear_model(x,y).t)
print("T-stat :",newey_west(x,y).t)

