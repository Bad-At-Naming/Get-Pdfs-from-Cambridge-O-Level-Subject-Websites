from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import os
import re

Subject_Links = []  
"""
Make a list of all the subjects you want to get the syllabi and past papers of and replace the [] with said list e.g.:

Subject_Links = ['https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-pakistan-studies-2059/', 'https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-islamiyat-2058/', 'https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-urdu-first-language-3247/', 'https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-literature-in-english-2010/', 'https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-english-language-1123/', 'https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-mathematics-d-4024/'] 

for the syllabi and past papers of the subjects: Pakistan Studies, Islamiyat, Urdu First Language, Literature In English, English Language, Mathematics D

"""


def get_title(Link):
    Link = Link.split("cambridge-o-level-")[1]

    if Link[-1] == "/":
        Link = Link[:len(Link)-1]

    Link = re.sub(r'[0-9]+', '', Link)

    if Link[-1] == "-":
        Link = Link[:len(Link)-1]

    return Link.title().replace("-", " ")


Subject_Names = []


def prep():
    os.mkdir("./Class X/")
    for n in range(len(Subject_Links)):
        Subject_Names.append(get_title(Subject_Links[n]))

    for x in range(len(Subject_Names)):
        os.mkdir("./Class X/"+Subject_Names[x])
        os.mkdir("./Class X/"+Subject_Names[x]+"/Syllabi")
        os.mkdir("./Class X/"+Subject_Names[x]+"/Exam Papers")


def download_past_papers():
    for n in range(len(Subject_Links)):  # Gets the past paper pdfs
        print(f"starting {Subject_Names[n]} past papers")
        With_Past_Papers = Subject_Links[n]+"/past-papers/"
        html = urlopen(With_Past_Papers)

        # Used to actually access the pdf files
        Base_Link = "https://www.cambridgeinternational.org"
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for link in soup.find_all(attrs={'href': re.compile(".pdf")}):
            # Gets all pdf files from the page, needs to be appended to Base link to be accessed
            links.append(str(link.get('href')))

        for i in range(len(links)):
            # Appends pdf image link to base link to access pdf file
            pdf = requests.get(Base_Link+links[i])
            Name_Of_Pdf_File = links[i].split("-", 1)[1]
            with open(("./Class X/"+Subject_Names[n]+"/Exam Papers/"+Name_Of_Pdf_File), 'wb') as f:
                f.write(pdf.content)
            print(f"done {Name_Of_Pdf_File}")
        print(f"done {Subject_Names[n]} past papers")


def download_syllabus():
    for n in range(len(Subject_Links)):  # Gets the syllabus pdfs
        print(f"starting {Subject_Names[n]} syllabus")
        With_Past_Papers = Subject_Links[n]
        html = urlopen(With_Past_Papers)

        # Used to actually access the pdf files
        Base_Link = "https://www.cambridgeinternational.org"
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for link in soup.find_all(attrs={'href': re.compile(".pdf")}):
            # Gets all pdf files from the page, needs to be appended to Base link to be accessed
            links.append(str(link.get('href')))

        for i in range(len(links)):
            # Appends pdf image link to base link to access pdf file
            pdf = requests.get(Base_Link+links[i])
            Name_Of_Pdf_File = links[i].split("-", 1)[1]
            with open(("./Class X/"+Subject_Names[n]+"/Syllabi/"+Name_Of_Pdf_File), 'wb') as f:
                f.write(pdf.content)
            print(f"done {Name_Of_Pdf_File}")
        print(f"done {Subject_Names[n]} syllabi")


prep()
download_past_papers()
download_syllabus()
