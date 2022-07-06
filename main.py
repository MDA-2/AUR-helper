from bs4 import BeautifulSoup
import requests
import re
import sys
import os

def installPackages():
    os.system("git clone https://aur.archlinux.org/" + sys.argv[2])
    os.system("cd " + sys.argv[2])
    os.system("makepkg -si")
def findPackages(x):
    url = "https://aur.archlinux.org/packages?O=0&SeB=nd&K=" + x + "&outdated=&SB=p&SO=d&PP=50&submit=Go"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    results = soup.table.find_all(string=re.compile('a'))
    print(results)

if sys.argv[1] == "-i":
    installPackages()
if sys.argv[1] == "-f":
    findPackages(sys.argv[2])
