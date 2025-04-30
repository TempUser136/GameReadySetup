import requests
import subprocess
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service


url="https://dotnet.microsoft.com/en-us/download/dotnet-framework"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
child_soup = soup.find('table', {'class': 'table'})
children = child_soup.findChildren("td")
first = children[0]
print(first)
linkTag=first.findChildren("a")
print(linkTag[0].get('href'))
parts = str(linkTag[0].get('href')).split('/')

newUrl=url+'/'+parts[len(parts)-1]
page=requests.get(newUrl)
soup = BeautifulSoup(page.content, "html.parser")
child_soup = soup.find('a', {'data-bi-dlnm': '.NET Framework Runtime Download'})
##child_soup = soup.find('a', {'data-bi-dlnm': ".NET Framework Runtime Download"})
print(child_soup.get('href'))

lastUrl = "https://dotnet.microsoft.com/" + child_soup.get('href')

page=requests.get(lastUrl)
soup = BeautifulSoup(page.content, "html.parser")
child_soup = soup.find('p', {'class': 'text-center lead mb-5'})
downloadLink=child_soup.find("a").get('href')


print(downloadLink)
local_filename = '.Net Framework Runtime.exe'

headers = {
   'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64)'
}

response = requests.get(downloadLink, stream=True, headers=headers)

with open(local_filename, 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
print(type(response))
 
