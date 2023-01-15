import json

from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class websiteBrowser:


    # poslem, tu spracujem cez BS
    def __init__(self, URL):

        self.adresy = []
        self.predmety = [];
        self.rocnik = 1;
        s = Service(ChromeDriverManager().install())

        self.URL = URL;
        self.driver = webdriver.Chrome(service=s)


    def ziskajAdresyPredmetov(self,html):
        URL = self.URL;
        self.adresy = []

        #self.driver.get(URL+"/plany.php?f=5&t=Z&m=2&r=1&z=MN&c=4")

        # Use Beautiful Soup to parse the HTML of the webpage
        soup = BeautifulSoup(html, 'html.parser')

        # Find the table with the courses
        table = soup.find('table', attrs={'id': 'id-tabulka-studijnych-planov'})

        # Find all the rows in the table
        rows = table.find_all('tr')
        # prehladavam hlavnu stranku so stidujnimy a robim objekty , ktore sa samy spracujku
        # Iterate over the rows
        for row in rows:
            # Find the cells in the row

            if (row.has_attr('class')) and ((row['class'][0] == 'odd') or (row['class'][0] == 'evn')):
                cells = row.find_all('td')

                # Extract the text from the cells
                course = cells[0].text
                link = cells[0].find('a')['href']
                self.adresy.append(URL + "/" + link)



        return self.adresy;

    def nacitajObsahAdresies(self):

        localObsahAdries = []
        for adresa in self.adresy:
            self.driver.get(adresa)
            localObsahAdries.append(self.driver.page_source)


        # Use Selenium to navigate to the course page


        # Use Beautiful Soup to parse the HTML of the course page
        return localObsahAdries
