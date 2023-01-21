import os
import bs4
import requests
from sys import *

def PrashantsLinksDisplay(URL):
    res = requests.get(URL)
    print(type(res))

    soup = bs4.BeautifulSoup(res.text,'lxml')
    print("type(soup) : ",type(soup))
    
    links = soup.find_all('a', href = True)
    
    return(links)

def main():
    
    print("-----Link Extracter By Prashant Paulbudhe-----")
    
    print("-----Application Name  :   Link Extracter-----")
    
    print("Application Name : ",argv[0])
    
    if(len(argv) == 2):
        if(argv[1] == '-h' or argv[1] == '-H'):
            print("This Script is used to fetch links from wikipedia.")
            exit()
        
        if(argv[1] == '-u' or argv[1] == '-U'):
            print("Usage : ApllicationName")
            exit()
    
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    
    arr = PrashantsLinksDisplay(url)
    
    print("--Links Are--")
    
    for element in arr:
        if '#' not in element['href']:
            print(element['href'])
        

if __name__ == "__main__":
    main()    