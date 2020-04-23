import pandas as pd
import urllib
import numpy as np
import datetime


######Escolha a data e type aqui#########
data='2020-04-01'
##################################



url='https://brasil.io/dataset/covid19/caso?date='+data+'&place_type=city&format=csv'

response = urllib.request.urlopen(url)
dataset = pd.read_csv(response,header=0)
dataset=dataset[dataset.city != 'Importados/Indefinidos']


geo = dataset.iloc[:, [8]].values
confirmados=dataset.iloc[:, [4]].values
#obitos=dataset.iloc[:, [5]].values
list1=['confirmadosmunicipio_sec']*len(geo)
#list2=['obitos_sec']*len(geo)
#nome=list1+list2

datastr=datetime.datetime.strptime(data, '%Y-%m-%d').strftime('%d/%m/%Y')

listadata=[datastr]*len(geo)


geo = [int(i[0]) for i in geo.tolist()]
confirmados = [i[0] for i in confirmados.tolist()]


dummy={
       'nome':list1,
       'geocode': geo,
       'valor': confirmados,
       'data':listadata}


dataset = pd.DataFrame(dummy, columns = ['nome', 'geocode','valor','data'])


dataset.to_csv(r''+data+'mun.csv', index = False, sep=';')
