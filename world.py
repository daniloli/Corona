
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dataset=pd.read_csv('full_data.csv')
x=dataset.iloc[:,0:2].values
y=dataset.iloc[:]['total_cases'].values
dic={}

for i in range(len(y)):
    try:
        dic[x[i][1]].append(y[i])
    except(KeyError):
        dic[x[i][1]]=[]
        dic[x[i][1]].append(y[i])
        

world=dic['World']

#plt.plot(np.linspace(0,len(world)-1,num=len(world)),world)
#legend=[]
#for l in dic:
#    if l!='World' and l!='China':
#        if dic[l][-1]>1000:
#            plt.plot(np.linspace(0,len(dic[l])-1,num=len(dic[l])),dic[l])
#            legend.append(l)
#plt.legend(legend)
#plt.savefig('teste.jpg')
#plt.figure()
#plt.show()    

legend=[]
for l in dic:
    if l!='World' and l!='China':
        if dic[l][-1]>1000:
            plt.plot(np.linspace(0,9,num=10),dic[l][0:10])
            legend.append(l)
plt.legend(legend)
plt.savefig('teste.jpg')
plt.figure()
plt.show()    