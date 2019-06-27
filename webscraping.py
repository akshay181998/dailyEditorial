import requests 
from bs4 import BeautifulSoup
from csv import writer 
import array as arr

output = [] ; 
editorial = [] ;
response = requests.get('https://www.thehindu.com/opinion/editorial/')
soup = BeautifulSoup(response.text , 'html.parser')
posts = soup.find_all('a',href=True,class_='ES2-100x4-text1-heading')
for post in posts:
  output.append(post['href'])

for x in output :
  res = requests.get(x)
  s = BeautifulSoup(res.text , 'html.parser')
  po = s.find_all('p',class_ = 'drop-caps')
  for c in po :
    editorial.append(c.get_text())
    print(c.get_text())

def ed():
  return editorial