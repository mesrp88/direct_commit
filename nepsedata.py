from bs4 import BeautifulSoup
import requests

headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
URL1= "https://nepsealpha.com/trading-signals/sell-table/"
page1= requests.get(URL1, headers= headers)
soup= BeautifulSoup(page1.content, 'html.parser')
table = soup.find('table')
table_rows= table.find_all('tr')
table_header= table.find_all('th')
 
all_header= [th.text for th in table_header]
nepse_csv={}
rows= []
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text for i in td]
    rows.append(row)

del rows[0]
new_sym=[]
for index in range(len(all_header)):
    for row in rows[1:]:
        row_e= row[index]
    new_sym.append(row_e[index])
nepse_csv['symbols']=new_sym
print(new_sym)
print(nepse_csv)






    
