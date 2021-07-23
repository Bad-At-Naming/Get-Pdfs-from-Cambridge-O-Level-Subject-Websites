from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import os
import re

Subject_Links = [] # Make a list of all the links of the subjects you want to download pdfs of

def get_title(Link):
    Link = Link.split("cambridge-o-level-")[1]


    if Link[-1] == "/" :
        Link = Link[:len(Link)-1]

    Link = re.sub(r'[0-9]+', '', Link)

    if Link[-1] == "-" :
        Link = Link[:len(Link)-1]

    return Link.title().replace("-"," ")

Subject_Names = []
def prep():
    for n in range(len(Subject_Links)):
        Subject_Names.append(get_title(Subject_Links[n]))

    for x in range(len(Subject_Names)):
        os.mkdir("./"+Subject_Names[x])



def download_past_papers():
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

def download_syllabus():
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

prep()
download_past_papers()
download_syllabus()
