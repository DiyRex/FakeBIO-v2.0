import json
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") 


def pick_useragent():
    f = open('UserAgents/useragents.json',)
    randusr = random.randint(1, 5)
    data = json.load(f)
    for i in data['User_Agents']:
        return i["useragent{}".format(randusr)]

useragent= pick_useragent()
 
headers = {"User-Agent": useragent}

response = requests.get("https://www.fakeaddressgenerator.com/", headers=headers)


soup = BeautifulSoup(response.content,"html.parser")
dat = str(soup.prettify())

tabledata = soup.find_all("div", class_="col-sm-6 no-padding")


tab = soup.find_all('table', class_='table common-table')

for td in tab:
    name = soup.find_all("td")[1].get_text()
    gend = soup.find_all("td")[3].get_text()
    title = soup.find_all("td")[5].get_text()
    race = soup.find_all("td")[7].get_text()
    bday = soup.find_all("td")[9].get_text()
    ssn = soup.find_all("td")[11].get_text()
    street = soup.find_all("td")[14].get_text()
    city = soup.find_all("td")[16].get_text()
    state = soup.find_all("td")[18].get_text()
    statefull = soup.find_all("td")[20].get_text()
    zip = soup.find_all("td")[22].get_text()
    phone = soup.find_all("td")[24].get_text()
    mobile = soup.find_all("td")[26].get_text()

file = open("UserData/UserData.txt","a")

def write():
    file.writelines("==========  FakeBIO V 2.0  ==  " + dt_string + "  ==========" + "\n")
    file.writelines("\n")
    file.writelines("Name : " + name + "\n")
    file.writelines("Gend : " + gend + "\n")
    file.writelines("Title : " + title + "\n")
    file.writelines("Race : " + race + "\n")
    file.writelines("Bday : " + bday + "\n")
    file.writelines("SSN : " + ssn + "\n")
    file.writelines("Steet : " + street + "\n")
    file.writelines("City : " + city + "\n")
    file.writelines("State : " + state + "\n")
    file.writelines("StaFull : " + statefull + "\n")
    file.writelines("Zip : " + zip + "\n")
    file.writelines("Phone : " + phone + "\n")
    file.writelines("Mobile : " + mobile + "\n")
    file.writelines("\n")
    file.writelines("---------------------------- Script By DiyRex :) -----------" + "\n")
    file.writelines("\n")

write()
