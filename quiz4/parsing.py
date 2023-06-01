import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
file = open('gpu.csv','w',newline='\n')
csv_obj = csv.writer(file)
csv_obj.writerow(['Gpu Name'])
payloads = {'page':1,'Tid':7708}
url  =  'https://www.newegg.ca/GPUs-Video-Graphics-Cards/SubCategory/ID-48'

while payloads['page']<6:
    response = requests.get(url,params=payloads)
    # print(response)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    gpu_container = soup.find('div', class_='list-wrap')
    gpu_names = gpu_container.find_all('a', class_='item-title')
    for gpu_name in gpu_names:
        title = gpu_name.text
        csv_obj.writerow([title])
        print(title)
    payloads['page']+=1
    sleep(randint(15,20))