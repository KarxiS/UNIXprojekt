from grafMaker import grafMaker
from stranka import stranka
from websiteBrowser import websiteBrowser
import tkinter as tk
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Use Selenium to navigate to the webpage

root = tk.Tk()
root.geometry("600x600")
URL = "https://vzdelavanie.uniza.sk/vzdelavanie"
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get(URL+"/plany.php")

#message PREDMETY VYSLEDOK ------------

def button_clicked():
    strankyObj = [];

    analyzator = websiteBrowser(URL);
    adresy = analyzator.ziskajAdresyPredmetov(driver.page_source);
    adresyHtml = analyzator.nacitajObsahAdresies();

    for adresa in adresyHtml:
        strankaLocalObj = stranka(adresa)
        strankaLocalObj.spracuj()
        strankyObj.append(strankaLocalObj)

    grafMakerObj = grafMaker(strankyObj)
    text= grafMakerObj.vytvorGraf()
    tkText.set(text)
    strankyObj=[]
    driver.get(URL + "/plany.php")
    grafMakerObj.resetujPredmety()





button = tk.Button(root, text="Potvrd vyber", command=button_clicked)
button.place(x=40,y=10,width=80,height=30)
labelNajlepsie= tk.Label(root, text = "Vysledok analýzy:", font=("Helvetica", 17))
labelNajlepsie.place(x=40,y=80,width=220,height=30)
tkText = tk.StringVar();
tkText.set("Tu sa zobrazi vysledok \n Vyberte si studijny program v browseri a kliknite na tlacitko")
msgOutputNajlepsie = tk.Message(root, textvariable=tkText,anchor=tk.NW, font=("Helvetica", 15))
msgOutputNajlepsie.place(x=40,y=110,width=480,height=470)

# labelNajhorsie= tk.Label(root, text = "Najhorsie predmety", font=("Helvetica", 15))
# labelNajhorsie.place(x=40,y=170,width=220,height=30)
# msgOutputNajhorsie = tk.Message(root, text = "output", font=("Helvetica", 20))
# msgOutputNajhorsie.place(x=240,y=250,width=220,height=85)

#
# # Run the main loop
root.mainloop()

# Use Selenium to navigate to the course page





# Close the web browser
