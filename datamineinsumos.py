import requests
import urllib.request
from datetime import date
from bs4 import BeautifulSoup
import csv


Uf={11:'Rondônia',
12:'Acre',
13 :'Amazonas',
14 :'Roraima',
15 :'Pará',
16:'Amapá',
17 :'Tocantins',
21 :'Maranhão',
22 :'Piauí',
23 :'Ceará',
24 :'Rio Grande do Norte',
25 :'Paraíba',
26 :'Pernambuco',
27 :'Alagoas',
28:'Sergipe',
29:'Bahia',
31:'Minas Gerais',
32:'Espírito Santo',
33:'Rio de Janeiro',
35:'São Paulo',
41:'Paraná',
42:'Santa Catarina',
43:'Rio Grande do Sul',
50:'Mato Grosso do Sul',
51:'Mato Grosso',
52:'Goiás',
53:'Distrito Federal'}


nomeColuna=['alcool em gel', 'cloroquina', 'testes pcr', 'teste rápido', 'mascara cirurgica', 'mascara n95', 'mais médicos', 'leitos locados']
nomeColuna2=['leitos uti sus', 'leitos uti nao sus']
nomePhp=['alcool','cloroquina','pcr','kit','mascara_3_camadas', 'mascara95','mais_medicos','graflocados']
nomePhp2=['uti_sus','uti_n_sus']
finalCsv=[]
# Set the URL you want to webscrape from
for estado in Uf:
    #temp={'Estado':Uf[estado]}
    for i in range(len(nomePhp)):
        url = 'https://covid-insumos.saude.gov.br/paineis/insumos/graficos/'+nomePhp[i]+'.php?uf='+str(estado)
        print(url)
    
        response = requests.get(url)
    
        soup = BeautifulSoup(response.text, "html.parser")
        
        line_count = 1 #variable to track what line you are on
        for one_a_tag in soup.findAll('script'):
            if one_a_tag.string != None:
                dataPoint=one_a_tag.string.find('data')
                valueStart=one_a_tag.string[dataPoint:].find('[')+1+dataPoint
                valueEnd=one_a_tag.string[dataPoint:].find(']')+dataPoint-1
                dataPoint2=one_a_tag.string.find('categories')
                valueStart2=one_a_tag.string[dataPoint2:].find('[')+2+dataPoint2
                valueEnd2=one_a_tag.string[dataPoint2:].find(']')+dataPoint2-2
                finalCsv.append({'nome':nomeColuna[i],'geocode':estado,'valor':one_a_tag.string[valueStart:valueEnd],'data':one_a_tag.string[valueStart2:valueEnd2]})
                #temp.update({nomeColuna[i]: one_a_tag.string[valueStart:valueEnd]})
    leitostotal=0    
    for j in range(len(nomePhp2)):
        
        url = 'https://covid-insumos.saude.gov.br/paineis/insumos/graficos/'+nomePhp2[j]+'.php?uf='+str(estado)
        print(url)
    
        response = requests.get(url)
    
        soup = BeautifulSoup(response.text, "html.parser")
        
        line_count = 1 #variable to track what line you are on
        for one_a_tag in soup.findAll('script'):
            if one_a_tag.string != None:
                dataPoint=one_a_tag.string.find('data')
                valueStart=one_a_tag.string[dataPoint:].find('[')+1+dataPoint
                valueEnd=one_a_tag.string[dataPoint:].find(']')+dataPoint-1
                leitostotal+=int(one_a_tag.string[valueStart:valueEnd])
                dataPoint2=one_a_tag.string.find('categories')
                valueStart2=one_a_tag.string[dataPoint2:].find('[')+2+dataPoint2
                valueEnd2=one_a_tag.string[dataPoint2:].find(']')+dataPoint2-2
                finalCsv.append({'nome':nomeColuna2[j],'geocode':estado,'valor':one_a_tag.string[valueStart:valueEnd],'data':one_a_tag.string[valueStart2:valueEnd2]})
                #temp.update({nomeColuna[i]: one_a_tag.string[valueStart:valueEnd]})
    finalCsv.append({'nome':'leitos total','geocode':estado,'valor':leitostotal,'data':one_a_tag.string[valueStart2:valueEnd2]})
        

csvCols=['nome','geocode','valor','data']
csv_file='insumos'+date.today().strftime("%b-%d-%Y")+'.csv'

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csvCols,lineterminator = '\n')
        writer.writeheader()
        for data in finalCsv:
            writer.writerow(data)
except IOError:
    print("I/O error")

