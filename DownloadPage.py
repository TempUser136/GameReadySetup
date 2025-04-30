import requests
import subprocess
from bs4 import BeautifulSoup
url="https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170"

query_parameters = {"downloadformat": "csv"}

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
child_soup = soup.find_all('a')

downloadLink = ""

for i in child_soup:
    if "vc_redist.x64" in  str(i.get('href')):
      print(i.get('href'))
      downloadLink = i.get('href')

local_filename = 'VC_redist.x64.exe'

headers = {
   'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64)'
}
response = requests.get(downloadLink,stream=True, headers=headers)

with open(local_filename, 'wb') as f:
   for chunk in response.iter_content(chunk_size=8192):
      if chunk:
         f.write(chunk)

exe_path = "VC_redist.x64.exe"

subprocess.run([exe_path], check=True)