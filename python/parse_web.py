import requests
import urllib.request
import re
import html
from bs4 import BeautifulSoup
import csv

# specify the url
quote_page = 'https://www.appnexus.com/third-party-providers'

# query the website and return the html to the variable ‘page’
page = requests.get(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.text, 'html.parser')

ar_category=soup.findAll('h3')
ar_table=soup.findAll('table')
ar_table_abc={}
ar_table_company={}
ar_save_company = ["xaxis","zillow","zodiak active","zedo","zebestof","zalando","yahoo","wayfair","weborama",
                    "webads","ve interactive","varick media","underdog media","tvty","tradelab","taboola","supership","sublime skinz",
                    "smartclip","sizmek","simplifi","signal digital","schibsted","sanoma media","rs internet","roi media","rockerbox",
                    "quisma","powerLinks media","plista","platform integrations","one advertising","omnicom media group","nielsen","netnames","netcom medya",
                    "mythings","mobilefuse","mindshare worldwide","mindshare singapore","microsoft media network","microsoft advertising","meredith","mediamark pty","mediacom",
                    "media digital","media impact","liveramp","linkedIn","linkdotnet","light reaction","keyade","jpmorgan chase","iponweb",
                    "integral science","hurra communications","headlight","gumtree","greenhouse group","getintent","gemius","forum communications",
                    "forensiq","falk technologies","exponential","emerse","toro","ebay","drawbridge","doubleclick","distribeo","cpx interactive",
                    "conversant","connect ads for programming","collective","claranet","cardlytics","captify technologies","brightroll","bluekai",
                    "bering","bannerconnect","axel springer","audience science","appnexus","amnet","affiperf","groupm"
                    ]


i=0
count=0
result={}
for table in ar_table:
    ar_td=ar_table[i].findAll('td')
    for td in ar_td:
        #text_abc=re.sub(r"[\W_]+","",td.text.strip()).lower()
        #text_abc = ' '.join( [w for w in text_abc.split() if len(w)>2] )
        #text_abc = re.sub(r"ltd","",text_abc)

        text_abc = re.sub(r"[^A-Za-z0-9 ]+","",td.text.strip()).lower()
        text_abc = ' '.join( [w for w in text_abc.split() if len(w)>2] )
        text_abc = re.sub(r"\s*ltd+\s*","",text_abc).strip()
        text_abc = re.sub(r"\s*inc+\s*","",text_abc).strip()    

        res = [ele for ele in ar_save_company if(text_abc.startswith(ele))] 
        if len(res)>0:
            text_abc = res[0]
        
        if text_abc in ar_table_abc:
            if td.text.strip() not in ar_table_abc[text_abc]: 
                ar_table_abc[text_abc]+="," + td.text.strip()
        else:
            ar_table_abc[text_abc]=td.text.strip()
        #line=td.text.strip() + ';' + re.sub(r"[1-6].", "",ar_category[i].text.strip().encode('ascii', 'ignore').decode('ascii')).strip() 
        category = re.sub(r"[1-6].", "",ar_category[i].text.strip().encode('ascii', 'ignore').decode('ascii')).strip()
        if text_abc in result:
            if category not in result[text_abc]:
                result[text_abc] += ',' + category
        else:    
            result[text_abc] = category
        count+=1
    i=i+1
    
    if i>5:
        break

print(count)

#print(ar_table[0].findAll('td'))

with open('appNexus_cat.csv','w') as file:
    for key in result:
        company = ar_table_abc[key]
        names = ""
        if len(ar_table_abc[key].split(','))>1:
            company = ar_table_abc[key].split(',')[0]
            names = ar_table_abc[key]
        
        file.write(company + ";" + result[key] + ";" + names)
        file.write('\n')

file.close()

#print(re.sub(r"[1-6]. ", "",ar_category[0].text.strip().encode('ascii', 'ignore').decode('ascii')))
#print(ar_category[1])
#print(ar_category[2])
#print(ar_category[3])
#print(ar_category[4])
#print(ar_category[5])