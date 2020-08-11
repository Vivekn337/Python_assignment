import numpy as np
import random
import seaborn as sns
import matplotlib.pyplot as plt

#simulation of bias for different value of alpha and different sample sizes
alpha=random.sample(range(1,10),5)
for a in range(len(alpha)):
    alp=alpha[a]
    rep = 10
    sample=[25,50,100,250,500]
    bias = np.zeros([rep,len(sample)])
    for ss in range(len(sample)):
        n=sample[ss]
        for re in range(rep):
            rho=0.5
            e= np.random.normal(size=(n,))
            x=e.copy()
            for i in  range(1,n):
                 x[i]=alp+rho*x[i-1]+e[i]
            ymat = x[1:]
            xmat = x[:-1].reshape(-1,1)
            xmat = np.hstack([np.ones((len(xmat),1)),xmat])
            beta=np.linalg.solve(xmat.T@xmat,xmat.T@ymat)
            bis = beta[1]-rho
            bias[re,ss]=bis
    plt.figure()
    for ss in range(len(sample)):
        sns.kdeplot(bias[:,ss],label=sample[ss])
    plt.title("Bias for Alpha = {0} rho = {1}".format(alp,rho))
    
    
    
#Simulation of bias for different values of phi in different sample sizes
rho=[]
for i in range(5):
    rho.append(random.random())
for a in range(len(rho)):
    rh=rho[a]    
    rep = 10
    sample=[25,50,100,250,500]
    bias = np.zeros([rep,len(sample)])
    for ss in range(len(sample)):
        n=sample[ss]
        for re in range(rep):
            alp=1
            e= np.random.normal(size=(n,))
            x=e.copy()
            for i in  range(1,n):
                 x[i]=alp+rh*x[i-1]+e[i]
            ymat = x[1:]
            xmat = x[:-1].reshape(-1,1)
            xmat = np.hstack([np.ones((len(xmat),1)),xmat])
            beta=np.linalg.solve(xmat.T@xmat,xmat.T@ymat)
            bis = beta[1]-rh
            bias[re,ss]=bis
    plt.figure()
    for ss in range(len(sample)):
        sns.kdeplot(bias[:,ss],label=sample[ss])
    plt.title("Bias for Alpha = {0} rho = {1}".format(alp,rh))
    
    
    
#Simulation of bias for different values of Variance of error term
var_e=random.sample(range(1,10),5)
for a in range(len(var_e)):
    rep = 100
    sample=[25,50,100,250,500]
    bias = np.zeros([rep,len(sample)])
    for ss in range(len(sample)):
        n=sample[ss]
        for re in range(rep):
            rho=0.5
            alp=1
            e= np.random.normal(scale=a,size=(n,))
            x=e.copy()
            for i in  range(1,n):
                 x[i]=alp+rho*x[i-1]+e[i]
            ymat = x[1:]
            xmat = x[:-1].reshape(-1,1)
            xmat = np.hstack([np.ones((len(xmat),1)),xmat])
            beta=np.linalg.solve(xmat.T@xmat,xmat.T@ymat)
            bis = beta[1]-rho
            bias[re,ss]=bis
    plt.figure()
    a=np.sqrt(a)
    for ss in range(len(sample)):
        sns.kdeplot(bias[:,ss],label=sample[ss])
    plt.title("Bias for Alpha = {0} rho = {1} variance of error term={2}".format(alp,rho,a))
    