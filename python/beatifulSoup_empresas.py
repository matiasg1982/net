from bs4 import BeautifulSoup
import requests
import re
import time
from random import randint


def ScrapEmpresasElEconomista(arTr):
    
    arResult = list()
    dCompany = {}

    for iCountCompanies,bsTr in enumerate(arTr,1):
        name = bsTr.find(class_='tal').find_all('a')[0].contents[0]
        link = bsTr.find(class_='tal').find_all('a')[0].get('href')
        income = bsTr.find(class_='tal').findNext('td').contents[0]
        activity = bsTr.find(class_='tal').findNext('td').findNext('td').find_all('abbr')[0].get('title')
        print(activity)
        company_page = requests.get(link)
        company_soup = BeautifulSoup(company_page.content, 'html.parser')
        if company_soup.find(class_="empre-datos"):

            arTd = company_soup.find(class_="empre-datos").find_all('td')
            dCompany.clear()
            for td in arTd:
                if td.find(text='Denominación'):
                    strCompanyName = td.find(text='Denominación').findNext('td').contents[0]
                if td.find(text='Actividad'):
                    strCompanyActivity = td.find(text='Actividad').findNext('td').contents[0]
                if td.find(text='Domicilio Social'):
                    strCompanyAddress = td.find(text='Domicilio Social').findNext('td').contents[0].strip()
                    strCompanyAddress = re.sub("\t|\n","",strCompanyAddress)
                if td.find(text='Localidad'):
                    strCompanyCity = td.find(text='Localidad').findNext('td').contents[0]
                if td.find(text='Teléfono'):
                    strCompanyTel = td.find(text='Teléfono').findNext('td').find(text=True, recursive=False)
                if td.find(text='Otros Teléfonos'):
                    strCompanyTel_2 = td.find(text='Otros Teléfonos').findNext('td').contents[0]
                    strCompanyTel_2 = re.sub("\t|\n","",strCompanyTel_2)
                if td.find(text='Página Web'):
                    strCompanySite = td.find(text='Página Web').findNext('td').find_all('a')[0].get('href')

            dCompany["name"]=strCompanyName
            dCompany["activity"]=strCompanyActivity
            dCompany["address"]=strCompanyAddress
            dCompany["city"]=strCompanyCity
            dCompany["tel"]=strCompanyTel
            dCompany["tel_2"]=strCompanyTel_2
            dCompany["site"]=strCompanySite
            
            arResult.append(dCompany)
            break

    return arResult


page = requests.get("https://ranking-empresas.eleconomista.es/empresas-VALENCIA.html")
soup = BeautifulSoup(page.content, 'html.parser')

#iCurrentPage = firstPage
iFirstPage = int(soup.find_all('li',{"class":'current'})[0].findNext('span').contents[0])
iLastPage = 0
if soup.find_all('li',{"class":'arrow'})[1]:
    iLastPage = int(soup.find_all('li',{"class":'arrow'})[1].previousSibling.find(text=True, recursive=False))
iCurrentPage = iFirstPage



exit()

if soup.find_all('tr',{"class":'tr_hover_even'}):
    arTr = soup.find_all('tr',{"class":'tr_hover_even'})

    results=ScrapEmpresasElEconomista(arTr)
else:
    exit()

#iSecondsWait = randint(0, 10)
#time.sleep(iSecondsWait)


#print(results)
