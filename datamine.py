import pandas as pd
import urllib
import numpy as np
import datetime
#url='https://brasil.io/dataset/covid19/caso?format=csv'


######Escolha a data e type aqui#########
data='2020-04-07'
##################################



url='https://brasil.io/dataset/covid19/caso?date='+data+'&place_type=state&format=csv'
#url='https://raw.githubusercontent.com/RamiKrispin/coronavirus-csv/master/coronavirus_dataset.csv'

response = urllib.request.urlopen(url)
dataset = pd.read_csv(response,header=0)



geo = dataset.iloc[:, [8]].values
confirmados=dataset.iloc[:, [4]].values
obitos=dataset.iloc[:, [5]].values
list1=['confirmados_sec']*len(geo)
list2=['obitos_sec']*len(geo)
nome=list1+list2

datastr=datetime.datetime.strptime(data, '%Y-%m-%d').strftime('%d/%m/%Y')

listadata=[datastr]*2*len(geo)


dummy={
       'nome':nome,
       'geocode':np.append(geo,geo),
       'valor':np.append(confirmados,obitos),
       'data':listadata}


dataset = pd.DataFrame(dummy, columns = ['nome', 'geocode','valor','data'])


dataset.to_csv(r''+data+'.csv', index = False, sep=';')


#
#cidades=dataset[dataset.iloc[:, 3].values=='city']
#estados=dataset[dataset.iloc[:, 3].values=='state']
#
# 
#
#from collections import Counter
#place=list(Counter(y).keys())
#
#index=int(input('number:  '))
#
#bsb=dataset[dataset.iloc[:, 2].values==place[index]]
#
