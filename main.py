from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import os

Subject_Links = []   #Put links of all subjects u want the pdfs from
Subject_Names = []   #Put names of all subjects of the links u put above **IN THE SAME ORDER** as you did above

for x in range(len(Subject_Names)):
    os.mkdir("./"+Subject_Names[x])

for n in range(len(Subject_Links)):   #Gets the past paper pdfs
    With_Past_Papers = Subject_Links[n]+"/past-papers/"
    html = urlopen(With_Past_Papers)

    Base_Link = "https://www.cambridgeinternational.org"   #Used to actually access the pdf files
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all(attrs={'href': re.compile(".pdf")}):
        links.append(str(link.get('href')))   #Gets all pdf files from the page, needs to be appended to Base link to be accessed

    for i in range(len(links)):
        pdf = requests.get(Base_Link+links[i])   #Appends pdf image link to base link to access pdf file
        Name_Of_Pdf_File = links[i].split("-",1)[1]
        with open(("./"+Subject_Names[n]+"/"+Name_Of_Pdf_File),'wb') as f: 
            f.write(pdf.content) 

for n in range(len(Subject_Links)): #Gets the syllabus pdfs
    With_Past_Papers = Subject_Links[n]
    html = urlopen(With_Past_Papers)

    Base_Link = "https://www.cambridgeinternational.org"   #Used to actually access the pdf files
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all(attrs={'href': re.compile(".pdf")}):
        links.append(str(link.get('href')))   #Gets all pdf files from the page, needs to be appended to Base link to be accessed

    for i in range(len(links)):
        pdf = requests.get(Base_Link+links[i])   #Appends pdf image link to base link to access pdf file
        Name_Of_Pdf_File = links[i].split("-",1)[1]
        with open(("./"+Subject_Names[n]+"/"+Name_Of_Pdf_File),'wb') as f:
            f.write(pdf.content)