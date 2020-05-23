from bs4 import BeautifulSoup
import requests


def cases():
    source=requests.get('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India').text
    soup = BeautifulSoup(source, 'lxml')
    head=soup.find_all('th')
    
    total=str(head[99])[4:-7]
    deaths=str(head[100])[16:-5]
    recovered=str(head[101])[16:-5]
    active=str(head[102])[16:-5]
    
    return total,deaths,recovered,active